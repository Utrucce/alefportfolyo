/**
 * ALΣF Portal & Privacy Script
 * Sertan Çubukcu (sertancubukcu@gmail.com)
 * 
 * Özellikler:
 * 1. Dil Seçici (TR / EN / İkisi)
 * 2. Ekran Görüntüleri Rayı & Lightbox Büyütücü
 * 3. Bildirim & E-posta Kopyalama
 * 4. Animasyonlu Mitolojik Tuval (Loraks, Transformers Energon, Yu-Gi-Oh Yıldızları)
 * 5. Gerçekçi 3B Kanat Çırpan Eterik Kelebekler (Anatomik Forewing/Hindwing & Süzülüş)
 * 6. Gerçekçi Kambur Balina (Humpback Whale), Su Fışkırtma & Yüzü Islatacak Dev Su Sıçratması
 * 7. Web Audio API Gerçekçi Balina Şarkısı & Deniz Çarpma/Sıçrama Sesi
 */

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================
  // 1. DİL SEÇİCİ (TR / EN / İKİSİ)
  // ==========================================
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
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      setLanguage(btn.dataset.lang);
    });
  });

  let savedLang = 'tr';
  try { savedLang = localStorage.getItem('alef_site_lang') || 'tr'; } catch (e) {}
  setLanguage(savedLang);

  window.addEventListener('resize', () => {
    setLanguage(document.documentElement.getAttribute('data-lang') || 'tr');
  });


  // ==========================================
  // 2. EKRAN GÖRÜNTÜLERİ KAYDIRMA RAYI
  // ==========================================
  const track = document.getElementById('screenshotTrack');
  const prevBtn = document.getElementById('prevScreenshot');
  const nextBtn = document.getElementById('nextScreenshot');

  if (track) {
    const scrollStep = 280;
    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.preventDefault();
        track.scrollBy({ left: -scrollStep, behavior: 'smooth' });
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        track.scrollBy({ left: scrollStep, behavior: 'smooth' });
      });
    }
  }


  // ==========================================
  // 3. BÜYÜK GÖRÜNTÜLEYİCİ (LIGHTBOX MODAL)
  // ==========================================
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


  // ==========================================
  // 4. BİLDİRİM & KOPYALAMA İŞLEMLERİ
  // ==========================================
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
    setTimeout(() => toast.classList.remove('show'), 3200);
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
      showToast('Kopyalanamadı, lütfen elle kopyalayınız.');
    }
    document.body.removeChild(ta);
  }

  document.querySelectorAll('[data-copy-email]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      copyText('sertancubukcu@gmail.com', 'E-posta adresi kopyalandı: sertancubukcu@gmail.com');
    });
  });

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


  // ==========================================
  // 5. SES MOTORU (WEB AUDIO API - BALİNA ŞARKISI & SU ÇARPMASI)
  // Hiçbir harici dosya indirmeden saf matematiksel akustik sentez
  // ==========================================
  let audioCtx = null;

  function initAudio() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  document.addEventListener('click', initAudio, { once: true });
  document.addEventListener('touchstart', initAudio, { once: true });

  // 1. Derin Okyanus Balina Çağrısı Sentezi
  function playWhaleSong() {
    try {
      initAudio();
      if (!audioCtx) return;

      const now = audioCtx.currentTime;
      const osc1 = audioCtx.createOscillator();
      const osc2 = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc1.type = 'sine';
      osc2.type = 'triangle';

      // Rezonant Bant Geçiren Filtre (Derin Su Akustiği)
      filter.type = 'bandpass';
      filter.Q.setValueAtTime(4.5, now);
      filter.frequency.setValueAtTime(140, now);
      filter.frequency.exponentialRampToValueAtTime(320, now + 1.2);
      filter.frequency.exponentialRampToValueAtTime(160, now + 2.4);

      // Balina Frekans Kayması (95 Hz -> 310 Hz -> 110 Hz)
      osc1.frequency.setValueAtTime(95, now);
      osc1.frequency.exponentialRampToValueAtTime(310, now + 1.1);
      osc1.frequency.exponentialRampToValueAtTime(180, now + 2.0);
      osc1.frequency.exponentialRampToValueAtTime(260, now + 2.8);
      osc1.frequency.exponentialRampToValueAtTime(110, now + 3.8);

      // İkinci Harmonik (Alt Bas Gövdesi)
      osc2.frequency.setValueAtTime(48, now);
      osc2.frequency.exponentialRampToValueAtTime(155, now + 1.1);
      osc2.frequency.exponentialRampToValueAtTime(55, now + 3.8);

      // Hacim Zarfı
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.35, now + 0.6);
      gain.gain.setValueAtTime(0.35, now + 2.5);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 4.2);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(gain);
      gain.connect(audioCtx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 4.2);
      osc2.stop(now + 4.2);
    } catch (e) {
      console.warn('Balina sesi üretilemedi:', e);
    }
  }

  // 2. Dev Su Sıçratma & Dalga Çarpması Sentezi
  function playWaterCrash(intensity = 1.0) {
    try {
      initAudio();
      if (!audioCtx) return;

      const now = audioCtx.currentTime;
      const bufferSize = audioCtx.sampleRate * 2.2;
      const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
      const output = noiseBuffer.getChannelData(0);

      // Pembe / Beyaz Gürültü Üretimi (Su Kütlesi)
      let b0 = 0, b1 = 0, b2 = 0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        b0 = 0.99886 * b0 + white * 0.0555179;
        b1 = 0.99332 * b1 + white * 0.0750759;
        b2 = 0.96900 * b2 + white * 0.1538520;
        output[i] = (b0 + b1 + b2 + white * 0.5362) * 0.35;
      }

      const whiteNoise = audioCtx.createBufferSource();
      whiteNoise.buffer = noiseBuffer;

      // Alçak Geçiren Filtre (Gürültüyü ağır su çarpmasına dönüştürür)
      const filter = audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.Q.setValueAtTime(5.0, now);
      filter.frequency.setValueAtTime(1400, now);
      filter.frequency.exponentialRampToValueAtTime(120, now + 1.6);

      const gain = audioCtx.createGain();
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.75 * intensity, now + 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 2.0);

      // Derin Su Darbesi (Sub-Bass Thud)
      const subOsc = audioCtx.createOscillator();
      const subGain = audioCtx.createGain();
      subOsc.type = 'sine';
      subOsc.frequency.setValueAtTime(75, now);
      subOsc.frequency.exponentialRampToValueAtTime(32, now + 0.6);

      subGain.gain.setValueAtTime(0.85 * intensity, now);
      subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.8);

      subOsc.connect(subGain);
      subGain.connect(audioCtx.destination);

      whiteNoise.connect(filter);
      filter.connect(gain);
      gain.connect(audioCtx.destination);

      subOsc.start(now);
      whiteNoise.start(now);
      subOsc.stop(now + 0.8);
      whiteNoise.stop(now + 2.1);

      // Su Damlacığı Pıtırtıları (Micro Water Droplet Chirps)
      for (let k = 0; k < 10; k++) {
        const dropTime = now + 0.15 + Math.random() * 0.9;
        const dropOsc = audioCtx.createOscillator();
        const dropGain = audioCtx.createGain();
        dropOsc.type = 'sine';
        dropOsc.frequency.setValueAtTime(900 + Math.random() * 700, dropTime);
        dropOsc.frequency.exponentialRampToValueAtTime(350, dropTime + 0.08);

        dropGain.gain.setValueAtTime(0.12 * intensity, dropTime);
        dropGain.gain.exponentialRampToValueAtTime(0.001, dropTime + 0.08);

        dropOsc.connect(dropGain);
        dropGain.connect(audioCtx.destination);

        dropOsc.start(dropTime);
        dropOsc.stop(dropTime + 0.09);
      }
    } catch (e) {
      console.warn('Su sesi üretilemedi:', e);
    }
  }


  // ==========================================
  // 6. ANİMASYONLU MİTOLOJİK TUVAL (CANVAS)
  // Loraks Truffula Halesi, Transformers Energon Ağları & Yu-Gi-Oh Yıldızları
  // ==========================================
  const canvas = document.getElementById('mythicBgCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = 0, height = 0;

    function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const orbs = [
      { x: 0.2, y: 0.25, r: 240, color: 'rgba(255, 51, 153, 0.09)', vx: 0.0003, vy: 0.0002 },
      { x: 0.8, y: 0.35, r: 280, color: 'rgba(0, 242, 254, 0.09)', vx: -0.0002, vy: 0.0003 },
      { x: 0.45, y: 0.75, r: 260, color: 'rgba(255, 215, 0, 0.08)', vx: 0.0002, vy: -0.0003 },
      { x: 0.7, y: 0.85, r: 220, color: 'rgba(168, 85, 247, 0.09)', vx: -0.0003, vy: -0.0002 }
    ];

    const energonNodes = [];
    const nodeCount = Math.min(22, Math.floor(window.innerWidth / 65));
    for (let i = 0; i < nodeCount; i++) {
      energonNodes.push({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        size: Math.random() * 2.5 + 1.2,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: 0.02 + Math.random() * 0.03
      });
    }

    const stars = [];
    const starCount = Math.min(35, Math.floor(window.innerWidth / 45));
    for (let i = 0; i < starCount; i++) {
      stars.push({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        vy: -0.2 - Math.random() * 0.35,
        size: Math.random() * 2.2 + 0.8,
        twinkle: Math.random() * Math.PI * 2,
        twinkleSpeed: 0.03 + Math.random() * 0.04,
        isGolden: Math.random() > 0.4
      });
    }

    let time = 0;
    function render() {
      if (!document.hidden) {
        time += 0.012;
        ctx.clearRect(0, 0, width, height);

        orbs.forEach(orb => {
          const cx = (orb.x + Math.sin(time * 0.4 + orb.r) * 0.05) * width;
          const cy = (orb.y + Math.cos(time * 0.35 + orb.r) * 0.05) * height;
          const grad = ctx.createRadialGradient(cx, cy, 10, cx, cy, orb.r);
          grad.addColorStop(0, orb.color);
          grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.arc(cx, cy, orb.r, 0, Math.PI * 2);
          ctx.fill();
        });

        for (let i = 0; i < energonNodes.length; i++) {
          const n1 = energonNodes[i];
          n1.x += n1.vx;
          n1.y += n1.vy;
          n1.pulse += n1.pulseSpeed;

          if (n1.x < -10) n1.x = width + 10;
          if (n1.x > width + 10) n1.x = -10;
          if (n1.y < -10) n1.y = height + 10;
          if (n1.y > height + 10) n1.y = -10;

          for (let j = i + 1; j < energonNodes.length; j++) {
            const n2 = energonNodes[j];
            const dx = n1.x - n2.x;
            const dy = n1.y - n2.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 140) {
              const alpha = (1 - dist / 140) * 0.2;
              ctx.strokeStyle = `rgba(0, 242, 254, ${alpha})`;
              ctx.lineWidth = 0.8;
              ctx.beginPath();
              ctx.moveTo(n1.x, n1.y);
              ctx.lineTo(n2.x, n2.y);
              ctx.stroke();
            }
          }

          const glow = 0.4 + 0.4 * Math.sin(n1.pulse);
          ctx.fillStyle = `rgba(0, 242, 254, ${glow})`;
          ctx.beginPath();
          ctx.arc(n1.x, n1.y, n1.size, 0, Math.PI * 2);
          ctx.fill();
        }

        stars.forEach(star => {
          star.y += star.vy;
          star.twinkle += star.twinkleSpeed;
          if (star.y < -10) {
            star.y = height + 10;
            star.x = Math.random() * width;
          }

          const alpha = 0.25 + 0.65 * Math.abs(Math.sin(star.twinkle));
          ctx.fillStyle = star.isGolden ? `rgba(255, 215, 0, ${alpha})` : `rgba(255, 255, 255, ${alpha})`;

          const s = star.size * (0.8 + 0.3 * Math.sin(star.twinkle));
          ctx.beginPath();
          ctx.moveTo(star.x, star.y - s * 2);
          ctx.lineTo(star.x + s * 0.5, star.y);
          ctx.lineTo(star.x + s * 2, star.y);
          ctx.lineTo(star.x + s * 0.5, star.y + s * 0.5);
          ctx.lineTo(star.x, star.y + s * 2);
          ctx.lineTo(star.x - s * 0.5, star.y + s * 0.5);
          ctx.lineTo(star.x - s * 2, star.y);
          ctx.lineTo(star.x - s * 0.5, star.y);
          ctx.closePath();
          ctx.fill();
        });
      }
      requestAnimationFrame(render);
    }
    render();
  }


  // ==========================================
  // 7. GERÇEKÇİ 3B ANATOMİK KELEBEKLER (BUTTERFLIES)
  // Forewing, Hindwing, Damar Desenleri ve Doğal Süzülüş Dinamiği
  // ==========================================
  const butterflyContainer = document.getElementById('butterflyContainer');
  if (butterflyContainer) {
    const butterflyPalettes = [
      { name: 'lorax-pink', f1: '#ff2a85', f2: '#ec4899', h1: '#b5179e', h2: '#7209b7' },
      { name: 'energon-cyan', f1: '#00f2fe', f2: '#0284c7', h1: '#0369a1', h2: '#1e3a8a' },
      { name: 'millennium-gold', f1: '#ffd700', f2: '#f59e0b', h1: '#b45309', h2: '#78350f' },
      { name: 'aurora-emerald', f1: '#00f260', f2: '#10b981', h1: '#047857', h2: '#064e3b' }
    ];

    const butterflies = [];
    const count = Math.min(8, Math.max(5, Math.floor(window.innerWidth / 200)));

    for (let i = 0; i < count; i++) {
      const pal = butterflyPalettes[i % butterflyPalettes.length];
      const el = document.createElement('div');
      el.className = 'butterfly';
      el.style.width = '52px';
      el.style.height = '42px';

      // Gerçekçi Vektör Kelebek Anatomisi (Forewing, Hindwing, Gövde, Antenler)
      el.innerHTML = `
        <div class="butterfly-body">
          <div class="butterfly-antenna-l"></div>
          <div class="butterfly-antenna-r"></div>
        </div>
        <div class="wings-pair wings-left">
          <svg viewBox="0 0 50 60" style="width:100%; height:100%; filter: drop-shadow(0 0 6px ${pal.f1}88);">
            <defs>
              <linearGradient id="fwGradL${i}" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="${pal.f1}"/>
                <stop offset="65%" stop-color="${pal.f2}"/>
                <stop offset="100%" stop-color="#111827"/>
              </linearGradient>
              <linearGradient id="hwGradL${i}" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="${pal.h1}"/>
                <stop offset="70%" stop-color="${pal.h2}"/>
                <stop offset="100%" stop-color="#000"/>
              </linearGradient>
            </defs>
            <!-- Forewing (Ön Kanat) -->
            <path d="M 48 30 C 40 10, 20 2, 6 6 C -2 10, -1 25, 12 36 C 26 46, 42 36, 48 30 Z" fill="url(#fwGradL${i})"/>
            <path d="M 48 30 Q 25 15 8 10 M 48 30 Q 28 28 16 34 M 48 30 Q 35 38 24 42" stroke="rgba(255,255,255,0.4)" stroke-width="0.8" fill="none"/>
            <!-- Hindwing (Arka Kanat) -->
            <path d="M 47 32 C 38 42, 24 56, 12 52 C 2 48, 6 36, 18 32 C 30 28, 42 30, 47 32 Z" fill="url(#hwGradL${i})"/>
            <circle cx="16" cy="46" r="2.5" fill="#fff" opacity="0.8"/>
            <circle cx="10" cy="38" r="1.8" fill="${pal.f1}" opacity="0.9"/>
          </svg>
        </div>
        <div class="wings-pair wings-right">
          <svg viewBox="0 0 50 60" style="width:100%; height:100%; transform: scaleX(-1); filter: drop-shadow(0 0 6px ${pal.f1}88);">
            <!-- Forewing (Ön Kanat) -->
            <path d="M 48 30 C 40 10, 20 2, 6 6 C -2 10, -1 25, 12 36 C 26 46, 42 36, 48 30 Z" fill="url(#fwGradL${i})"/>
            <path d="M 48 30 Q 25 15 8 10 M 48 30 Q 28 28 16 34 M 48 30 Q 35 38 24 42" stroke="rgba(255,255,255,0.4)" stroke-width="0.8" fill="none"/>
            <!-- Hindwing (Arka Kanat) -->
            <path d="M 47 32 C 38 42, 24 56, 12 52 C 2 48, 6 36, 18 32 C 30 28, 42 30, 47 32 Z" fill="url(#hwGradL${i})"/>
            <circle cx="16" cy="46" r="2.5" fill="#fff" opacity="0.8"/>
            <circle cx="10" cy="38" r="1.8" fill="${pal.f1}" opacity="0.9"/>
          </svg>
        </div>
      `;

      butterflyContainer.appendChild(el);

      butterflies.push({
        el: el,
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight * 0.8 + 40,
        vx: (Math.random() > 0.5 ? 1 : -1) * (0.8 + Math.random() * 0.9),
        vy: (Math.random() - 0.5) * 0.6,
        scale: 0.85 + Math.random() * 0.4,
        angle: 0,
        phase: Math.random() * Math.PI * 2,
        flutterFreq: 0.05 + Math.random() * 0.03
      });
    }

    function animateButterflies() {
      if (!document.hidden) {
        const w = window.innerWidth;
        const h = window.innerHeight;

        butterflies.forEach(b => {
          b.phase += b.flutterFreq;
          b.x += b.vx;
          // Gerçekçi Kelebek Çırpınış Salınımı (Bouncy flight dynamics)
          b.y += Math.sin(b.phase) * 2.2 + b.vy;

          if (b.vx > 0 && b.x > w + 60) {
            b.x = -60;
            b.y = Math.random() * h * 0.85 + 40;
          } else if (b.vx < 0 && b.x < -60) {
            b.x = w + 60;
            b.y = Math.random() * h * 0.85 + 40;
          }

          if (b.y < 25) b.y = 25;
          if (b.y > h - 80) b.y = h - 80;

          const targetAngle = b.vx > 0 ? (b.vy * 20 + Math.sin(b.phase) * 16) : (180 - (b.vy * 20 + Math.sin(b.phase) * 16));
          b.angle += (targetAngle - b.angle) * 0.1;

          b.el.style.transform = `translate3d(${b.x}px, ${b.y}px, 0) rotate(${b.angle}deg) scale(${b.scale})`;
        });
      }
      requestAnimationFrame(animateButterflies);
    }
    requestAnimationFrame(animateButterflies);
  }


  // ==========================================
  // 8. GERÇEKÇİ KAMBUR BALİNA (HUMPBACK WHALE),
  // DEV SU SIÇRATMASI & YÜZÜ ISLATACAK EKRAN DAMLACIKLARI
  // ==========================================
  const whaleContainer = document.getElementById('whaleContainer');
  const screenSplashOverlay = document.getElementById('screenSplashOverlay');
  const summonWhaleBtn = document.getElementById('summonWhaleBtn');
  let isWhaleJumping = false;

  // Gerçekçi Kambur Balina (Humpback Whale) Vektör Çizimi
  if (whaleContainer && !document.getElementById('whaleActor')) {
    const actor = document.createElement('div');
    actor.id = 'whaleActor';
    actor.className = 'whale-actor';
    actor.style.width = '260px';
    actor.style.height = '160px';

    actor.innerHTML = `
      <div id="blowholeSpray" class="blowhole-plume">
        <svg viewBox="0 0 40 80" style="width:100%; height:100%;">
          <defs>
            <linearGradient id="sprayGrad" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stop-color="rgba(255,255,255,0.95)"/>
              <stop offset="70%" stop-color="rgba(186,230,253,0.7)"/>
              <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
            </linearGradient>
          </defs>
          <path d="M 20 80 Q 8 40 4 10 Q 14 2 20 0 Q 26 2 36 10 Q 32 40 20 80 Z" fill="url(#sprayGrad)"/>
          <circle cx="12" cy="18" r="3.5" fill="#fff" opacity="0.8"/>
          <circle cx="28" cy="14" r="4" fill="#fff" opacity="0.85"/>
          <circle cx="20" cy="6" r="3" fill="#bae6fd" opacity="0.9"/>
        </svg>
      </div>

      <svg viewBox="0 0 360 200" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%; filter: drop-shadow(0 10px 24px rgba(0, 114, 255, 0.65));">
        <defs>
          <linearGradient id="whaleBackGrad" x1="0%" y1="0%" x2="100%" y2="60%">
            <stop offset="0%" stop-color="#0f172a"/>
            <stop offset="40%" stop-color="#1e293b"/>
            <stop offset="75%" stop-color="#0369a1"/>
            <stop offset="100%" stop-color="#00f2fe"/>
          </linearGradient>
          <linearGradient id="whaleThroatGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="50%" stop-color="#cbd5e1"/>
            <stop offset="100%" stop-color="#64748b"/>
          </linearGradient>
          <linearGradient id="whaleFinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0284c7"/>
            <stop offset="80%" stop-color="#f1f5f9"/>
            <stop offset="100%" stop-color="#ffffff"/>
          </linearGradient>
        </defs>

        <!-- Humpback Dorsal Body (Kambur Balina Gövdesi & Karakteristik Kambur) -->
        <path d="M 45 110 C 65 55, 140 35, 230 45 C 275 52, 315 78, 345 105 C 325 112, 280 120, 240 135 C 175 160, 95 165, 45 110 Z" fill="url(#whaleBackGrad)"/>
        
        <!-- Dorsal Fin (Küçük Kambur Yüzgeci) -->
        <path d="M 125 45 C 115 28, 105 22, 98 24 C 102 34, 110 40, 118 46 Z" fill="#0f172a"/>

        <!-- Ventral Throat Pleats (Gerçekçi Genleşen Boğaz Yivleri) -->
        <path d="M 130 118 C 175 152, 240 148, 295 115 C 245 130, 180 130, 130 118 Z" fill="url(#whaleThroatGrad)"/>
        <!-- Boğaz Yiv Çizgileri -->
        <path d="M 140 124 Q 210 144 280 120" stroke="#94a3b8" stroke-width="1.2" fill="none" opacity="0.85"/>
        <path d="M 155 130 Q 215 147 270 126" stroke="#94a3b8" stroke-width="1.2" fill="none" opacity="0.85"/>
        <path d="M 175 136 Q 220 150 260 132" stroke="#94a3b8" stroke-width="1" fill="none" opacity="0.8"/>

        <!-- Knobby Tubercles (Kafadaki Tüberküller / Yumrular) -->
        <circle cx="330" cy="94" r="3" fill="#cbd5e1" opacity="0.9"/>
        <circle cx="316" cy="85" r="3.2" fill="#cbd5e1" opacity="0.9"/>
        <circle cx="298" cy="74" r="3" fill="#cbd5e1" opacity="0.85"/>
        <circle cx="280" cy="66" r="3" fill="#cbd5e1" opacity="0.85"/>
        <circle cx="260" cy="58" r="2.8" fill="#cbd5e1" opacity="0.8"/>
        <!-- Çene Yumruları -->
        <circle cx="338" cy="106" r="2.8" fill="#e2e8f0"/>
        <circle cx="320" cy="115" r="2.8" fill="#e2e8f0"/>
        <circle cx="300" cy="122" r="2.8" fill="#e2e8f0"/>

        <!-- Göz -->
        <circle cx="282" cy="92" r="3.8" fill="#000"/>
        <circle cx="283" cy="91" r="1.4" fill="#fff"/>
        <circle cx="282" cy="92" r="6" stroke="#38bdf8" stroke-width="1.2" fill="none" opacity="0.85"/>

        <!-- Giant Wing-like Pectoral Fin (Dev Kambur Yan Yüzgeci - Beyaz Tırtıklı Kenarlar) -->
        <path d="M 185 118 C 220 155, 235 190, 215 195 C 198 192, 185 165, 165 125 Z" fill="url(#whaleFinGrad)"/>
        <!-- Tırtıklı Yüzgeç Uçları -->
        <circle cx="225" cy="185" r="2.5" fill="#fff"/>
        <circle cx="218" cy="192" r="2.5" fill="#fff"/>
        <circle cx="210" cy="194" r="2.5" fill="#fff"/>

        <!-- Fluked Tail (Geniş Çentikli Kuyruk Yüzgeci) -->
        <path d="M 50 112 C 34 96, 12 76, 4 60 C 14 84, 28 102, 42 110 C 26 116, 10 134, 4 158 C 14 145, 34 126, 50 115 Z" fill="url(#whaleBackGrad)"/>
        <!-- Kuyruk Beyaz Alt Deseni -->
        <path d="M 38 110 Q 18 92 10 74 Q 24 96 36 108 Z" fill="#e2e8f0" opacity="0.85"/>
        <path d="M 38 112 Q 18 130 10 146 Q 24 128 36 114 Z" fill="#e2e8f0" opacity="0.85"/>
      </svg>
    `;

    whaleContainer.appendChild(actor);
  }

  // Yüzü Islatacak Ekran Su Sıçratması (Screen Splash & Glass Droplets)
  function spawnScreenWaterSplash() {
    if (!screenSplashOverlay) return;

    // 1. Kamera Camı Buğulanması (Screen Mist Wash)
    const mist = document.createElement('div');
    mist.className = 'screen-splash-mist';
    screenSplashOverlay.appendChild(mist);
    setTimeout(() => mist.remove(), 1900);

    // 2. 35 Adet Gerçekçi Sıvı Cam Damlası (Screen Water Droplets)
    const dropCount = Math.floor(Math.random() * 10) + 32;
    for (let i = 0; i < dropCount; i++) {
      const drop = document.createElement('div');
      drop.className = 'screen-water-drop';

      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight * 0.85;
      const size = 10 + Math.random() * 22; // 10px - 32px arası dev damlalar
      const dripDist = 45 + Math.random() * 115; // Aşağı akış mesafesi

      drop.style.left = `${x}px`;
      drop.style.top = `${y}px`;
      drop.style.width = `${size}px`;
      drop.style.height = `${size * (1 + Math.random() * 0.35)}px`;
      drop.style.setProperty('--drip-dist', `${dripDist}px`);
      drop.style.animationDelay = `${Math.random() * 0.25}s`;

      screenSplashOverlay.appendChild(drop);
      setTimeout(() => drop.remove(), 3800);

      // Ana damlanın etrafına küçük mikro sıçrama zerreleri
      for (let s = 0; s < 3; s++) {
        const micro = document.createElement('div');
        micro.className = 'screen-micro-drop';
        const mSize = 3 + Math.random() * 5;
        micro.style.left = `${x + (Math.random() - 0.5) * 45}px`;
        micro.style.top = `${y + (Math.random() - 0.5) * 45}px`;
        micro.style.width = `${mSize}px`;
        micro.style.height = `${mSize}px`;
        micro.style.animationDelay = `${Math.random() * 0.2}s`;
        screenSplashOverlay.appendChild(micro);
        setTimeout(() => micro.remove(), 2500);
      }
    }
  }

  // Deniz İçi Parçacık Sıçratma (Ocean Waves, Foam & 60+ Droplets)
  function spawnOceanWaterSplash(centerXPercent, bottomPx, count = 35) {
    if (!whaleContainer) return;
    const containerW = whaleContainer.offsetWidth || window.innerWidth;
    const originX = (containerW * centerXPercent) / 100;

    // Genişleyen Çok Katmanlı Su Halkaları
    for (let r = 0; r < 2; r++) {
      setTimeout(() => {
        const ring = document.createElement('div');
        ring.className = 'water-ring';
        ring.style.left = `${originX - 15}px`;
        ring.style.bottom = `${bottomPx}px`;
        ring.style.width = `${30 + r * 20}px`;
        ring.style.height = `${12 + r * 6}px`;
        whaleContainer.appendChild(ring);
        setTimeout(() => ring.remove(), 1600);
      }, r * 180);
    }

    // 40+ Adet Dinamik Parabolik Su Damlacığı
    for (let i = 0; i < count; i++) {
      const drop = document.createElement('div');
      drop.className = 'splash-droplet';
      drop.style.left = `${originX}px`;
      drop.style.bottom = `${bottomPx + 8}px`;

      const angle = (Math.PI / 180) * (20 + Math.random() * 140);
      const distance = 60 + Math.random() * 140;
      const dx = Math.cos(angle) * distance * (Math.random() > 0.5 ? 1 : -1);
      const dy = -Math.sin(angle) * distance;

      drop.style.setProperty('--dx', `${dx}px`);
      drop.style.setProperty('--dy', `${dy}px`);
      drop.style.width = `${5 + Math.random() * 6}px`;
      drop.style.height = `${5 + Math.random() * 6}px`;

      whaleContainer.appendChild(drop);
      setTimeout(() => drop.remove(), 1350);
    }
  }

  // Balinayı Zıplatma Fonksiyonu
  function triggerWhaleBreach() {
    const actor = document.getElementById('whaleActor');
    if (!actor || isWhaleJumping) return;

    isWhaleJumping = true;
    actor.classList.remove('jumping');
    void actor.offsetWidth;
    actor.classList.add('jumping');

    // 1. ÇIKIŞ ANI: Su Yüzeyini Yarma, Çıkış Sıçraması & Hafif Su Sesi
    setTimeout(() => {
      spawnOceanWaterSplash(10, 15, 30);
      playWaterCrash(0.65);
    }, 150);

    // 2. YÜKSELİŞ & TEPE NOKTASI: Balina Şarkısı & Su Püskürtme (Blowhole)
    setTimeout(() => {
      playWhaleSong();
      const spray = document.getElementById('blowholeSpray');
      if (spray) {
        spray.classList.remove('spraying');
        void spray.offsetWidth;
        spray.classList.add('spraying');
      }
      spawnOceanWaterSplash(42, 140, 20);
    }, 1800);

    // 3. İNİŞ & ÇARPMA ANI: DEV DALGA, GÜRLEYEN SU ÇARPMASI & EKRANI ISLATAN DAMLACIKLAR!
    setTimeout(() => {
      spawnOceanWaterSplash(76, 20, 50);
      playWaterCrash(1.0);
      spawnScreenWaterSplash(); // Yüzü ıslatacak ekran damlacıkları!
    }, 3350);

    // 4. Bitiş ve Hazır Olma
    setTimeout(() => {
      actor.classList.remove('jumping');
      isWhaleJumping = false;
    }, 4500);
  }

  // Balina Düğmesine Tıklama
  if (summonWhaleBtn) {
    summonWhaleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      initAudio();
      triggerWhaleBreach();
      showToast('🌊 Kambur balina havalandı, ekranınız sırılsıklam oldu! 🐋');
    });
  }

  // Otomatik Periyodik Atlama (Her 26 saniyede bir)
  setInterval(() => {
    if (!document.hidden && !isWhaleJumping) {
      triggerWhaleBreach();
    }
  }, 26000);

  // Sayfa açıldıktan 4 saniye sonra ilk görkemli atlayış
  setTimeout(() => {
    if (!document.hidden) triggerWhaleBreach();
  }, 4000);

});
