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
}

function deleteNote(index) {
  notes.splice(index, 1);
  localStorage.setItem("notes", JSON.stringify(notes));
  renderNotes();
}

renderNotes();
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

  const newPlan = {
    date: date,
    text: text
  };

  plans.push(newPlan);
  localStorage.setItem("plans", JSON.stringify(plans));

  document.getElementById("planDate").value = "";
  document.getElementById("planText").value = "";

  renderPlans();
}

function deletePlan(index) {
  plans.splice(index, 1);
  localStorage.setItem("plans", JSON.stringify(plans));
  renderPlans();
}

renderPlans();