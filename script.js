document.addEventListener('DOMContentLoaded', () => {
  // 1. Language Switcher Logic
  const langButtons = document.querySelectorAll('.lang-btn');
  const trContent = document.querySelectorAll('.content-tr');
  const enContent = document.querySelectorAll('.content-en');
  const dualContainer = document.querySelector('.dual-lang-container');
  let activeLanguage = 'tr';

  function updateLanguageColumns() {
    if (!dualContainer) return;
    dualContainer.style.gridTemplateColumns =
      activeLanguage === 'both' && window.innerWidth > 860
        ? 'repeat(2, minmax(0, 1fr))'
        : '1fr';
  }

  function setLanguage(lang) {
    if (!['tr', 'en', 'both'].includes(lang)) lang = 'tr';
    activeLanguage = lang;

    langButtons.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
      btn.setAttribute('aria-pressed', String(btn.dataset.lang === lang));
    });

    if (lang === 'tr') {
      trContent.forEach(el => el.style.display = 'block');
      enContent.forEach(el => el.style.display = 'none');
    } else if (lang === 'en') {
      trContent.forEach(el => el.style.display = 'none');
      enContent.forEach(el => el.style.display = 'block');
    } else if (lang === 'both') {
      trContent.forEach(el => el.style.display = 'block');
      enContent.forEach(el => el.style.display = 'block');
    }
    updateLanguageColumns();
    try {
      localStorage.setItem('alef_site_lang', lang);
    } catch (error) {
      showToast('Dil tercihi bu tarayıcıda kaydedilemedi.');
    }
  }

  langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      setLanguage(btn.dataset.lang);
    });
    window.addEventListener('resize', updateLanguageColumns);
  });

  let savedLang = 'tr';
  try {
    savedLang = localStorage.getItem('alef_site_lang') || 'tr';
  } catch (error) {
    showToast('Dil tercihi okunamadı; Türkçe gösteriliyor.');
  }
  setLanguage(savedLang);

  // 2. Carousel Controls
  const track = document.getElementById('screenshotTrack');
  const prevBtn = document.getElementById('prevScreenshot');
  const nextBtn = document.getElementById('nextScreenshot');

  if (track && prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
      track.scrollBy({ left: -280, behavior: 'smooth' });
    });
    nextBtn.addEventListener('click', () => {
      track.scrollBy({ left: 280, behavior: 'smooth' });
    });
  }

  // 3. Lightbox Functionality
  const lightbox = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const lightboxClose = document.getElementById('lightboxClose');

  function openLightbox(src, caption) {
    if (!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    if (lightboxCaption) lightboxCaption.textContent = caption || '';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (lightboxClose) {
    lightboxClose.addEventListener('click', closeLightbox);
  }

  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });

  // Attach Lightbox to mockups and info cards
  document.querySelectorAll('.phone-mockup, .info-card').forEach(card => {
    card.addEventListener('click', () => {
      const img = card.querySelector('img');
      const caption = card.querySelector('.phone-caption, h4');
      if (img) {
        openLightbox(img.src, caption ? caption.textContent.trim() : '');
      }
    });
  });

  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }

    const field = document.createElement('textarea');
    field.value = text;
    field.setAttribute('readonly', '');
    field.style.position = 'fixed';
    field.style.opacity = '0';
    document.body.appendChild(field);
    field.select();

    let copied = false;
    try {
      copied = document.execCommand('copy');
    } catch (error) {
      field.remove();
      return Promise.reject(error);
    }

    field.remove();
    return copied
      ? Promise.resolve()
      : Promise.reject(new Error('Panoya kopyalama desteklenmiyor.'));
  }

  // 4. Toast Notification
  function showToast(message) {
    let toast = document.getElementById('toastNotice');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toastNotice';
      toast.className = 'toast-notice';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 3000);
  }

  // 5. Copy Email
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const email = 'sertancubukcu@gmail.com';
      copyToClipboard(email).then(() => {
        showToast('E-posta adresi panoya kopyalandı: ' + email);
      }).catch(() => {
        showToast('E-posta: ' + email);
      });
    });
  }

  // 6. Copy Full Policy Text for Play Console
  const copyPolicyBtn = document.getElementById('copyPolicyBtn');
  if (copyPolicyBtn) {
    copyPolicyBtn.addEventListener('click', () => {
      let activeLang = 'tr';
      try {
        activeLang = localStorage.getItem('alef_site_lang') || 'tr';
      } catch (error) {
        showToast('Dil tercihi okunamadı; Türkçe metin kopyalanıyor.');
      }
      let textToCopy = '';
      if (activeLang === 'en') {
        const enBox = document.querySelector('.content-en-full');
        textToCopy = enBox ? enBox.innerText : '';
      } else {
        const trBox = document.querySelector('.content-tr-full');
        textToCopy = trBox ? trBox.innerText : '';
      }
      if (textToCopy) {
        copyToClipboard(textToCopy).then(() => {
          showToast('Gizlilik Politikası metni panoya kopyalandı.');
        }).catch(() => {
          showToast('Kopyalama başarısız oldu, lütfen manuel kopyalayın.');
        });
      }
    });
  }
});
