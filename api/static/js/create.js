$(function () {
  $('[data-toggle="popover"]').popover()
});

$("#room_type").change(function () {
  if(!$("#room_type")[0].checked){
    $("#invite_label").css({'display' : 'none'});
    for (let i = 0; i < $(".invite").length; i++) {
       $($(".invite")[i]).css({'display' : 'none'})
    }
  }
  else {
    $("#invite_label").css({'display' : 'flex'});
    for (let i = 0; i < $(".invite").length; i++) {
      $($(".invite")[i]).css({'display' : 'block'})
    }
  }
});