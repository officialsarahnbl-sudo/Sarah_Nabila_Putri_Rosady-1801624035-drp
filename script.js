// =========================
// MOOD SYSTEM
// =========================
let currentMood = "😊";

window.setMood = function (mood) {

  currentMood = mood;

  document.getElementById("selectedMood")
    .innerText = "Mood: " + mood;

};

// =========================
// CHIBI
// =========================
document.addEventListener("DOMContentLoaded", function () {

  const chibi = document.getElementById("chibi");
  const bubble = document.getElementById("chibiBubble");

  const messages = [
    "Halooo 💖",
    "Semangat ya ✨",
    "Jangan sedih 🌸",
    "Aku temenin 📝",
    "Kamu hebat 😆"
  ];

  chibi.addEventListener("click", () => {

    const randomText =
      messages[Math.floor(Math.random() * messages.length)];

    bubble.innerText = randomText;

    bubble.style.display = "block";

    clearTimeout(window.bubbleTimer);

    window.bubbleTimer = setTimeout(() => {
      bubble.style.display = "none";
    }, 3000);

  });

});

// =========================
// NAVIGATION
// =========================
window.showPage = function (page) {

  const journalPage =
    document.getElementById("journalPage");

  const plannerPage =
    document.getElementById("plannerPage");

  const buttons =
    document.querySelectorAll(".nav button");

  buttons.forEach(btn =>
    btn.classList.remove("active")
  );

  if (page === "journal") {

    journalPage.style.display = "block";
    plannerPage.style.display = "none";

    buttons[0].classList.add("active");

  } else {

    journalPage.style.display = "none";
    plannerPage.style.display = "block";

    buttons[1].classList.add("active");

  }

};

// =========================
// JOURNAL
// =========================
window.addNote = function () {

  const noteInput =
    document.getElementById("note");

  const list =
    document.getElementById("list");

  const text =
    noteInput.value.trim();

  if (text === "") {

    alert("Isi jurnal dulu 💖");
    return;

  }

  // tanggal sekarang
  const today =
    new Date().toLocaleDateString("id-ID", {
      day: "numeric",
      month: "long",
      year: "numeric"
    });

  const li =
    document.createElement("li");

  li.innerHTML = `

    <div class="noteCard">

      <div class="noteTop">

        <span class="noteDate">
          🌸 ${today}
        </span>

        <button
          class="deleteBtn"
          onclick="
            this.parentElement.parentElement.parentElement.remove();
            saveData();
          "
        >
          Hapus
        </button>

      </div>

      <p class="noteMood">
        ${currentMood}
      </p>

      <p class="noteText">
        ${text}
      </p>

    </div>

  `;

  list.prepend(li);

  saveData();

  noteInput.value = "";

};

// =========================
// PLANNER
// =========================
window.addPlan = function () {

  const date =
    document.getElementById("planDate").value;

  const text =
    document.getElementById("planText")
    .value
    .trim();

  const planList =
    document.getElementById("planList");

  if (date === "" || text === "") {

    alert("Isi tanggal & rencana dulu 📅");
    return;

  }

  const li =
    document.createElement("li");

  li.innerHTML = `

    <div>

      <strong>${date}</strong>
      <br>

      ${text}

    </div>

    <button
      onclick="
        this.parentElement.remove();
        saveData();
      "
    >
      Hapus
    </button>

  `;

  planList.prepend(li);

  saveData();

  document.getElementById("planDate").value = "";
  document.getElementById("planText").value = "";

};

// =========================
// DARK MODE
// =========================
window.toggleTheme = function () {

  document.body.classList.toggle("dark");

};

// =========================
// SAVE DATA
// =========================
function saveData() {

  localStorage.setItem(
    "journalNotes",
    document.getElementById("list").innerHTML
  );

  localStorage.setItem(
    "plannerNotes",
    document.getElementById("planList").innerHTML
  );

}

// =========================
// LOAD DATA
// =========================
window.onload = function () {

  const journalData =
    localStorage.getItem("journalNotes");

  const plannerData =
    localStorage.getItem("plannerNotes");

  if (journalData) {

    document.getElementById("list").innerHTML =
      journalData;

  }

  if (plannerData) {

    document.getElementById("planList").innerHTML =
      plannerData;

  }

  // LOAD WALLPAPER
  const savedWallpaper =
    localStorage.getItem("customWallpaper");

  if (savedWallpaper) {

    document.body.style.backgroundImage =
      `url(${savedWallpaper})`;

    document.body.style.backgroundSize =
      "cover";

    document.body.style.backgroundPosition =
      "center";

  }

};

// =========================
// CUSTOM WALLPAPER
// =========================
document.addEventListener("DOMContentLoaded", function () {

  const wallpaperInput =
    document.getElementById("wallpaperInput");

  wallpaperInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) return;

    const reader = new FileReader();

    reader.onload = function (e) {

      const image =
        e.target.result;

      document.body.style.backgroundImage =
        `url(${image})`;

      document.body.style.backgroundSize =
        "cover";

      document.body.style.backgroundPosition =
        "center";

      localStorage.setItem(
        "customWallpaper",
        image
      );

    };

    reader.readAsDataURL(file);

  });

});