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

//Запуск свертывания блока FAQ
if (document.querySelector('.faq-block')) {
    let FaqBlock = document.querySelectorAll('.faq-block');
    let buttonFaq = document.querySelectorAll('#button-faq');

    for (var i = 0; i < FaqBlock.length; i++) {
        buttonFaq[i].addEventListener('click', function () {
            // Проверяем, есть ли у текущего блока класс 'active'
            if (this.parentNode.classList.contains('active')) {
                // Если есть, убираем его
                this.parentNode.classList.remove('active');
            } else {
                // Если нет, убираем класс 'active' у всех блоков
                for (var j = 0; j < FaqBlock.length; j++) {
                    FaqBlock[j].classList.remove('active');
                }
                // Добавляем класс 'active' к текущему блоку
                this.parentNode.classList.add('active');
            }
        });
    }
}
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