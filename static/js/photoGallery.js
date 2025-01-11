document.addEventListener('DOMContentLoaded', function () {
  const carousels = document.querySelectorAll('.swiper');
  carousels.forEach(carousel => {
    new Swiper(carousel, {
      slidesPerView: 3,
      slidesPerGroup: 1,
      spaceBetween: 10,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets', // Options: 'bullets', 'fraction', 'progressbar'
        clickable: true,
        color: 'red',
      },
      loop: true,
      autoplay: {
        delay: 3000,
        disableOnInterface: false,
        pauseOnMouseEnter: true,
      },
    });
  });
});