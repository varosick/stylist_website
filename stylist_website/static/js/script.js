//Модальное окно обратного звонка
//Все страницы
// if (document.querySelector('#button-callback')){
//     let buttonCallback = document.querySelectorAll('#button-callback');
//     let ModalCallback = document.querySelector('.modal-callback');
//     let ModalCallbackBlock = document.querySelector('.modal-callback-block');
//     let ModalCallbackBlockThanks = document.querySelector('.modal-callback-thanks');
//     let buttonModalCallbackClose = document.querySelector('.modal-callback__close');
//     // let buttonModalCallbackOpenThanks = document.querySelector('.modal-callback__button_open-thanks');

//     for (var i = 0; i < buttonCallback.length; i++){
//         buttonCallback[i].addEventListener('click', function () {
//             ModalCallback.classList.add("active");
//             ModalCallbackBlock.classList.add("active");
//         });
//         buttonModalCallbackClose.addEventListener('click', function () {
//             ModalCallback.classList.remove("active");
//             ModalCallbackBlockThanks.classList.remove("active");
//         });
//         // buttonModalCallbackOpenThanks.addEventListener('click', function () {
//         //     ModalCallbackBlock.classList.remove("active");
//         //     ModalCallbackBlockThanks.classList.add("active");
//         // });
//     }
// }


//Модальное окно мобильного меню
//Все страницы
if (document.querySelector('#button-header')){
    let buttonHeader = document.querySelectorAll('#button-header');
    let ModalHeader = document.querySelector('.modal-menu');
    let buttonModalHeaderClose = document.querySelector('.modal-menu__close');

    let linksDesktopMenu = document.querySelector('.header-menu');
    let linksModalMenu = document.querySelector('.modal-menu__links');
    linksModalMenu.insertAdjacentHTML('afterbegin', linksDesktopMenu.innerHTML);


    for (var i = 0; i < buttonHeader.length; i++){
        buttonHeader[i].addEventListener('click', function () {
            ModalHeader.classList.add("active");
        });
        buttonModalHeaderClose.addEventListener('click', function () {
            ModalHeader.classList.remove("active");
        });
    }
}

//Запуск видео на весь экран
//Страница: Главная, О школе
if (document.querySelector('#button-video')){
    let buttonVideo = document.querySelectorAll('#button-video');
    let BlockContentVideo = document.querySelector('.video-full-play');
    let BlockVideo = document.querySelector('.video-full__video');

    for (var i = 0; i < buttonVideo.length; i++){
        BlockVideo.controls = false;
        buttonVideo[i].addEventListener('click', function () {
            BlockContentVideo.classList.add("no-active");
            BlockVideo.style.filter = null;
            BlockVideo.play();
            BlockVideo.controls = true;
        });
    }
}

//Запуск свертывания блока курсы
//Страница: Главная, Курсы, Страница Курса, ЛК все курсы
// if (document.querySelector('.courses-block-container')){
//     let buttonСourseAll = document.querySelector('#button-course-all');
//     let buttonСourseMasterClass = document.querySelector('#button-course-master-class');
//     let buttonСoursePro = document.querySelector('#button-course-pro');
//     let buttonСourseBaza = document.querySelector('#button-course-baza');

//     let СourseMasterClass = document.querySelectorAll('#course-master-class');
//     let СoursePro = document.querySelectorAll('#course-pro');
//     let СourseBaza = document.querySelectorAll('#course-baza');

//     let buttonСoursesShow = document.querySelector('#button-courses-show');
//     const СourseLengthMax = 3; //количество вывода курсов при нажатии на "показать еще"

//     buttonСourseAll.addEventListener('click', function () {
//         buttonСourseAll.classList.add('active');
//         buttonСourseMasterClass.classList.remove('active');
//         buttonСoursePro.classList.remove('active');
//         buttonСourseBaza.classList.remove('active');

//         for (var i = 0; i < СourseMasterClass.length; i++){
//             СourseMasterClass[i].classList.add('active');
//         }
//         for (var i = 0; i < СoursePro.length; i++){
//             СoursePro[i].classList.add('active');
//         }
//         for (var i = 0; i < СourseBaza.length; i++){
//             СourseBaza[i].classList.add('active');
//         }
//         СoursesShow();
//     });

//     buttonСourseMasterClass.addEventListener('click', function () {
//         buttonСourseAll.classList.remove('active');
//         buttonСourseMasterClass.classList.add('active');
//         buttonСoursePro.classList.remove('active');
//         buttonСourseBaza.classList.remove('active');

//         for (var i = 0; i < СourseMasterClass.length; i++){
//             СourseMasterClass[i].classList.add('active');
//         }
//         for (var i = 0; i < СoursePro.length; i++){
//             СoursePro[i].classList.remove('active');
//         }
//         for (var i = 0; i < СourseBaza.length; i++){
//             СourseBaza[i].classList.remove('active');
//         }
//         СoursesShow();
//     });

//     buttonСoursePro.addEventListener('click', function () {
//         buttonСourseAll.classList.remove('active');
//         buttonСourseMasterClass.classList.remove('active');
//         buttonСoursePro.classList.add('active');
//         buttonСourseBaza.classList.remove('active');

//         for (var i = 0; i < СourseMasterClass.length; i++){
//             СourseMasterClass[i].classList.remove('active');
//         }
//         for (var i = 0; i < СoursePro.length; i++){
//             СoursePro[i].classList.add('active');
//         }
//         for (var i = 0; i < СourseBaza.length; i++){
//             СourseBaza[i].classList.remove('active');
//         }
//         СoursesShow();
//     });

//     buttonСourseBaza.addEventListener('click', function () {
//         buttonСourseAll.classList.remove('active');
//         buttonСourseMasterClass.classList.remove('active');
//         buttonСoursePro.classList.remove('active');
//         buttonСourseBaza.classList.add('active');

//         for (var i = 0; i < СourseMasterClass.length; i++){
//             СourseMasterClass[i].classList.remove('active');
//         }
//         for (var i = 0; i < СoursePro.length; i++){
//             СoursePro[i].classList.remove('active');
//         }
//         for (var i = 0; i < СourseBaza.length; i++){
//             СourseBaza[i].classList.add('active');
//         }
//         СoursesShow();
//     });

//     //кнопка показать еще
//     buttonСoursesShow.addEventListener('click', function() {
//         let СourseActiveShowFalseAll = document.querySelectorAll('.courses-block-container.show-false');
        
//         if (СourseActiveShowFalseAll.length <= СourseLengthMax){
//             buttonСoursesShow.style.display = 'none'}
//         else {
//             buttonСoursesShow.style.display = 'block'}

//         for (var i = 0; i < СourseLengthMax; i++) {
//             if (document.querySelector('.show-false')) {
//                 СourseActiveShowFalseAll[i].classList.remove('show-false');
//                 СourseActiveShowFalseAll[i].classList.add('show-true');
//             } 
//         }
//     })

//     function СoursesShow() {
//         let СourseAll = document.querySelectorAll('.courses-block-container');
//         let СourseActiveAll = document.querySelectorAll('.courses-block-container.active');
//         let buttonСoursesShow = document.querySelector('#button-courses-show');
//         const СourseLengthMax = 3; //количество вывода курсов при нажатии на "показать еще"

//         //очищаем показ блоков
//         for (var i = 0; i < СourseAll.length; i++) {
//             if (document.querySelector('.show-true')) {СourseAll[i].classList.remove('show-true');} 
//             else if (document.querySelector('.show-false')) {СourseAll[i].classList.remove('show-false');}
//         }

//         //показываем первые три блока
//         for (var i = 0; i < СourseActiveAll.length; i++) {
//             if (СourseActiveAll.length >= СourseLengthMax){
//                 СourseActiveAll[i].classList.add('show-false');
//                 for (var j = 0; j < СourseLengthMax; j++) {
//                     СourseActiveAll[j].classList.remove('show-false');
//                     СourseActiveAll[j].classList.add('show-true');
//                 }
//                 buttonСoursesShow.style.display = 'block'
//             } else {
//                 СourseActiveAll[i].classList.add('show-true');
//                 buttonСoursesShow.style.display = 'none'}
//         }
//     }
// }

//Запуск свертывания блока FAQ
//Страница: Главная, О школе, Курсы, Страница Курса
if (document.querySelector('.faq-block')){
    let FaqBlock = document.querySelectorAll('.faq-block');
    let buttonFaq = document.querySelectorAll('#button-faq');

    for (var i = 0; i < FaqBlock.length; i++){
        buttonFaq[i].addEventListener('click', function () {
            for (var j = 0; j < FaqBlock.length; j++){
                FaqBlock[j].classList.remove('active');
            };
            this.parentNode.classList.add('active');
        });
    }
}

//Изменение футера в зависимости от разрешения
//Все страницы
/*
if (document.querySelector('.footer-flex-planshet')){
    document.querySelector('.footer-flex-planshet-top').insertAdjacentHTML('beforeEnd', document.querySelector('#insert-footer__logo').outerHTML);
    document.querySelector('.footer-flex-planshet-top').insertAdjacentHTML('beforeEnd', document.querySelector('#insert-footer-social').outerHTML);
    document.querySelector('.footer-flex-planshet-top').insertAdjacentHTML('afterEnd', document.querySelector('#insert-footer__links').outerHTML);
    document.querySelector('.footer-flex-planshet-bottom-left').insertAdjacentHTML('beforeEnd', document.querySelector('#insert-footer__copyright1').outerHTML);
    document.querySelector('.footer-flex-planshet-bottom-left').insertAdjacentHTML('beforeEnd', document.querySelector('#insert-footer__copyright2').outerHTML);
    document.querySelector('.footer-flex-planshet-bottom-right').insertAdjacentHTML('beforeEnd', document.querySelector('#insert-politics').outerHTML);
}*/

//Скролл из футера, стрелка вверх
//Все страницы
if (document.querySelector('.footer__button-up')){
    let buttonFooterTop = document.querySelector('.footer__button-up');

    buttonFooterTop.addEventListener('click', function() {
        ScrollTop();
    });

    function ScrollTop() {
        let top = Math.max(document.body.scrollTop,document.documentElement.scrollTop);
        if(top > 0) {
            window.scrollBy(0,-100);
            buttonFooterTop = setTimeout('ScrollTop()',5);
        } else clearTimeout(buttonFooterTop);
        return false;
    }
}

//Скролл карты в планшетной и мобильной версии
//Страница: Главная
if (document.querySelector('.georgaphy__inner')){
    let Georgaphy = document.querySelector('.georgaphy__inner');
    let GeorgaphyRange = document.querySelector('#georgaphy-scroll__range');

    GeorgaphyRange.max = Georgaphy.scrollWidth-Georgaphy.offsetWidth;

    GeorgaphyRange.addEventListener('input', function() {
        Georgaphy.scrollLeft = GeorgaphyRange.value
    });
}

$(document).ready(function() {
    $('.georgaphy__inner').on('scroll', function() {
        console.log($(this).scrollLeft());
        $('#georgaphy-scroll__range').val($(this).scrollLeft());
    });
});


//Параллакс изображений в блоке "мы лучшие"
//Страница: О школе
if (document.querySelector('.we-best')){
    let WeBestOffsetTop = document.querySelector('.we-best').offsetTop;
    let WeBestOffsetHeight = document.querySelector('.we-best').offsetHeight;
    let WeBestTop = WeBestOffsetTop-(WeBestOffsetHeight/2);
    // let imgWeBestOne = document.querySelector('.we-best__img-one');
    let imgWeBestTwo = document.querySelector('.we-best__img-two');
    let imgWeBestThree = document.querySelector('.we-best__img-three');
    let imgWeBestFour = document.querySelector('.we-best__img-four');

    window.addEventListener('scroll', function () {
        if (window.pageYOffset >= WeBestTop) {
            imgScrollY = window.pageYOffset-WeBestTop;
            //console.log(scrollY);
            // imgWeBestOne.style.transform = 'translateY(' + (-imgScrollY/3) +'px)';
            imgWeBestTwo.style.transform = 'translateY(' + (-imgScrollY/3) +'px)';
            imgWeBestThree.style.transform = 'translateY(' + (-imgScrollY/3 - 80) +'px)';
            imgWeBestFour.style.transform = 'translateY(' + (-imgScrollY/3 - 80) +'px)';
        }
    });
}

//Модальное окно "купить"
//Страница: страница курса
// if (document.querySelector('#button-buy')){
//     let buttonBuy = document.querySelectorAll('#button-buy');
//     let ModalBuy = document.querySelector('.modal-buy');
//     let buttonModalBuyClose = document.querySelector('.modal-buy__close');

//     let BuyFirstName = document.querySelector('#courses-first-name');
//     let BuyFirstPrice = document.querySelector('#courses-first-price');

//     let ModalBuyTitle = document.querySelector('#modal-buy__title_span');
//     let ModalBuyPrice = document.querySelector('#modal-buy__price');
//     ModalBuyTitle.innerHTML = BuyFirstName.innerHTML;
//     ModalBuyPrice.innerHTML = BuyFirstPrice.innerHTML;

//     for (var i = 0; i < buttonBuy.length; i++){
//         buttonBuy[i].addEventListener('click', function () {
//             ModalBuy.classList.add("active");
//         });
//         buttonModalBuyClose.addEventListener('click', function () {
//             ModalBuy.classList.remove("active");
//         });
//     }
// }

//Запуск свертывания карточек блога
//Страница: Блог
if (document.querySelector('.blog-container')){

    let buttonBlogShow = document.querySelector('#button-blog-show');
    let BlogAll = document.querySelectorAll('.blog-container');
    const BlogLengthMax = 3; //количество вывода статей при нажатии на "показать еще"

    //кнопка показать еще
    buttonBlogShow.addEventListener('click', function() {
        let BlogActiveShowFalseAll = document.querySelectorAll('.blog-container.show-false');
        
        if (BlogActiveShowFalseAll.length <= BlogLengthMax){
            buttonBlogShow.style.display = 'none'}
        else {
            buttonBlogShow.style.display = 'block'}

        for (var i = 0; i < BlogLengthMax; i++) {
            if (document.querySelector('.show-false')) {
                BlogActiveShowFalseAll[i].classList.remove('show-false');
                BlogActiveShowFalseAll[i].classList.add('show-true');
            } 
        }
    })

    //показываем первые три блока
    for (var i = 0; i < BlogAll.length; i++) {
        if (BlogAll.length >= BlogLengthMax){
            BlogAll[i].classList.add('show-false');
            for (var j = 0; j < BlogLengthMax; j++) {
                BlogAll[j].classList.remove('show-false');
                BlogAll[j].classList.add('show-true');
            }
            buttonBlogShow.style.display = 'block'
        } else {
            BlogAll[i].classList.add('show-true');
            buttonBlogShow.style.display = 'none'}
    }
}

//Запуск видео на весь экран
//Страница: Страница статьи
if (document.querySelector('#content-blog_button-video')){
    let buttonBlogVideo = document.querySelectorAll('#content-blog_button-video');
    let BlogBlockContentVideo = document.querySelector('.content-blog__video_play');
    let BlogBlockVideo = document.querySelector('.content-blog__video-full__video');

    for (var i = 0; i < buttonBlogVideo.length; i++){
        BlogBlockVideo.controls = false;
        buttonBlogVideo[i].addEventListener('click', function () {
            BlogBlockContentVideo.classList.add("no-active");
            BlogBlockVideo.play();
            BlogBlockVideo.controls = true;
        });
    }
}

//Открытие контента
//Страница: Отзывы
if (document.querySelector('.reviews-container')){
    let ReviewsContainer = document.querySelectorAll('.reviews-container-right');
    let buttonReviewsShow = document.querySelectorAll('#button-reviews-container-show-all');

    for (var i = 0; i < ReviewsContainer.length; i++){
        buttonReviewsShow[i].addEventListener('click', function () {
            this.parentNode.classList.toggle('full-open');
        });
    }
}

//Запуск видео
//Страница: Отзывы
if (document.querySelector('#reviews-container_button-video')){
    let buttonReviewsVideo = document.querySelectorAll('#reviews-container_button-video');
    let ReviewsBlockContentVideo = document.querySelectorAll('.reviews-container-right__video_play');
    let ReviewsBlockVideo = document.querySelectorAll('.reviews-container-right__video-full__video');
    let ReviewsVideo = document.querySelectorAll('.reviews-container-right__video');

    for (let i = 0; i < ReviewsVideo.length; i++){
        ReviewsBlockVideo[i].controls = false;
        buttonReviewsVideo[i].addEventListener('click', function () {
            for (let j = 0; j < ReviewsVideo.length; j++){
                ReviewsBlockContentVideo[j].classList.remove('no-active');
                ReviewsBlockVideo[j].pause();
            };
            ReviewsBlockContentVideo[i].classList.add("no-active");
            ReviewsBlockVideo[i].play();
            ReviewsBlockVideo[i].controls = true;
        });
    }
}

//Запуск свертывания карточек отзывов
//Страница: Отзывы
if (document.querySelector('.reviews-container')){

    let buttonReviewsShow = document.querySelector('#button-reviews-show');
    let ReviewsAll = document.querySelectorAll('.reviews-container');
    const ReviewsLengthMax = 3; //количество вывода статей при нажатии на "показать еще"

    //кнопка показать еще
    buttonReviewsShow.addEventListener('click', function() {
        let ReviewsActiveShowFalseAll = document.querySelectorAll('.reviews-container.show-false');
        
        if (ReviewsActiveShowFalseAll.length <= ReviewsLengthMax){
            buttonReviewsShow.style.display = 'none'}
        else {
            buttonReviewsShow.style.display = 'block'}

        for (var i = 0; i < ReviewsLengthMax; i++) {
            if (document.querySelector('.show-false')) {
                ReviewsActiveShowFalseAll[i].classList.remove('show-false');
                ReviewsActiveShowFalseAll[i].classList.add('show-true');
            } 
        }
    })

    //показываем первые три блока
    for (var i = 0; i < ReviewsAll.length; i++) {
        if (ReviewsAll.length >= ReviewsLengthMax){
            ReviewsAll[i].classList.add('show-false');
            for (var j = 0; j < ReviewsLengthMax; j++) {
                ReviewsAll[j].classList.remove('show-false');
                ReviewsAll[j].classList.add('show-true');
            }
            buttonReviewsShow.style.display = 'block'
        } else {
            ReviewsAll[i].classList.add('show-true');
            buttonReviewsShow.style.display = 'none'}
    }
}

//Запуск слайдера
//Страница: Отзывы
if (document.querySelector('.reviews-container-right__slider')){
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 30,
        loop: false,
        pagination: {
        clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
}

//Запуск свертывания курсов в личном кабинете
//Страница: ЛК мои курсы
if (document.documentElement.clientWidth < 768) {
    if (document.querySelector('.my-courses-container')){

        let buttonMyCoursesShow = document.querySelector('#button-my-courses-show');
        let MyCoursesAll = document.querySelectorAll('.my-courses-container');
        const MyCoursesLengthMax = 3; //количество вывода статей при нажатии на "показать еще"
    
        //кнопка показать еще
        buttonMyCoursesShow.addEventListener('click', function() {
            let MyCoursesActiveShowFalseAll = document.querySelectorAll('.my-courses-container.show-false');
            
            if (MyCoursesActiveShowFalseAll.length <= MyCoursesLengthMax){
                buttonMyCoursesShow.style.display = 'none'}
            else {
                buttonMyCoursesShow.style.display = 'block'}
    
            for (var i = 0; i < MyCoursesLengthMax; i++) {
                if (document.querySelector('.show-false')) {
                    MyCoursesActiveShowFalseAll[i].classList.remove('show-false');
                    MyCoursesActiveShowFalseAll[i].classList.add('show-true');
                } 
            }
        })
    
        //показываем первые три блока
        for (var i = 0; i < MyCoursesAll.length; i++) {
            if (MyCoursesAll.length >= MyCoursesLengthMax){
                MyCoursesAll[i].classList.add('show-false');
                for (var j = 0; j < MyCoursesLengthMax; j++) {
                    MyCoursesAll[j].classList.remove('show-false');
                    MyCoursesAll[j].classList.add('show-true');
                }
                buttonMyCoursesShow.style.display = 'block'
            } else {
                MyCoursesAll[i].classList.add('show-true');
                buttonMyCoursesShow.style.display = 'none'}
        }
    }
}
if (document.documentElement.clientWidth > 768) {
    if (document.querySelector('.my-courses-container')){

        let buttonMyCoursesShow = document.querySelector('#button-my-courses-show');
        let MyCoursesAll = document.querySelectorAll('.my-courses-container');
        const MyCoursesLengthMax = 6; //количество вывода статей при нажатии на "показать еще"
    
        //кнопка показать еще
        buttonMyCoursesShow.addEventListener('click', function() {
            let MyCoursesActiveShowFalseAll = document.querySelectorAll('.my-courses-container.show-false');
            
            if (MyCoursesActiveShowFalseAll.length <= MyCoursesLengthMax){
                buttonMyCoursesShow.style.display = 'none'}
            else {
                buttonMyCoursesShow.style.display = 'block'}
    
            for (var i = 0; i < MyCoursesLengthMax; i++) {
                if (document.querySelector('.show-false')) {
                    MyCoursesActiveShowFalseAll[i].classList.remove('show-false');
                    MyCoursesActiveShowFalseAll[i].classList.add('show-true');
                } 
            }
        })
    
        //показываем первые шесть блоков
        for (var i = 0; i < MyCoursesAll.length; i++) {
            if (MyCoursesAll.length >= MyCoursesLengthMax){
                MyCoursesAll[i].classList.add('show-false');
                for (var j = 0; j < MyCoursesLengthMax; j++) {
                    MyCoursesAll[j].classList.remove('show-false');
                    MyCoursesAll[j].classList.add('show-true');
                }
                buttonMyCoursesShow.style.display = 'block'
            } else {
                MyCoursesAll[i].classList.add('show-true');
                buttonMyCoursesShow.style.display = 'none'}
        }
    }
}


//Изменение активных блоков в ЛК курсы
//Страница: ЛК курсы
/*
if (document.querySelector('#header-courses__my-courses')){
    let buttonMyCourses = document.querySelector('#header-courses__my-courses');
    let buttonAllCourses = document.querySelector('#header-courses__all-courses');
    let BlockMyCourses = document.querySelector('.my-courses');
    let BlockAllCourses = document.querySelector('.courses');

        buttonMyCourses.addEventListener('click', function () {
            this.classList.remove("no-active");
            buttonAllCourses.classList.add("no-active");
            BlockAllCourses.classList.add("no-active");
            BlockMyCourses.classList.remove("no-active");
        });

        buttonAllCourses.addEventListener('click', function () {
            this.classList.remove("no-active");
            buttonMyCourses.classList.add("no-active");
            BlockAllCourses.classList.remove("no-active");
            BlockMyCourses.classList.add("no-active");
        });
}
*/

//Запуск видео
//Страница: ЛК видео
// if (document.querySelector('#lk-video-content__video__play__button')){
//     let buttonLkVideoVideo = document.querySelectorAll('#lk-video-content__video__play__button');
//     let LkVideoBlockContentVideo = document.querySelectorAll('.lk-video-content__video__play');
//     let LkVideoBlockVideo = document.querySelectorAll('.lk-video-content__video__play__video');
//     let LkVideoVideo = document.querySelectorAll('.lk-video-content__video');

//     for (let i = 0; i < LkVideoVideo.length; i++){
//         LkVideoBlockVideo[i].controls = false;
//         buttonLkVideoVideo[i].addEventListener('click', function () {
//             for (let j = 0; j < LkVideoVideo.length; j++){
//                 LkVideoBlockContentVideo[j].classList.remove('no-active');
//                 LkVideoBlockVideo[j].pause();
//             };
//             LkVideoBlockContentVideo[i].classList.add("no-active");
//             LkVideoBlockVideo[i].play();
//             LkVideoBlockVideo[i].controls = true;
//         });
//     }
// }

//Модальное окно открытия входа в личном кабинете
//Страница: ЛК мои курсы, ЛК все курсы, ЛК видео
if (document.querySelector('#button-lk-in-lk')){
    let buttonLkInLk = document.querySelectorAll('#button-lk-in-lk');
    let ModalLkInLk = document.querySelector('.modal-lk-in-lk');
    let buttonModalLkInLkClose = document.querySelector('.modal-lk-in-lk__close');

    for (var i = 0; i < buttonLkInLk.length; i++){
        buttonLkInLk[i].addEventListener('click', function () {
            ModalLkInLk.classList.add("active");
        });
        buttonModalLkInLkClose.addEventListener('click', function () {
            ModalLkInLk.classList.remove("active");
        });
    }
}

//Модальное окно входа в личный кабинет
//Страница: Все кроме ЛК
if (document.querySelector('#button-lk-out-lk')){
    let buttonLkOutLk = document.querySelectorAll('#button-lk-out-lk');
    let ModalLkOutLk = document.querySelector('.modal-lk-out-lk');
    let buttonModalLkOutLkClose = document.querySelector('.modal-lk-out-lk__close');

    for (var i = 0; i < buttonLkOutLk.length; i++){
        buttonLkOutLk[i].addEventListener('click', function () {
            ModalLkOutLk.classList.add("active");
        });
        buttonModalLkOutLkClose.addEventListener('click', function () {
            ModalLkOutLk.classList.remove("active");
        });
    }
}

//Запуск свертывания блока содержание
//Страница: ЛК видео, ЛК открытый курс
// if (document.querySelector('.modal-lk-content-block-point')){
//     let ModalLkContentBlockPoint = document.querySelectorAll('.modal-lk-content-block-point');
//     let buttonLkContentPoint = document.querySelectorAll('#button-lk-content-point');

//     for (var i = 0; i < ModalLkContentBlockPoint.length; i++){
//         buttonLkContentPoint[i].addEventListener('click', function () {
//             for (var j = 0; j < ModalLkContentBlockPoint.length; j++){
//                 ModalLkContentBlockPoint[j].classList.remove('active');
//             };
//             this.parentNode.classList.add('active');
//         });
//     }
// }

//Модальное окно блока содержание
//Страница: ЛК видео, ЛК открытый курс
if (document.querySelector('#button-lk-content')){
    let buttonLkContent = document.querySelectorAll('#button-lk-content');
    let ModalLkContent = document.querySelector('.modal-lk-content');
    let buttonModalLkContentClose = document.querySelector('.modal-lk-content__close');

    for (var i = 0; i < buttonLkContent.length; i++){
        buttonLkContent[i].addEventListener('click', function () {
            ModalLkContent.classList.add("active");
        });
        buttonModalLkContentClose.addEventListener('click', function () {
            ModalLkContent.classList.remove("active");
        });
    }
}

//Модальное окно регистрации
//Все кроме ЛК
// if (document.querySelector('.button-registration')){
//     let buttonRegistration = document.querySelectorAll('.button-registration');
//     let ModalRegistration = document.querySelector('.modal-registration');
//     let ModalRegistrationBlock = document.querySelector('.modal-registration-block');
//     let ModalRegistrationBlockThanks = document.querySelector('.modal-registration-thanks');
//     let buttonModalRegistrationClose = document.querySelector('.modal-registration__close');
//     let buttonModalRegistrationOpenThanks = document.querySelector('.modal-registration__button_open-thanks');

//     for (var i = 0; i < buttonRegistration.length; i++){
//         buttonRegistration[i].addEventListener('click', function () {
//             ModalRegistration.classList.add("active");
//             ModalRegistrationBlock.classList.add("active");
//         });
//         buttonModalRegistrationClose.addEventListener('click', function () {
//             ModalRegistration.classList.remove("active");
//             ModalRegistrationBlockThanks.classList.remove("active");
//         });
//         // buttonModalRegistrationOpenThanks.addEventListener('click', function () {
//         //     ModalRegistrationBlock.classList.remove("active");
//         //     ModalRegistrationBlockThanks.classList.add("active");
//         // });
        
//     }
// }

//Модальное окно авторизации
//Все кроме ЛК
if (document.querySelector('.button-authorization')){
    let buttonAuthorization = document.querySelectorAll('.button-authorization');
    let ModalAuthorization = document.querySelector('.modal-authorization');
    let ModalAuthorizationBlock = document.querySelector('.modal-authorization-block');
    let buttonModalAuthorizationClose = document.querySelector('.modal-authorization__close');

    for (var i = 0; i < buttonAuthorization.length; i++){
        buttonAuthorization[i].addEventListener('click', function () {
            ModalAuthorization.classList.add("active");
            ModalAuthorizationBlock.classList.add("active");
        });
        buttonModalAuthorizationClose.addEventListener('click', function () {
            ModalAuthorization.classList.remove("active");
        });
    }
}

//Модальное окно восстановления
//Все кроме ЛК
if (document.querySelector('.button-recovery')){
    let buttonAuthorization = document.querySelectorAll('.button-recovery');
    let ModalAuthorization = document.querySelector('.modal-recovery');
    let ModalAuthorizationBlock = document.querySelector('.modal-recovery-block');
    let buttonModalAuthorizationClose = document.querySelector('.modal-recovery__close');

    for (var i = 0; i < buttonAuthorization.length; i++){
        buttonAuthorization[i].addEventListener('click', function () {
            ModalAuthorization.classList.add("active");
            ModalAuthorizationBlock.classList.add("active");
        });
        buttonModalAuthorizationClose.addEventListener('click', function () {
            ModalAuthorization.classList.remove("active");
        });
    }
}

//Загрузка изображения в личном кабинете
//ЛК мой профиль
if (document.querySelector('#lk-my-profil__input')){
   let LkMyProfilInput = document.querySelector('#lk-my-profil__input');
   let LkMyProfilInputImg = document.querySelector('#lk-my-profil__img');

    LkMyProfilInput.addEventListener('change', function() {
    if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                LkMyProfilInputImg.setAttribute('src', e.target.result);
            };
            reader.readAsDataURL(this.files[0]);
    }
    
    });
}

if (document.querySelector('.lk-loading')){
    function outNum(num, elem) {
      let LkLoading = document.querySelector(".lk-loading");
      let LkLoadingLogo = document.querySelector(".lk-loading__logo");
      let LkLoadingInner = document.querySelector(".lk-loading__number");
      let LkLoadingTime = 2500;
      let LkLoadingStep = 1;  
      let LkLoadingNumber = 0;

      LkLoadingLogo.style.display = "none"

      let t = Math.round(LkLoadingTime / (num / LkLoadingStep));
      let interval = setInterval(() => {
        LkLoadingNumber = LkLoadingNumber + LkLoadingStep;
        if (LkLoadingNumber == num) {
          clearInterval(interval);
        }
        if (LkLoadingNumber == 100) {
            LkLoadingInner.style.display = "none"
            LkLoadingLogo.style.display = "block"
            LkLoading.style.transition = "1s";
            LkLoading.style.opacity = "0";
        }
        LkLoadingInner.innerHTML = LkLoadingNumber;
      }, t);

    }

    outNum(100, "#out");
}
function previewImage(event) {
    const img = document.getElementById('lk-my-profil__img');
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            img.src = e.target.result; // Устанавливаем источник изображения
        }
        reader.readAsDataURL(file); // Читаем файл как URL
    }
}