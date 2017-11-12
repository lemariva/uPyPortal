$(document).ready(function() {
  var form = $('form#login-form');

  $('#login-button').css("visibility", "visible");

  form.submit(function( event ) {
    event.preventDefault();
    submitLogin();
  });

  function submitLogin() {
    $.post(form.attr('target'), form.serialize(), function(data) {
      if (data.success) {
        $('#popup_success').popup('show');
      } else {
        $('#popup_error').popup('show');
      }
    });
  }

  // style for the overlays
  $('#popup_error').popup({
    color: 'white',
    opacity: 1,
    transition: '0.3s',
    scrolllock: true
  });

  $('#popup_success').popup({
    color: 'white',
    opacity: 1,
    transition: '0.3s',
    scrolllock: true
  });

});
