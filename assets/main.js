/* Her Balanced Body article helpers */
(function () {
  const sections = document.querySelectorAll('.post-body h2[id], .post-body h3[id]');
  const navLinks = document.querySelectorAll('.toc-list a');

  if (!sections.length || !navLinks.length) return;

  function onScroll() {
    let current = '';

    sections.forEach(function (section) {
      const sectionTop = section.offsetTop - 140;
      if (window.pageYOffset >= sectionTop) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(function (link) {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', onScroll);
  onScroll();
})();
