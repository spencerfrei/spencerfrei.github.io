$(document).ready(function () {
  $('#about-link').click(function () {
    styleReset();
    $(this).addClass('active-link');
    $('#about').addClass('active');
  });

  $('#home-link').click(function () {
    styleReset();
    $(this).addClass('active-link');
    $('#home').addClass('active');
  });

  $('#teaching-link').click(function () {
    styleReset();
    $(this).addClass('active-link');
    $('#teaching').addClass('active');
  });

  $('#publications-link').click(function () {
    styleReset();
    $(this).addClass('active-link');
    $('#publications').addClass('active');
  });

  $('#activities-link').click(function () {
    styleReset();
    $(this).addClass('active-link');
    $('#activities').addClass('active');
  });

  //    $('#tutor-link').click(function(){
  //   	styleReset();
  //   	$(this).addClass('active-link');
  //    	$('#tutoring').addClass('active');
  //    });
});

function styleReset() {
  $('.link').removeClass('active-link');
  $('.content').removeClass('active');
}
