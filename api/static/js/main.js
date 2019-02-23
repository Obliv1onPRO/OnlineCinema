$(document).ready(function () {
    $('.header').height($(window).height());
});

$(".navbar a, .description button").click(function () {
    $("body,html").animate({
        scrollTop: $("#" + $(this).data('value')).offset().top
    }, 1000)
});
