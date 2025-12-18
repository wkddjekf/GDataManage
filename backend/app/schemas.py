from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID

class PlanRecordCreate(BaseModel):
    update_date: date
    work: str
    table_name: str
    owner: str
    note: Optional[str] = ""
    p4_path: str

class PlanRecordOut(BaseModel):
    id: UUID
    update_date: date
    work: str
    table_name: str
    owner: str
    note: str
    p4_path: str

    class Config:
        from_attributes = True

class PlanRecordUpdate(BaseModel):
    update_date: date
    work: str
    table_name: str
    owner: str
    note: str = ""
    p4_path: str

class RecordUpdate(BaseModel):
    update_date: Optional[date] = None
    work: Optional[str] = None
    table_name: Optional[str] = None
    owner: Optional[str] = None
    note: Optional[str] = None
    p4_path: Optional[str] = None
