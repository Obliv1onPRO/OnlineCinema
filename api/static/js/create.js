$(function () {
    $('[data-toggle="popover"]').popover()
});

$("#room_type").change(function () {
    if (!$("#room_type")[0].checked) {
        $("#invite_label").css({'display': 'none'});
        for (let i = 0; i < $(".invite").length; i++) {
            $($(".invite")[i]).css({'display': 'none'})
        }
    } else {
        $("#invite_label").css({'display': 'flex'});
        for (let i = 0; i < $(".invite").length; i++) {
            $($(".invite")[i]).css({'display': 'block'})
        }
    }
});

$(".invite").click(function () {

});


$('#submit').click(function () {
    let name = $('#room_name').val();
    let type = $('#room_type').val();
    let iframe = $('#iframe').val();
    let csrf = $('input[name=csrfmiddlewaretoken]').val();

    type = (type == 'on' ? false : true);

    let data = JSON.stringify({'name': name, 'type': type, 'iframe': iframe});
    // let data = {'name' : name, 'type' : type, 'iframe' : iframe, 'csrfmiddlewaretoken' : csrf};
    //
    let req = new XMLHttpRequest();
    req.open('POST', '/create', false);
    req.setRequestHeader('Content-type', 'application/json');
    req.setRequestHeader('X-CSRFToken', csrf);
    req.onload = async () => {
        // resp = JSON.parse(req.responseText);
        console.log(req.responseText)
    };
    req.send(data);
});