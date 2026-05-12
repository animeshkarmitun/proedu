// menu button  start==============================
$(document).ready(function () {
    // jQuery to toggle menu visibility
    $("#menuButton").click(function () {
        $("#menuContainer").toggle();

        // Toggle the icon
        let icon = $(this).find("i");
        if (icon.hasClass("bx-menu")) {
            icon.removeClass("bx-menu").addClass("bx-x");
        } else {
            icon.removeClass("bx-x").addClass("bx-menu");
        }
    });
});


$(document).ready(function () {
    $(window).on("scroll", function () {
        if ($(this).scrollTop() > 0) {
            $("#header .logo").css("display", "block");
        } else {
            $("#header .logo").css("display", "none");
        }
    });
});

/*=============== javascript animation start =================*/

$(document).ready(function () {
    function isInViewport(element) {
        var elementTop = $(element).offset().top;
        var elementBottom = elementTop + $(element).outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop && elementTop < viewportBottom;
    }

    function animateOnScroll() {
        $(".fade-element").each(function () {
            if (isInViewport(this)) {
                $(this).css("opacity", 1);
                $(this).css("top", 0);
                $(this).css("left", 0);
            }
        });
    }

    $(window).on("scroll", animateOnScroll);
    $(window).on("resize", animateOnScroll);

    // Trigger animation on page load
    animateOnScroll();
});

$("#banner").on("slide.bs.carousel", function (e) {
    var $nextSlide = $(e.relatedTarget);
    $nextSlide.find(".banner-fade-element").css("opacity", 0);
    $nextSlide.find(".banner-fade-down").css("transform", "translateY(-20px)");
    $nextSlide.find(".banner-fade-up").css("transform", "translateY(20px)");
    $nextSlide.find(".banner-fade-left").css("transform", "translateX(-20px)");
    $nextSlide.find(".banner-fade-right").css("transform", "translateX(20px)");
});

$("#banner").on("slid.bs.carousel", function (e) {
    var $currentSlide = $(e.relatedTarget);
    $currentSlide.find(".banner-fade-element").css("opacity", 1);
    $currentSlide.find(".banner-fade-down").css("transform", "translateY(0)");
    $currentSlide.find(".banner-fade-up").css("transform", "translateY(0)");
    $currentSlide.find(".banner-fade-left").css("transform", "translateX(0)");
    $currentSlide.find(".banner-fade-right").css("transform", "translateX(0)");
});

$(document).ready(function () {
    $(".carousel-item.active .banner-fade-element").css("opacity", 1);
    $(".carousel-item.active .banner-fade-down").css(
        "transform",
        "translateY(0)"
    );
    $(".carousel-item.active .banner-fade-up").css("transform", "translateY(0)");
    $(".carousel-item.active .banner-fade-left").css(
        "transform",
        "translateX(0)"
    );
    $(".carousel-item.active .banner-fade-right").css(
        "transform",
        "translateX(0)"
    );
});

$(document).ready(function () {
    function applyFadeEffect(elementId) {
        var text = $("#" + elementId)
            .html()
            .split(" ");
        $("#" + elementId).html("");

        for (var i = 0; i < text.length; i++) {
            $("#" + elementId).append(
                '<h2 class="word-fade-element">' + text[i] + "</h2> "
            );
        }

        let observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        $("#" + elementId + " .word-fade-element").each(function (index) {
                            $(this)
                                .delay(120 * index)
                                .queue(function (next) {
                                    $(this).addClass("word-fade-top");
                                    next();
                                });
                        });
                        observer.unobserve(entry.target); // Stop observing once the animation has started
                    }
                });
            },
            { threshold: 0.5 }
        );

        observer.observe(document.getElementById(elementId));
    }
    applyFadeEffect("fade-text");
    applyFadeEffect("fade-text-2");
    applyFadeEffect("fade-text-3");
    applyFadeEffect("fade-text-4");
    applyFadeEffect("fade-text-5");
});
/*=============== javascript animation start =================*/

//from validation start
$(document).ready(function () {
    let currentStep = 1;

    function showValidationMessage(id, condition) {
        if (condition) {
            $(id).removeClass("d-none");
        } else {
            $(id).addClass("d-none");
        }
        return condition;
    }

    function validateGrades(grades) {
        const gradesValue = parseFloat(grades);
        return !isNaN(gradesValue) && gradesValue >= 1.00 && gradesValue <= 5.00;
    }
    $("#next").click(function (e) {
        e.preventDefault(); // Prevent form submission

        // Step data extraction
        var country = $("input[name='country']:checked").val();
        var date = $("input[name='date']:checked").val();
        var degree = $("input[name='degree']:checked").val();
        var lavel = $("input[name='lavel']:checked").val();
        var grades = $("input[name='grades']").val();
        var graduationyear = $("#years option:selected").val();
        var passport = $("input[name='passport']:checked").val();
        var languagetest = $("#languagetest option:selected").val();
        var admit = $("input[name='admit']:checked").val();
        var current_city = $("input[name='current_city']").val();

        switch (currentStep) {
            case 1:
                if (showValidationMessage("#invalid-country", !country)) return;
                $("#step-one").hide();
                $("#step-two").show();
                $(".progress-bar").css("width", "25%");
                currentStep++;
                break;

            case 2:
                let step2Invalid = showValidationMessage("#invalid-date", !date) |
                    showValidationMessage("#invalid-degree", !degree);
                if (step2Invalid) return;
                $("#step-two").hide();
                $("#step-three").show();
                $(".progress-bar").css("width", "50%");
                currentStep++;
                break;

            case 3:
                let step3Invalid = showValidationMessage("#invalid-passport", !passport) |
                    showValidationMessage("#invalid-graduationyear", !graduationyear) |
                    showValidationMessage("#invalid-grades", !validateGrades(grades)) |
                    showValidationMessage("#invalid-lavel", !lavel);
                if (step3Invalid) return;
                $("#step-three").hide();
                $("#step-four").show();
                $(".progress-bar").css("width", "75%");
                currentStep++;
                break;

            case 4:
                let step4Invalid = showValidationMessage("#invalid-languagetest", !languagetest) |
                    showValidationMessage("#invalid-admit", !admit) |
                    showValidationMessage("#invalid-current_city", !current_city);
                if (step4Invalid) return;
                $("#step-four").hide();
                $("#step-five").show();
                $("#next").hide();
                $(".progress-bar").css("width", "100%");
                currentStep++;
                break;
            default:
                break;
        }
    });

    $("#back").click(function () {
        switch (currentStep) {
            case 2:
                $("#step-two").hide();
                $("#step-one").show();
                $(".progress-bar").css("width", "0%");
                currentStep--;
                break;
            case 3:
                $("#step-three").hide();
                $("#step-two").show();
                $(".progress-bar").css("width", "25%");
                currentStep--;
                break;
            case 4:
                $("#step-four").hide();
                $("#step-three").show();
                $(".progress-bar").css("width", "50%");
                currentStep--;
                break;
            case 5:
                $("#step-five").hide();
                $("#step-four").show();
                $(".progress-bar").css("width", "75%");
                currentStep--;
                break;
            default:
                break;
        }
    });
});


/** Initiate Pure Counter*/
new PureCounter();

/**
 * Frequently Asked Questions Toggle
 */
document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
        faqItem.parentNode.classList.toggle('faq-active');
    });
});