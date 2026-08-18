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

  // Let a URL hash open the right tab, so links from other pages
  // (e.g. /blog/ -> /#publications) land where they should.
  var hashToLink = {
    '#home': '#home-link',
    '#news': '#activities-link',
    '#activities': '#activities-link',
    '#publications': '#publications-link',
    '#teaching': '#teaching-link',
    '#about': '#about-link'
  };

  function openTabFromHash() {
    var link = hashToLink[window.location.hash];
    if (link && $(link).length) {
      $(link).click();
    }
  }

  openTabFromHash();
  $(window).on('hashchange', openTabFromHash);

});

function styleReset() {
  $('.link').removeClass('active-link');
  $('.content').removeClass('active');
}
