const btn = document.getElementById("btn");
const modal = document.getElementById("modal2");

btn ? console.log(btn) : console.log("nothing");
modal ? console.log(modal): console.log("no modal");

btn.addEventListener("click", () => {
  console.log("click!!");
  modal.style.display = "flex";
});