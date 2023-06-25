import data from "/back-end/index.js";
const IconsCtn = document.getElementById("iconCtn");
const openIcon = document.getElementById("openBtn");
const closeIcon = document.getElementById("closeBtn");
const navBarCtn = document.getElementById("navLinksCtn");
const getProductsCtn = document.getElementById("productsCtn");

IconsCtn.addEventListener("click", () => {
  openIcon.classList.toggle("hide");
  closeIcon.classList.toggle("hide");
  navBarCtn.classList.toggle("own-nav-links-container");
});

function getRandomData(data) {
  const mobilesData = data.mobileData;
  const laptopData = data.laptopsData;
  const snekerData = data.snekersData;
  const shirtData = data.shirtsData;
  const tshirtData = data.tshirtsData;
  const pantData = data.pantsData;
  const watchData = data.watchesData;
  const camerData = data.camersData;

  return [
    mobilesData,
    laptopData,
    snekerData,
    shirtData,
    tshirtData,
    pantData,
    watchData,
    camerData,
  ];
}
let pass = getRandomData(data);
var len = pass.length;
var index = Math.floor(Math.random() * len);
var index_2 = Math.floor(Math.random() * pass[index].length);
var newData = pass[index][index_2];

const showWeb = (mob) => {
  let divEl = document.createElement("img");
  divEl.src = mob.img_url;
  getProductsCtn.appendChild(divEl);
};

showWeb(newData);
