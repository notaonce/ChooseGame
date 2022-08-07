
const $ = (selector) => document.querySelector(selector);


const body = $("body");
const modal = $(".modal-container");

const openModal = () => {
    modal.classList.add("open");
    body.style.overflow = "hidden"
};

const closeModal = () => {
    modal.classList.remove("open") ;
    body.style.overflow = "auto";
};

