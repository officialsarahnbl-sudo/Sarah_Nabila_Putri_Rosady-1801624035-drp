let notes = JSON.parse(localStorage.getItem("notes")) || [];

function getCurrentDate() {
  const today = new Date();
  return today.toLocaleDateString("id-ID", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric"
  });
}

function renderNotes() {
  const list = document.getElementById("list");
  list.innerHTML = "";

  notes.forEach((note, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <div>
        <strong>${note.date}</strong><br>
        ${note.text}
      </div>
      <button onclick="deleteNote(${index})">Hapus</button>
    `;
    list.appendChild(li);
  });
}

function addNote() {
  const noteInput = document.getElementById("note").value;
  if (noteInput.trim() === "") return;

  const newNote = {
    text: noteInput,
    date: getCurrentDate()
  };

  notes.push(newNote);
  localStorage.setItem("notes", JSON.stringify(notes));

  document.getElementById("note").value = "";
  renderNotes();

  chibiSpeak("Yeay! Catatan berhasil disimpan 💖");
}

function deleteNote(index) {
  notes.splice(index, 1);
  localStorage.setItem("notes", JSON.stringify(notes));
  renderNotes();

  chibiSpeak("Catatan dihapus 😢");
}

let plans = JSON.parse(localStorage.getItem("plans")) || [];

function renderPlans() {
  const list = document.getElementById("planList");
  list.innerHTML = "";

  plans.forEach((plan, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <div>
        <strong>${plan.date}</strong><br>
        ${plan.text}
      </div>
      <button onclick="deletePlan(${index})">Hapus</button>
    `;
    list.appendChild(li);
  });
}

function addPlan() {
  const date = document.getElementById("planDate").value;
  const text = document.getElementById("planText").value;

  if (date === "" || text.trim() === "") return;

  const newPlan = { date, text };
  plans.push(newPlan);
  localStorage.setItem("plans", JSON.stringify(plans));

  document.getElementById("planDate").value = "";
  document.getElementById("planText").value = "";

  renderPlans();

  chibiSpeak("Rencana berhasil ditambahkan! ✨");
}

function deletePlan(index) {
  plans.splice(index, 1);
  localStorage.setItem("plans", JSON.stringify(plans));
  renderPlans();

  chibiSpeak("Rencana dihapus 😢");
}

function showPage(page) {
  const journal = document.getElementById("journalPage");
  const planner = document.getElementById("plannerPage");
  const buttons = document.querySelectorAll(".nav button");

  buttons.forEach(btn => btn.classList.remove("active"));

  if (page === "journal") {
    journal.style.display = "block";
    planner.style.display = "none";
    buttons[0].classList.add("active");
    chibiSpeak("Ayo tulis jurnalmu 💖");
  } else {
    journal.style.display = "none";
    planner.style.display = "block";
    buttons[1].classList.add("active");
    chibiSpeak("Siapkan rencana hari ini! 📅");
  }
}

// --- Fungsi chibi ngomong ---
function chibiSpeak(text) {
  const bubble = document.getElementById("chibiBubble");
  if (!bubble) return;

  bubble.innerText = text;
  bubble.style.display = "block";

  const chibi = document.getElementById("chibi");
  const rect = chibi.getBoundingClientRect();
  bubble.style.left = rect.left + "px";
  bubble.style.top = (rect.top - 50 + window.scrollY) + "px";

  setTimeout(() => {
    bubble.style.display = "none";
  }, 3000);
}

// --- Inisialisasi halaman ---
window.onload = function () {
  renderNotes();
  renderPlans();
  showPage("journal");

  const chibi = document.getElementById("chibi");
  if (chibi) {
    const messages = [
      "Semangat yaa! 💕",
      "Jangan lupa istirahat 😚",
      "Kamu keren banget hari ini! ✨",
      "Ayo tulis jurnalmu 💖"
    ];

    chibi.addEventListener("click", () => {
      const random = messages[Math.floor(Math.random() * messages.length)];
      chibiSpeak(random);
    });
  }
};