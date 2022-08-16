// Swiper JS
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 5,
    centeredSlides: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        dynamicBullets: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    allowTouchMove: false, /* 배너 드래그 조작 금지*/
});