(function ($) {
    "use strict";

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Team carousel
    $(".team-carousel, .related-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 30,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 30,
        dots: true,
        loop: true,
        center: true,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 30,
        dots: true,
        loop: true,
        center: true,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0: {
                items: 2
            },
            576: {
                items: 3
            },
            768: {
                items: 4
            },
            992: {
                items: 5
            },
            1200: {
                items: 6
            }
        }
    });

})(jQuery);

function required() {

    // data send from form to card
    var year = document.Modelform.year.value;
    var engine_hp = document.Modelform.engine_hp.value;
    var engine_cylinders = document.Modelform.engine_cylinders.value;
    var highway_mpg = document.Modelform.highway_mpg.value;
    var city_mpg = document.Modelform.city_mpg.value;
    if (year === "") {
        document.getElementById("year_label").style.color = "rgb(255, 166, 0)";
        // return true;
    }
    if (engine_hp === "") {
        document.getElementById("engine_hp_label").style.color = "rgb(255, 166, 0)";
        // return true;
    }
    if (engine_cylinders === "") {
        document.getElementById("engine_cylinders_label").style.color = "rgb(255, 166, 0)";
        // return true;
    }
    if (highway_mpg === "") {
        document.getElementById("highway_mpg_label").style.color = "rgb(255, 166, 0)";
        // return true;
    }
    if (city_mpg === "") {
        document.getElementById("city_mpg_label").style.color = "rgb(255, 166, 0)";
        // return true;
    }
    else {
        return true;
    }
}



var popupViews = document.querySelectorAll('.popup-view');
var popupBtns = document.querySelectorAll('.popup-btn');
var closeBtns = document.querySelectorAll('.close-btn');

//javascript for quick view button
var popup = function (popupClick) {
    popupViews[popupClick].classList.add('active');
}

popupBtns.forEach((popupBtn, i) => {
    popupBtn.addEventListener("click", () => {
        popup(i);
    });
});

//javascript for close button
closeBtns.forEach((closeBtn) => {
    closeBtn.addEventListener("click", () => {
        popupViews.forEach((popupView) => {
            popupView.classList.remove('active');
        });
    });
});

var myApp = new function () {
    this.printDiv = function () {
        var div = document.getElementById('DataPrint');
        var win = window.open('', '', 'height=700,width=700');

        // Define and style for the elements and store it in a vairable.
        var style = '<style>';
        style = style + 'div, p {border: solid 1px #CCC;' +
            'padding: 10px;}';
        style = style + "img { width: 75px; height: 75px;}";
        style = style + '</style>';

        // Now, write the DIV contents with CSS styles and print it.
        win.document.write(style);
        win.document.write(div.outerHTML);
        win.print();
    }
}

//     //var make = document.Modelform.make.value;
//    // var model = document.Modelform.model.value;
//    var year = document.Modelform.year.value;
//    // var engine_fuel_type = document.Modelform.engine_fuel_type.value;
//     var engine_hp = document.Modelform.engine_hp.value;
//     var engine_cylinders = document.Modelform.engine_cylinders.value;
//    // var transmission_type = document.Modelform.transmission_type.value;
//    // var driven_wheels = document.Modelform.driven_wheels.value;
//    // var number_of_doors = document.Modelform.number_of_doors.value;
//     //var vehicle_size = document.Modelform.vehicle_size.value;
//     //var vehicle_style = document.Modelform.vehicle_style.value;
//     var highway_mpg = document.Modelform.highway_mpg.value;
//     var city_mpg = document.Modelform.city_mpg.value;
// document.getElementById('makeData').innerHTML = document.Modelform.make.value;
// document.getElementById('modelData').innerHTML = document.Modelform.model.value;
// document.getElementById('yearData').innerHTML = document.Modelform.year.value;
// document.getElementById('engine_fuel_typeData').innerHTML = document.Modelform.engine_fuel_type.value;
// document.getElementById('engine_hpData').innerHTML = document.Modelform.engine_hp.value;
// document.getElementById('engine_cylindersData').innerHTML = document.Modelform.engine_cylinders.value;
// document.getElementById('transmission_typeData').innerHTML = document.Modelform.transmission_type.value;
// document.getElementById('driven_wheelsData').innerHTML = document.Modelform.driven_wheels.value;
// document.getElementById('number_of_doorsData').innerHTML = document.Modelform.number_of_doors.value;
// document.getElementById('vehicle_sizeData').innerHTML = document.Modelform.vehicle_size.value;
// document.getElementById('vehicle_styleData').innerHTML = document.Modelform.vehicle_style.value;
// document.getElementById('highway_mpgData').innerHTML = document.Modelform.highway_mpg.value;
// document.getElementById('city_mpgData').innerHTML = document.Modelform.city_mpg.value;