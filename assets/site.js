const menuButton = document.querySelector('.nav-toggle');
const menu = document.getElementById('main-nav');

if (menuButton && menu) {
  const compact = window.matchMedia('(max-width: 780px)');

  function setMenu(open) {
    menu.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
  }

  function updateMenu() {
    menuButton.hidden = !compact.matches;
    setMenu(!compact.matches);
  }

  menuButton.addEventListener('click', () => setMenu(menu.hidden));
  document.addEventListener('click', (event) => {
    if (compact.matches && !menu.hidden && !event.target.closest('.masthead')) setMenu(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && compact.matches && !menu.hidden) {
      setMenu(false);
      menuButton.focus();
    }
  });
  compact.addEventListener('change', updateMenu);
  updateMenu();
}

const filters = document.querySelector('.filters');
if (filters) {
  const buttons = [...filters.querySelectorAll('button')];
  const panels = [...document.querySelectorAll('[data-panel]')];

  function selectCategory(category) {
    for (const button of buttons) {
      button.setAttribute('aria-pressed', String(button.dataset.category === category));
    }
    for (const panel of panels) {
      panel.hidden = panel.dataset.panel !== category;
    }
  }

  for (const button of buttons) {
    button.addEventListener('click', () => {
      if (button.getAttribute('aria-pressed') === 'true') return;
      selectCategory(button.dataset.category);
      const panel = document.getElementById(button.getAttribute('aria-controls'));
      panel.dispatchEvent(new Event('okay:catalogue-change', { bubbles: true }));
    });
  }
  selectCategory(buttons[0].dataset.category);
  filters.hidden = false;
}

const enquiry = document.getElementById('enquiry-form');
if (enquiry) {
  const product = enquiry.elements.namedItem('product');
  const selected = new URLSearchParams(window.location.search).get('product');
  const copy = document.getElementById('copy-enquiry');
  const status = document.getElementById('enquiry-status');
  const email = enquiry.dataset.email;

  if ([...product.options].some((option) => option.value === selected)) {
    product.value = selected;
  }

  function draft() {
    const fields = new FormData(enquiry);
    const value = (field) => {
      const entry = fields.get(field).trim();
      return entry || 'Not specified';
    };
    return {
      subject: 'Supply enquiry: ' + product.selectedOptions[0].textContent,
      body: [
        'Hello Okay Group,', '',
        'I would like to enquire about ' + product.selectedOptions[0].textContent + '.',
        '', 'Name: ' + value('name'),
        'Company or facility: ' + value('company'),
        'Email: ' + value('email'),
        'Delivery location: ' + value('location'),
        '', 'Requirements:', value('requirements'),
      ].join('\r\n'),
    };
  }

  enquiry.addEventListener('submit', (event) => {
    event.preventDefault();
    const { subject, body } = draft();
    const link = 'mailto:' + email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    status.textContent = 'Your email app should open with the draft. Review it and press Send there.';
    window.location.href = link;
  });

  if (navigator.clipboard) {
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      if (!enquiry.reportValidity()) return;
      const { subject, body } = draft();
      try {
        await navigator.clipboard.writeText('To: ' + email + '\nSubject: ' + subject + '\n\n' + body);
        status.textContent = 'Enquiry copied. Paste it into your email app to send it.';
      } catch {
        status.textContent = 'Copy is unavailable. Use Open email draft or email ' + email + ' directly.';
      }
    });
  }

  enquiry.hidden = false;
}
