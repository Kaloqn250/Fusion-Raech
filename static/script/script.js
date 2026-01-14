const panels = document.querySelectorAll(".panel");

panels.forEach((panel) => {
  panel.addEventListener("click", () => {
    removeActiveClasses();
    panel.classList.add("active");
  });
});

const removeActiveClasses = () => {
  panels.forEach((panel) => {
    panel.classList.remove("active");
  });
};
const elements = document.querySelectorAll('body *');
elements.forEach((el, index) => {

  setTimeout(() => {
    el.classList.add('show');
  }, index * 100);

});