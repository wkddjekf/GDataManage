<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>GDataManage</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen flex">
  <!-- Sidebar -->
  <aside class="w-64 bg-[#0f5b70] text-white p-6">
    <div class="text-2xl font-bold mb-8">기획데이터 관리</div>

    <nav class="space-y-3">
      <button id="nav-register" class="w-full text-left px-3 py-2 rounded-lg bg-white/10 hover:bg-white/20">
        기획 데이터 등록
      </button>
      <button id="nav-view" class="w-full text-left px-3 py-2 rounded-lg bg-white/10 hover:bg-white/20">
        기획 데이터 확인
      </button>
    </nav>
  </aside>

  <!-- Main -->
  <main class="flex-1 p-8">
    <!-- Top -->
    <header class="mb-6">
      <h1 id="pageTitle" class="text-2xl font-bold text-gray-900">기획 데이터 등록</h1>
      <p class="text-gray-600 mt-1">업데이트 작업별 변경 데이터(P4 경로/테이블 등)를 기록합니다.</p>
    </header>

    <!-- Alerts -->
    <div id="alertBox" class="hidden mb-6 rounded-lg border p-4"></div>

    <!-- Register Page -->
    <section id="page-register" class="space-y-6">
      <div class="bg-white rounded-xl shadow p-6 border">
        <h2 class="font-bold text-lg mb-4">기획 데이터 등록</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="text-sm text-gray-700">업데이트 일자</label>
            <input id="r_update_date" type="date" class="mt-1 w-full border rounded-lg p-2" />
          </div>
          <div>
            <label class="text-sm text-gray-700">관련 작업</label>
            <input id="r_work" type="text" placeholder="예: ER-12345 / 작업명" class="mt-1 w-full border rounded-lg p-2" />
          </div>
          <div>
            <label class="text-sm text-gray-700">테이블 명</label>
            <input id="r_table_name" type="text" placeholder="예: Table_Whatever" class="mt-1 w-full border rounded-lg p-2" />
          </div>
          <div>
            <label class="text-sm text-gray-700">담당자</label>
            <input id="r_owner" type="text" placeholder="예: 혁" class="mt-1 w-full border rounded-lg p-2" />
          </div>

          <div class="md:col-span-2">
            <label class="text-sm text-gray-700">참고사항</label>
            <input id="r_note" type="text" placeholder="특이사항/주의사항" class="mt-1 w-full border rounded-lg p-2" />
          </div>

          <div class="md:col-span-2">
            <label class="text-sm text-gray-700">P4V 경로</label>
            <input id="r_p4_path" type="text" placeholder='예: //ER/Dev/Data/....' class="mt-1 w-full border rounded-lg p-2" />
          </div>
        </div>

        <div class="mt-5 flex gap-3">
          <button id="btnCreate"
            class="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700">
            데이터 등록
          </button>
          <button id="btnCreateExample"
            class="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300">
            예시 채우기
          </button>
        </div>
      </div>

      <!-- Register History -->
      <div class="bg-white rounded-xl shadow p-6 border">
        <div class="flex items-center justify-between mb-3">
          <h3 class="font-bold">등록 히스토리</h3>
          <div class="text-sm text-gray-500">
            <span id="historyCount">0</span>건
          </div>
        </div>

        <div class="overflow-auto border rounded-lg">
          <table class="min-w-[900px] w-full text-sm">
            <thead class="bg-gray-50">
              <tr>
                <th class="text-left p-3 border-b">업데이트 일자</th>
                <th class="text-left p-3 border-b">관련 작업</th>
                <th class="text-left p-3 border-b">테이블 명</th>
                <th class="text-left p-3 border-b">담당자</th>
                <th class="text-left p-3 border-b">P4V 경로</th>
                <th class="text-left p-3 border-b">참고사항</th>
                <th class="text-left p-3 border-b">삭제</th>
              </tr>
            </thead>
            <tbody id="historyBody"></tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- View Page -->
    <section id="page-view" class="hidden space-y-6">
      <div class="bg-white rounded-xl shadow p-6 border">
        <h2 class="font-bold text-lg mb-4">기획 데이터 확인</h2>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 items-end">
          <div>
            <label class="text-sm text-gray-700">업데이트 일자</label>
            <input id="q_update_date" type="date" class="mt-1 w-full border rounded-lg p-2" />
          </div>
          <div>
            <label class="text-sm text-gray-700">관련 작업(부분검색)</label>
            <input id="q_work" type="text" placeholder="예: ER-123" class="mt-1 w-full border rounded-lg p-2" />
          </div>
          <div>
            <label class="text-sm text-gray-700">테이블 선택</label>
            <select id="q_table_name" class="mt-1 w-full border rounded-lg p-2">
              <option value="">(전체)</option>
            </select>
          </div>
          <div class="flex gap-2">
            <button id="btnSearch"
              class="flex-1 px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700">
              조회
            </button>
            <button id="btnReset"
              class="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300">
              초기화
            </button>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-xl shadow p-6 border">
        <div class="flex items-center justify-between mb-3">
          <h3 class="font-bold">조회 결과</h3>

          <div class="flex items-center gap-2">
            <button id="btnEditToggle"
              class="px-3 py-1 rounded border bg-white hover:bg-gray-50">
              편집 모드: OFF
            </button>
            <button id="btnSaveAll" class="hidden px-3 py-1 rounded bg-blue-600 text-white hover:bg-blue-700">
              저장
            </button>

            <div class="text-sm text-gray-500 ml-2">
              <span id="resultCount">0</span>건
            </div>
          </div>
        </div>

        <div class="overflow-auto border rounded-lg">
          <table class="min-w-[900px] w-full text-sm">
            <thead class="bg-gray-50">
              <tr>
                <th class="text-left p-3 border-b">업데이트 일자</th>
                <th class="text-left p-3 border-b">관련 작업</th>
                <th class="text-left p-3 border-b">테이블 명</th>
                <th class="text-left p-3 border-b">담당자</th>
                <th class="text-left p-3 border-b">P4V 경로</th>
                <th class="text-left p-3 border-b">참고사항</th>
              </tr>
            </thead>
            <tbody id="resultBody"></tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

<script>
  // ✅ 여기에 너의 백엔드(FASTAPI) Render URL 넣어줘
  // 예: const API_BASE = "https://gdatamanage.onrender.com";
  const API_BASE = "https://gdatamanage.onrender.com";

  // ---------- UI helpers ----------
  const el = (id) => document.getElementById(id);

  function showAlert(type, msg) {
    const box = el("alertBox");
    box.classList.remove("hidden");
    box.className = "mb-6 rounded-lg border p-4"; // reset
    if (type === "success") box.classList.add("bg-green-50","border-green-200","text-green-800");
    if (type === "error") box.classList.add("bg-red-50","border-red-200","text-red-800");
    if (type === "info") box.classList.add("bg-blue-50","border-blue-200","text-blue-800");
    box.textContent = msg;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function hideAlert() {
    el("alertBox").classList.add("hidden");
  }

  function toQS(params) {
    const usp = new URLSearchParams();
    Object.entries(params).forEach(([k, v]) => {
      if (v !== null && v !== undefined && String(v).trim() !== "") usp.set(k, v);
    });
    const s = usp.toString();
    return s ? `?${s}` : "";
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  // ---------- API ----------
  async function apiFetch(path, options = {}) {
    const res = await fetch(`${API_BASE}${path}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...(options.headers || {})
      },
    });

    const text = await res.text();
    let data = null;
    try { data = text ? JSON.parse(text) : null; } catch { data = text; }

    if (!res.ok) {
      const detail = (data && data.detail) ? JSON.stringify(data.detail) : (typeof data === "string" ? data : JSON.stringify(data));
      throw new Error(`${res.status} ${res.statusText} - ${detail}`);
    }
    return data;
  }

  async function createRecord(payload) {
    return apiFetch("/records", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }

  async function listRecords(filters) {
    return apiFetch("/records" + toQS(filters), { method: "GET" });
  }

  async function listTables() {
    return apiFetch("/tables", { method: "GET" });
  }

  async function deleteRecord(id) {
    return apiFetch(`/records/${id}`, { method: "DELETE" });
  }

  async function updateRecord(id, payload) {
    return apiFetch(`/records/${id}`, {
      method: "PUT",
      body: JSON.stringify(payload),
    });
  }

  // ---------- Pages ----------
  function showPage(page) {
    hideAlert();

    const isRegister = page === "register";
    el("page-register").classList.toggle("hidden", !isRegister);
    el("page-view").classList.toggle("hidden", isRegister);
    el("pageTitle").textContent = isRegister ? "기획 데이터 등록" : "기획 데이터 확인";
  }

  el("nav-register").addEventListener("click", async () => {
    showPage("register");
    await refreshHistory();
  });

  el("nav-view").addEventListener("click", async () => {
    showPage("view");
    await refreshTablesDropdown();
    await doSearch(); // 들어오자마자 한번 조회
  });

  // ---------- Register actions ----------
  el("btnCreateExample").addEventListener("click", () => {
    const today = new Date().toISOString().slice(0,10);
    el("r_update_date").value = today;
    el("r_work").value = "ER-99999";
    el("r_table_name").value = "Table_Test";
    el("r_owner").value = "혁";
    el("r_note").value = "프론트 연동 테스트";
    el("r_p4_path").value = "//ER/Dev/Data/Test/TestData.json";
  });

  el("btnCreate").addEventListener("click", async () => {
    try {
      hideAlert();

      const payload = {
        update_date: el("r_update_date").value,
        work: el("r_work").value.trim(),
        table_name: el("r_table_name").value.trim(),
        owner: el("r_owner").value.trim(),
        note: el("r_note").value.trim(),
        p4_path: el("r_p4_path").value.trim(),
      };

      // 간단 검증
      if (!payload.update_date) return showAlert("error", "업데이트 일자를 입력해줘.");
      if (!payload.work) return showAlert("error", "관련 작업을 입력해줘.");
      if (!payload.table_name) return showAlert("error", "테이블 명을 입력해줘.");
      if (!payload.owner) return showAlert("error", "담당자를 입력해줘.");
      if (!payload.p4_path) return showAlert("error", "P4V 경로를 입력해줘.");

      const created = await createRecord(payload);
      showAlert("success", `등록 완료! id=${created.id}`);

      // ✅ 등록 후: 등록 페이지 아래 히스토리 갱신
      await refreshHistory();

    } catch (e) {
      showAlert("error", `등록 실패: ${e.message}`);
    }
  });

  function renderHistory(rows) {
    const tbody = el("historyBody");
    tbody.innerHTML = "";
    el("historyCount").textContent = rows.length;

    if (!rows.length) {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td class="p-4 text-gray-500" colspan="7">히스토리가 없습니다.</td>`;
      tbody.appendChild(tr);
      return;
    }

    rows.forEach(r => {
      const tr = document.createElement("tr");
      tr.className = "hover:bg-gray-50";
      tr.innerHTML = `
        <td class="p-3 border-b whitespace-nowrap">${r.update_date}</td>
        <td class="p-3 border-b">${escapeHtml(r.work)}</td>
        <td class="p-3 border-b whitespace-nowrap">${escapeHtml(r.table_name)}</td>
        <td class="p-3 border-b whitespace-nowrap">${escapeHtml(r.owner)}</td>
        <td class="p-3 border-b font-mono text-xs break-all">${escapeHtml(r.p4_path)}</td>
        <td class="p-3 border-b">${escapeHtml(r.note || "")}</td>
        <td class="p-3 border-b whitespace-nowrap">
          <button data-del-id="${r.id}" class="px-3 py-1 rounded bg-red-600 text-white hover:bg-red-700">
            삭제
          </button>
        </td>
      `;
      tbody.appendChild(tr);
    });

    tbody.querySelectorAll("[data-del-id]").forEach(btn => {
      btn.addEventListener("click", async () => {
        const id = btn.getAttribute("data-del-id");
        if (!confirm("정말 삭제할까요?")) return;
        try {
          await deleteRecord(id);
          showAlert("success", "삭제 완료!");
          await refreshHistory();
        } catch (e) {
          showAlert("error", `삭제 실패: ${e.message}`);
        }
      });
    });
  }

  async function refreshHistory() {
    const rows = await listRecords({ limit: 50, offset: 0 });
    rows.sort((a, b) => String(b.update_date).localeCompare(String(a.update_date)));
    renderHistory(rows);
  }

  // ---------- View actions ----------
  async function refreshTablesDropdown() {
    try {
      const tables = await listTables();
      const sel = el("q_table_name");
      const keep = sel.value;

      sel.innerHTML = `<option value="">(전체)</option>`;
      tables.forEach(t => {
        const opt = document.createElement("option");
        opt.value = t;
        opt.textContent = t;
        sel.appendChild(opt);
      });

      if (keep) sel.value = keep;
    } catch (e) {
      console.warn(e);
    }
  }

  let editMode = false;

  el("btnEditToggle").addEventListener("click", async () => {
    editMode = !editMode;
    el("btnEditToggle").textContent = editMode ? "편집 모드: ON" : "편집 모드: OFF";
    el("btnSaveAll").classList.toggle("hidden", !editMode);
    await doSearch();
  });

  el("btnSaveAll").addEventListener("click", async () => {
    try {
      const tbody = el("resultBody");
      const inputs = tbody.querySelectorAll("[data-edit-id]");

      const byId = {};
      inputs.forEach(inp => {
        const id = inp.getAttribute("data-edit-id");
        const field = inp.getAttribute("data-edit-field");
        if (!byId[id]) byId[id] = {};
        byId[id][field] = inp.value;
      });

      const ids = Object.keys(byId);
      for (const id of ids) {
        const p = byId[id];
        const payload = {
          update_date: p.update_date || "",
          work: p.work || "",
          table_name: p.table_name || "",
          owner: p.owner || "",
          note: p.note || "",
          p4_path: p.p4_path || "",
        };

        if (!payload.update_date || !payload.work || !payload.table_name || !payload.owner || !payload.p4_path) {
          throw new Error("필수값(일자/작업/테이블/담당자/P4경로) 누락된 행이 있어요.");
        }

        await updateRecord(id, payload);
      }

      showAlert("success", "저장 완료!");
      await doSearch();
    } catch (e) {
      showAlert("error", `저장 실패: ${e.message}`);
    }
  });

  function renderRows(rows) {
    const tbody = el("resultBody");
    tbody.innerHTML = "";
    el("resultCount").textContent = rows.length;

    if (!rows.length) {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td class="p-4 text-gray-500" colspan="6">조회 결과가 없습니다.</td>`;
      tbody.appendChild(tr);
      return;
    }

    rows.forEach(r => {
      const tr = document.createElement("tr");
      tr.className = "hover:bg-gray-50";

      const cell = (field, value, type = "text") => {
        if (!editMode) return escapeHtml(value ?? "");
        const v = (value ?? "");
        return `<input data-edit-id="${r.id}" data-edit-field="${field}" type="${type}"
                  class="w-full border rounded p-2" value="${escapeHtml(v)}" />`;
      };

      tr.innerHTML = `
        <td class="p-3 border-b whitespace-nowrap">${cell("update_date", r.update_date, "date")}</td>
        <td class="p-3 border-b">${cell("work", r.work)}</td>
        <td class="p-3 border-b whitespace-nowrap">${cell("table_name", r.table_name)}</td>
        <td class="p-3 border-b whitespace-nowrap">${cell("owner", r.owner)}</td>
        <td class="p-3 border-b font-mono text-xs break-all">${cell("p4_path", r.p4_path)}</td>
        <td class="p-3 border-b">${cell("note", r.note || "")}</td>
      `;
      tbody.appendChild(tr);
    });
  }

  async function doSearch() {
    try {
      hideAlert();

      const filters = {
        update_date: el("q_update_date").value || "",
        work: el("q_work").value.trim(),
        table_name: el("q_table_name").value || "",
        limit: 200,
        offset: 0,
      };

      const rows = await listRecords(filters);
      renderRows(rows);

    } catch (e) {
      showAlert("error", `조회 실패: ${e.message}`);
    }
  }

  el("btnSearch").addEventListener("click", doSearch);

  el("btnReset").addEventListener("click", async () => {
    el("q_update_date").value = "";
    el("q_work").value = "";
    el("q_table_name").value = "";
    await doSearch();
  });

  // ---------- init ----------
  (async function init() {
    showPage("register");
    el("r_update_date").value = new Date().toISOString().slice(0,10);

    await refreshTablesDropdown();
    await refreshHistory();
  })();
</script>
</body>
</html>
