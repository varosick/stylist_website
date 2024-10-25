$(document).ready(function() {
	$('.open-modal-js').magnificPopup({
		type: 'inline',
		fixedContentPos: true,
		fixedBgPos: true,
		overflowY: 'auto',
		closeBtnInside: false,
		preloader: false,
		midClick: true,
		removalDelay: 200,
		mainClass: 'my-mfp-zoom-in',
	});
});

document.addEventListener('DOMContentLoaded', function () {
    let currentSlide = 0;
    const carousel_slides = document.querySelectorAll('.carousel_slide');
    const totalSlides = carousel_slides.length;

    function showSlide(index) {
        carousel_slides.forEach((slide) => {
            slide.classList.remove('active');
            slide.style.opacity = 0; // Сбрасываем opacity
        });

        carousel_slides[index].classList.add('active');
        carousel_slides[index].style.opacity = 1; // Устанавливаем opacity для активного
    }

    document.querySelector('.carousel_next').addEventListener('click', function () {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    });

    document.querySelector('.carousel_prev').addEventListener('click', function () {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
    });
	document.querySelector('.carousel_next').addEventListener('touchstart', function () {
    	currentSlide = (currentSlide + 1) % totalSlides;
    	showSlide(currentSlide);
	});

	document.querySelector('.carousel_prev').addEventListener('touchstart', function () {
    	currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    	showSlide(currentSlide);
	});


    // Показ первого слайда при загрузке
    showSlide(currentSlide);
});