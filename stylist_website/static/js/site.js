$(document).ready(function() {	
	//Доформирование лид формы
	if($("form.fastForm").length)
	{
		$("form.fastForm").each(function(index, value) {
			$(this).append('<input type=\"hidden\" name=\"f_name\" value=\"Форма N '+index+'\">');
			$(this).append('<input type=\"hidden\" name=\"r_url\" value=\"'+document.location.href+'\">');
			$(this).append('<input type=\"hidden\" name=\"t_url\" value=\"'+$('h1').text()+'\">');
		});
	}

	/* отправка формы */
	var fastForm = new Array;
	fastForm['forms'] = $("form.fastForm");
	fastForm['forms'].off("submit");

	fastForm['forms'].on("submit", function () {
		var form = $(this),
			submit = form.find("[type=submit]");

		submit.attr('disabled','disabled').addClass('disabled');
		// submit.append('<i class="fa fa-spinner fa-spin" style="margin-left: 5px;"></i>');
		var data = form.serializeArray();

		$.ajax({
			"url": form.attr("action"),
			"type": form.attr("method"),
			"data": data,

			"success": function (data) {
				if (data.indexOf('alert(') == '-1') {
					if (form.parents('.is-modal').length) {
						form.parents('.is-modal').find('.modal-callback__title').remove();
					}

					form.html(data);
				} else {
					if (!form.find('.fastForm__result').length) {
						form.append('<div class="fastForm__result"></div>');
					}
					form.find('.fastForm__result').html(data);					
				}
			},

			"complete": function () {
				submit.removeAttr('disabled').removeClass('disabled');
				submit.find('i.fa-spinner').remove();
			},

			"error": function (jqXHR, error, errorThrown) {
				console.log(jqXHR, error, errorThrown);
			}
		});

		return false;
	});

	// Отправка формы способ 2
	var 
	ajaxForm = new Array;
	ajaxForm['template'] = new Array
	ajaxForm['template']['output'] = "<div class=\"output\"></div>";
	ajaxForm['template']['success'] = "<div class=\"success alert alert-success\"></div>",
	ajaxForm['template']['error'] = "<div class=\"error alert alert-danger\"></div>";
	ajaxForm['forms'] = $("form.ajaxForm");
	ajaxForm['upload'] = $('#ajaxFormUpload');
	ajaxForm['uploadResult'] = $('#ajaxFormUploadResult');

	ajaxForm['forms'].off("submit");
	ajaxForm['forms'].on("submit", function () {
		var 
		form = $(this),
		form_id = form.attr('id'),
		submit = form.find("[type=submit]"),
		submit_2 = $("button[form="+form_id+"]"),
		alerts = form.find('.alert');

		var output = form.find('.output');
		if (output.length == 0) {
			output = $('.output[data-form='+form_id+']');
			if (output.length == 0) {
				form.append('<div class="output"></div>');
				output = form.find('.output');
			}
		}
		
		submit.attr('disabled','disabled').addClass('disabled');
		submit_2.attr('disabled','disabled').addClass('disabled');
		
		if ($('input[form=ajaxFormUpload]').length)
		{
			ajaxForm['upload'].trigger('submit');
			ajaxForm['uploadResult'].off('load');
			ajaxForm['uploadResult'].on('load', function () {
				console.log($(this).contents().text());

				var files = JSON.parse($(this).contents().text().match(/\{.*\}$/)[0])['files'];
				var filesCnt = files.length;
				for (var i = 0; i < filesCnt; i++)
				{
					form.append('<input type="hidden" class="temp" name="' + files[i]['name'] + '" value="' + files[i]['value'] + '" />');
					form.append('<input type="hidden" class="temp" name="' + files[i]['name'] + '" value="' + files[i]['value'] + '" />');
				}
				var data = form.serializeArray();
				
				$.ajax({
					"url": form.attr("action"),
					"type": form.attr("method"),
					"data": data,
					"dataType": "json",
					"complete": function () {
						
					},
					"error": function (jqXHR, error, errorThrown) {
						output.empty();
						submit.removeAttr('disabled').removeClass('disabled');
						submit_2.removeAttr('disabled').removeClass('disabled');
//						output.append('<div class="alert alert-danger">'+error+'</div>');
						output.append('<div class="alert alert-danger">Возникла ошибка при выполнении Ajax-запроса</div>');
					},
					"success": function (data) {
						output.empty();
						submit.removeAttr('disabled').removeClass('disabled');
						submit_2.removeAttr('disabled').removeClass('disabled');
						if (typeof(data.success) != 'undefined')
						{
							if (data.success.tmpl == 'clean') {
								output.append(data.success.message);
							} else {
								output.append('<div class="alert alert-success">'+data.success.message+'</div>');
							}
							if (typeof(data.success.timeout) != 'undefined')
							{
								setTimeout(function () {
									if (typeof(data.success.redirect) != 'undefined')
									{
										window.location = data.success.redirect;
									}
									if (typeof(data.success.trigger) != 'undefined')
									{
										form.trigger(data.success.trigger);
									}
									if (typeof(data.success.refresh) != 'undefined')
									{
										window.location = window.location;
									}
								}, data.success.timeout);
							}
						}
						else if (typeof(data.error) != 'undefined')
						{
							for (var i in data.error)
							{
								output.append('<div class="alert alert-danger">'+data.error[i].message+'</div>');
							}							
						}
					}
				});
			});
		}
		else
		{
			var data = form.serializeArray();
				
			$.ajax({
				"url": form.attr("action"),
				"type": form.attr("method"),
				"data": data,
				"dataType": "json",
				"complete": function () {
					form.find('.temp').remove();
				},
				"error": function (jqXHR, error, errorThrown) {
					output.empty();
					submit.removeAttr('disabled').removeClass('disabled');
					submit_2.removeAttr('disabled').removeClass('disabled');
//					output.append('<div class="alert alert-danger">'+error+'</div>');
					output.append('<div class="alert alert-danger">Возникла ошибка при выполнении Ajax-запроса</div>');
				},
				"success": function (data) {
					output.empty();
					submit.removeAttr('disabled').removeClass('disabled');
					submit_2.removeAttr('disabled').removeClass('disabled');
					if (typeof(data.success) != 'undefined')
					{
						if (data.success.tmpl == 'clean') {
							output.append(data.success.message);
						} else {
							output.append('<div class="alert alert-success">'+data.success.message+'</div>');
						}
						
						if (typeof(data.success.timeout) != 'undefined')
						{
							setTimeout(function () {
								if (typeof(data.success.redirect) != 'undefined')
								{
									window.location = data.success.redirect;
								}
								if (typeof(data.success.trigger) != 'undefined')
								{
									form.trigger(data.success.trigger);
								}
								if (typeof(data.success.refresh) != 'undefined')
								{
									window.location = window.location;
								}
							}, data.success.timeout);
						}
					}
					else if (typeof(data.error) != 'undefined')
					{
						let message = '';
						for (var i in data.error)
						{
							message += data.error[i].message+' ';
						}
						output.append('<div class="alert alert-danger">'+message+'</div>');
					}
				}
			});
		}
		
		return false;
	});


	$(document).on('click', '.courses-show-type-js', function(e) {
		e.preventDefault();
		let wrap = $('.courses-wrap');
		let type = $(this).data('type');
		let limit_courses = 2;

		if (!type || !wrap) { return false; }

		$(this).parents('.courses-buttons').find('.courses-show-type-js').removeClass('active')
		$(this).addClass('active')

		wrap.find('.courses-block-container').hide();
		if (type == 'all') {
			wrap.find('.courses-block-container:lt('+limit_courses+')').show();
		} else {
			wrap.find('.courses-block-container.courses-type-'+type+':lt('+limit_courses+')').show();			
		}
	});

	if ($('.courses-wrap').length) {
		let limit_courses = 2;
		let wrap = $('.courses-wrap');
		let btn_show_more = wrap.find('.courses-show-more-js');

		if (wrap.find('.courses-block-container').length > limit_courses) {
			btn_show_more.parent().show();
			wrap.find('.courses-block-container:gt('+(limit_courses-1)+')').hide();
		}
	}

	$(document).on('click', '.courses-show-more-js', function(e) {
		e.preventDefault();

		let wrap = $('.courses-wrap');
		let btn_show_more = wrap.find('.courses-show-more-js');
		let all_courses = wrap.find('.courses-block-container').length;
		let showed_courses = wrap.find('.courses-block-container:visible').length;
		let limit_courses = 2;

		if (showed_courses + limit_courses >= all_courses) {
			btn_show_more.parent().hide();
		}

		let type = $('.courses-show-type-js.active').data('type');
		let type_class = '';
		if (!!type && type != 'all') {
			type_class = '.courses-type-'+type;
		}
		
		wrap.find('.courses-block-container'+type_class+':lt('+(showed_courses + limit_courses)+')').show();
	});

	$.each($('.popup-gallery'), function() {
		$(this).magnificPopup({
			delegate: 'a',
			type: 'image',
			tClose: 'Закрыть (Esc)',
			tLoading: 'Загрузка изображения',
			mainClass: 'mfp-with-zoom mfp-img-mobile',
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1]
			}
		});
	});

	$('.open-modal-iframe-js').magnificPopup({
		type:'iframe',
		closeBtnInside: false,
		midClick: true,
		mainClass: 'my-mfp-zoom-in',
		removalDelay: 200,
		fixedContentPos: true,
		fixedBgPos: true,
	});
	

	$(document).on('click', '.set-view-lesson-js', function() {
		let _this = $(this);
		let data = {};
		data.course_id = $(this).data('course_id');
		data.theme_id = $(this).data('theme_id');
		data.lesson_id = $(this).data('lesson_id');

		$.ajax({
			"url": '/profile/set_view_lesson',
			"type": 'post',
			"data": data,

			"success": function (data) {
			},

			"complete": function () {
				_this.parent().find('.lk-video-content__video__point').addClass('active');
			},

			"error": function (jqXHR, error, errorThrown) {
				console.log(jqXHR, error, errorThrown);
			}
		});
	});


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

	$(document).on('click', '.buy-course-js', function(){
		let tarif_id = $(this).data('tarif_id');
		let tarif_select_el = $('#modal-buy-course select[name="tarif_id"]');
		if (!!tarif_id && !!tarif_select_el) {
			tarif_select_el.find('option[value="'+tarif_id+'"]').prop('selected', true);
			tarif_select_el.trigger('change');
		}
	});

	$(document).on('change', '#modal-buy-course select[name="tarif_id"]', function(){
		let price_f = $(this).find('option:selected').data('price_f');
		let price_el = $('#modal-buy-course .modal-buy__price');

		if (!!price_f && !!price_el) {
			price_el.html(price_f);
			price_el.data('price', price_f);
		}

		getPromocode();
	});

	$(document).on('input', '.modal-buy__promocod', function(){
		if (!!window.timeout_get_promocode) {
			clearTimeout(window.timeout_get_promocode);
		}

		window.timeout_get_promocode = setTimeout(function() {
			getPromocode();
		}, 500);
	});

	function getPromocode() {
		let _this = $('#modal-buy-course').find('.modal-buy__promocod');
		let promocode = _this.val();
		let course_id = $('#modal-buy-course').find('input[name="course_id"]').val();
		let tarif_id = $('#modal-buy-course').find('select[name="tarif_id"] option:selected').val();
		let promocod_info_el =  $('#modal-buy-course').find('.modal-buy__promocod-info');
		let price_el = $('#modal-buy-course .modal-buy__price');

		promocod_info_el.text('');

		$.ajax({
			url: '/promocodes/get_promocode_info',
			type: 'post',
			data: {
				promocode: promocode, 
				course_id: course_id, 
				tarif_id: tarif_id
			},
			success: function(data) {
				if (data.info != undefined) {
					promocod_info_el.text(data.info);
				}

				if (data.price_f != undefined) {
					price_el.text(data.price_f);
					$('#modal-buy-course .modal-buy__free').show();
					$('#modal-buy-course .modal-buy__payments').hide();
				} else {
					$('#modal-buy-course .modal-buy__free').hide();
					$('#modal-buy-course .modal-buy__payments').show();
					price_el.text(price_el.data('price'));
				}
			},
		});    
	}

	$(document).on('click', '.form-payment .button-payment', function(){
		let type_id = $(this).data('type_id');
		let form = $('.form-payment');

		form.find('input[name="type_id"]').val(type_id);
		form.submit();
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