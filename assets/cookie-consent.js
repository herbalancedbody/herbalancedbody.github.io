(function () {
  const banner = document.getElementById('cookie-consent');
  if (!banner) return;

  const storageKey = 'hbb:cookie-consent';

  const hide = () => banner.classList.add('hidden');

  if (sessionStorage.getItem(storageKey) === 'accepted') {
    hide();
    return;
  }

  document.getElementById('cookie-accept')?.addEventListener('click', () => {
    sessionStorage.setItem(storageKey, 'accepted');
    hide();
  });

  document.getElementById('cookie-settings')?.addEventListener('click', () => {
    const accepted = confirm('Only essential cookies are used for site functionality and analytics. Do you accept cookies?');
    if (accepted) {
      sessionStorage.setItem(storageKey, 'accepted');
    }
    hide();
  });
})();
