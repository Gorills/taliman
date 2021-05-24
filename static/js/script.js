$('.slider').slick({
  infinite: true,
  autoplay: true,
  speed: 300,
  slidesToShow: 1,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>"
});
$('.about-clients__feedback').slick({
  infinite: true,
  autoplay: true,
  speed: 300,
  slidesToShow: 1,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>"
});
$('.category__slider').slick({
  autoplay: true,
  dots: false,
  infinite: true,
  arrows: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>",
  responsive: [{
    breakpoint: 1024,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 3,
      infinite: true
    }
  }, {
    breakpoint: 600,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 2
    }
  }, {
    breakpoint: 480,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.portfolio__slider').slick({
  autoplay: true,
  dots: false,
  infinite: true,
  arrows: true,
  speed: 300,
  slidesToShow: 3,
  slidesToScroll: 3,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>",
  responsive: [{
    breakpoint: 1024,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 3,
      infinite: true
    }
  }, {
    breakpoint: 600,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 2
    }
  }, {
    breakpoint: 480,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.portfolio-detail__slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.portfolio-detail__nav'
});
$('.portfolio-detail__nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.portfolio-detail__slider',
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>",
  centerMode: true,
  focusOnSelect: true
});
$('.serv_detail__slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.serv_detail__nav'
});
$('.serv_detail__nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.serv_detail__slider',
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>",
  centerMode: true,
  focusOnSelect: true
});
$('.serv_detail__slider').magnificPopup({
  delegate: 'a',
  // child items selector, by clicking on it popup will open
  type: 'image',
  gallery: {
    enabled: true,
    // set to true to enable gallery
    preload: [0, 2],
    // read about this option in next Lazy-loading section
    navigateByImgClick: true,
    arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
    // markup of an arrow button
    tPrev: 'Previous (Left arrow key)',
    // title for left button
    tNext: 'Next (Right arrow key)',
    // title for right button
    tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter

  }
});
$('.portfolio-detail__slider').magnificPopup({
  delegate: 'a',
  // child items selector, by clicking on it popup will open
  type: 'image',
  gallery: {
    enabled: true,
    // set to true to enable gallery
    preload: [0, 2],
    // read about this option in next Lazy-loading section
    navigateByImgClick: true,
    arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
    // markup of an arrow button
    tPrev: 'Previous (Left arrow key)',
    // title for left button
    tNext: 'Next (Right arrow key)',
    // title for right button
    tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter

  }
});

function windowSize() {
  if ($(window).width() >= '992') {
    $('.header__item-drop').hover(function (e) {
      e.preventDefault();
      $('.header__dropdown').addClass('header__dropdown--active');
    });
    $('.close').hover(function () {
      $('.header__dropdown').removeClass('header__dropdown--active');
    });
    $('.header__dropdown').mouseleave(function () {
      $(this).removeClass('header__dropdown--active');
    });
  } else {
    $('.header__item-drop').click(function (e) {
      e.preventDefault();
      $('.header__dropdown').toggleClass('header__dropdown--active');
    });
  }
}

$(window).on('load resize', windowSize);
$('.show-popup').click(function (e) {
  e.preventDefault();
  $('.popup').addClass('popup--active');
  $('.popup__closer').addClass('popup__closer--active');
});
$('.popup__closer, .popup__icon').click(function (e) {
  e.preventDefault();
  $('.popup').removeClass('popup--active');
  $('.popup__closer').removeClass('popup__closer--active');
});
$('.header__bottom-menu-link').click(function (e) {
  e.preventDefault();
  $('.header__nav').addClass('header__nav--active');
  $('.nav-closer').addClass('nav-closer--active');
});
$('.nav-closer').click(function (e) {
  e.preventDefault();
  $('.header__nav').removeClass('header__nav--active');
  $('.nav-closer').removeClass('nav-closer--active');
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__link"), function () {
    if (this.href == url) {
      $(this).addClass('header__link--active');
    }
  });
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__drop-link"), function () {
    if (this.href == url) {
      $(this).addClass('header__drop-link--active');
      $('.header__item-drop').addClass('header__link--active');
    }
  });
});
$(window).scroll(function () {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/

  if (height > 125) {
    $('.header').addClass('header--fixed');
    $('.margintop').addClass('margintop--active');
  } else {
    /*Если меньше 100px удаляем класс для header*/
    $('.header').removeClass('header--fixed');
    $('.margintop').removeClass('margintop--active');
  }
});