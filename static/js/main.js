
//Making the side navigation collapsible
let wholePage = document.getElementById("page_wrapper");
let btn = document.getElementById("nav_collapse_btn");

btn.addEventListener("click", collapse);

function collapse() {
  wholePage.classList.toggle("collapsed");
  if (wholePage.classList.contains("collapsed")) {
    btn.innerHTML = "<i class='bx bxs-chevrons-right'></i>";
  } else {
    btn.innerHTML = "<i class='bx bxs-chevrons-left'></i>";
  }
}

//Creating the dark/light mode toggle

let darkMode = localStorage.getItem("dark_mode");
var toggleBtn = document.querySelector("#theme_switch");

const enableDarkMode = () => {
  document.body.classList.add("dark_mode");
  localStorage.setItem("darkMode", "enabled");
  console.log("enabled");
};

const disableDarkMode = () => {
  document.body.classList.remove("dark_mode");
  localStorage.setItem("darkMode", null);
  console.log("null");
};

toggleBtn.addEventListener("click", () => {
  darkMode = localStorage.getItem("darkMode");

  if (darkMode !== "enabled") {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});