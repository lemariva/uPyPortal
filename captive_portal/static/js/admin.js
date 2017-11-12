
LoginData = window.LoginData || {};

$(document).ready(function() {
  var form = $('form#login-form');

  $('a').click(function(e, obj) {
    e.preventDefault();
    var panel = e.target.parentNode.parentNode
    $.post(e.target.href, function(data) {
      if (data.success) {
        panel.remove();
      }
    });
  });


/*
  form.submit(function( event ) {
    event.preventDefault();
    submitLogin();
  });

  function submitLogin() {
    $.post(form.attr('target'), form.serialize(), function(data) {
      if (data.success) {
        var test = data;
      } else {
      }
    });
  }
*/

});

/*
$('.grid').masonry({
  // options
  itemSelector: '.grid-item',
  columnWidth: 200
});

function archive() {
  var elem = $(this);
  var panel = elem.parents('.panel');
  var self = this;
  $.post(elem.attr('href'), function(data) {
    if (data.success) {
      panel.remove();
      $('ul.logins').masonry();
    }
  });
}
*/
