from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select, distinct
from datetime import date
from uuid import UUID

from .db import SessionLocal, engine, Base
from .models import PlanRecord
from .schemas import (
    PlanRecordCreate,
    PlanRecordOut,
    PlanRecordUpdate,
    PlanRecordUpdateNote,  
)

app = FastAPI(
    title="GDataManage API",
    description="기획 데이터 히스토리 관리 API",
    version="1.0.0",
)

# CORS (프론트 분리/통합 모두 대비)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 운영 시 도메인 제한 권장
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 테이블 자동 생성 (Neon에 이미 있으면 영향 없음)
Base.metadata.create_all(bind=engine)

# DB 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# API
# ---------------------------

@app.post("/records", response_model=PlanRecordOut)
def create_record(
    payload: PlanRecordCreate,
    db: Session = Depends(get_db),
):
    record = PlanRecord(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@app.delete("/records/{record_id}")
def delete_record(record_id: str, db=Depends(get_db)):
    record = db.query(PlanRecord).filter(PlanRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(record)
    db.commit()
    return {"ok": True}

@app.patch("/records/{record_id}")
def update_record(record_id: str, payload: PlanRecordUpdate, db=Depends(get_db)):
    record = db.query(PlanRecord).filter(PlanRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    # 부분 수정 대응 (PATCH의 핵심)
    if payload.update_date is not None:
        record.update_date = payload.update_date
    if payload.work is not None:
        record.work = payload.work
    if payload.table_name is not None:
        record.table_name = payload.table_name
    if payload.owner is not None:
        record.owner = payload.owner
    if payload.note is not None:
        record.note = payload.note
    if payload.p4_path is not None:
        record.p4_path = payload.p4_path

    db.commit()
    db.refresh(record)
    return record

@app.get("/records", response_model=list[PlanRecordOut])
def list_records(
    update_date: date | None = None,
    work: str | None = None,
    table_name: str | None = None,
    limit: int = 200,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    stmt = select(PlanRecord).order_by(PlanRecord.created_at.desc())

    if update_date:
        stmt = stmt.where(PlanRecord.update_date == update_date)
    if work:
        stmt = stmt.where(PlanRecord.work.ilike(f"%{work}%"))
    if table_name:
        stmt = stmt.where(PlanRecord.table_name == table_name)

    stmt = stmt.limit(min(limit, 500)).offset(max(offset, 0))
    return db.execute(stmt).scalars().all()

@app.get("/tables", response_model=list[str])
def list_table_names(db: Session = Depends(get_db)):
    stmt = select(distinct(PlanRecord.table_name)).order_by(PlanRecord.table_name)
    return [row[0] for row in db.execute(stmt).all()]

@app.patch("/records/{record_id}/note", response_model=PlanRecordOut)
def update_note(
    record_id: str,
    payload: PlanRecordUpdateNote,
    db: Session = Depends(get_db),
):
    record = db.get(PlanRecord, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    record.note = payload.note
    from sqlalchemy import func
    record.updated_at = func.now()

    db.commit()
    db.refresh(record)
    return record

@app.delete("/records/{record_id}")
def delete_record(
    record_id: UUID,
    db: Session = Depends(get_db),
):
    record = db.get(PlanRecord, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()
    return {"ok": True}
