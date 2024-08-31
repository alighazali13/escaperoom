var swiper = new Swiper(".main-slider", {
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
      delay: 5000,
    },
  });

  var swiper = new Swiper(".cat-slider", {
    slidesPerView: 2,
    spaceBetween: 20,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 6,
          spaceBetween: 15,
        },
      },
  });


  var swiper = new Swiper(".off-product", {
    slidesPerView: 1.4,
    spaceBetween: 15,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".cinema-product", {
    slidesPerView: 1.4,
    spaceBetween: 15,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 4.1,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".slider-product1", {
    slidesPerView: 1.4,
    spaceBetween: 15,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".slider-product2", {
    slidesPerView: 1,
    spaceBetween: 10,
    autoplay: {
      delay: 3000,
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
    },
    
  });

  var swiper = new Swiper(".slider-product3", {
    slidesPerView: 2.4,
    spaceBetween: 10,
    autoplay: {
      delay: 5000,
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 4,
        spaceBetween: 15,
      },
    },
    
  });

  var swiper = new Swiper(".partners", {
    slidesPerView: 3,
    spaceBetween: 10,
    breakpoints: {
      640: {
        slidesPerView: 4,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 5,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 6,
        spaceBetween: 50,
      },
    },
    
  });


  var swiper = new Swiper(".gall-pro", {
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper(".pro-main", {
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: swiper,
    },
  });


  function decrement(e) {
    const btn = e.target.parentNode.parentElement.querySelector(
      'button[data-action="decrement"]'
    );
    const target = btn.nextElementSibling;
    let value = Number(target.value);
    value--;
    target.value = value;
  }


  var swiper = new Swiper(".related", {
    slidesPerView: 1.4,
    spaceBetween: 15,
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 4,
        spaceBetween: 15,
      },
    },
    
  });

  var swiper = new Swiper(".about-slider", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
    },
  });

  if (document.getElementById('dtl').value) {
    count_down_two_days_later();
  }
  



function count_down_two_days_later() {
  var duration = document.getElementById('dtl').value;
  console.log(duration);
  var timer = duration, hours, minutes, seconds;
  setInterval(() => {
    hours = Math.floor(timer / 3600);
    minutes = Math.floor((timer % 3600) / 60);
    seconds = Math.floor(timer % 60);

    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    document.getElementById('counterhours').style.setProperty('--value', hours);
    document.getElementById('counterminutes').style.setProperty('--value', minutes);
    document.getElementById('counterseconds').style.setProperty('--value', seconds);

    if (--timer < 0) {
      timer = duration;
      console.log("Countdown finished!");
    }
  }, 1000);
}


