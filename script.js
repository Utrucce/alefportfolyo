/**
 * ALΣF Portal & Privacy Script
 * Sertan Çubukcu (sertancubukcu@gmail.com)
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dil Seçici (Türkçe / English / İkisi)
  const langButtons = document.querySelectorAll('.lang-btn');
  const dualContainers = document.querySelectorAll('.dual-lang-container');

  function setLanguage(lang) {
    if (!['tr', 'en', 'both'].includes(lang)) lang = 'tr';
    document.documentElement.setAttribute('data-lang', lang);
    document.documentElement.lang = lang === 'en' ? 'en' : 'tr';

    langButtons.forEach(btn => {
      const isActive = btn.dataset.lang === lang;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });

    document.querySelectorAll('.content-tr').forEach(el => {
      el.hidden = (lang === 'en');
    });
    document.querySelectorAll('.content-en').forEach(el => {
      el.hidden = (lang === 'tr');
    });

    const wide = window.matchMedia('(min-width: 900px)').matches;
    dualContainers.forEach(c => {
      c.style.gridTemplateColumns = (lang === 'both' && wide) ? '1fr 1fr' : '1fr';
    });

    try { localStorage.setItem('alef_site_lang', lang); } catch (e) {}
  }

  langButtons.forEach(btn => {
    btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
  });

  let savedLang = 'tr';
  try { savedLang = localStorage.getItem('alef_site_lang') || 'tr'; } catch (e) {}
  setLanguage(savedLang);

  window.addEventListener('resize', () => {
    setLanguage(document.documentElement.getAttribute('data-lang') || 'tr');
  });

  // 2. Ekran Görüntüleri Kaydırma Rayı (Carousel)
  const track = document.getElementById('screenshotTrack');
  const prevBtn = document.getElementById('prevScreenshot');
  const nextBtn = document.getElementById('nextScreenshot');

  if (track) {
    const scrollStep = 280;
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        track.scrollBy({ left: -scrollStep, behavior: 'smooth' });
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        track.scrollBy({ left: scrollStep, behavior: 'smooth' });
      });
    }
  }

  // 3. Büyük Görüntüleyici (Lightbox Modal)
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

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });

  document.querySelectorAll('.phone-mockup, .zoomable').forEach(card => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('a')) return;
      const img = card.querySelector('img');
      const caption = card.querySelector('.phone-caption, h4, .app-meta h3');
      if (img) openLightbox(img.src, caption ? caption.textContent.trim() : img.alt);
    });
  });

  // 4. Bildirim Kutusu (Toast)
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
    setTimeout(() => toast.classList.remove('show'), 3000);
  }

  function copyText(text, okMsg) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(() => showToast(okMsg)).catch(() => fallbackCopy(text, okMsg));
    } else {
      fallbackCopy(text, okMsg);
    }
  }

  function fallbackCopy(text, okMsg) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      showToast(okMsg);
    } catch (e) {
      showToast('Kopyalanamadı, lütfen elle kopyalayın.');
    }
    document.body.removeChild(ta);
  }

  // 5. E-posta Kopyalama
  document.querySelectorAll('[data-copy-email]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      copyText('sertancubukcu@gmail.com', 'E-posta adresi kopyalandı: sertancubukcu@gmail.com');
    });
  });

  // 6. Gizlilik Politikası Metnini Kopyalama
  const copyPolicyBtn = document.getElementById('copyPolicyBtn');
  if (copyPolicyBtn) {
    copyPolicyBtn.addEventListener('click', () => {
      const lang = document.documentElement.getAttribute('data-lang') || 'tr';
      const tr = document.querySelector('.policy-full-tr');
      const en = document.querySelector('.policy-full-en');
      let text = '';
      if (lang === 'en') text = en ? en.innerText : '';
      else if (lang === 'both') text = (tr ? tr.innerText : '') + '\n\n' + (en ? en.innerText : '');
      else text = tr ? tr.innerText : '';
      if (text.trim()) copyText(text.trim(), 'Gizlilik politikası metni kopyalandı.');
    });
  }
});
