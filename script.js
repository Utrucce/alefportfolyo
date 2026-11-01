/**
 * ALΣF Portal & Privacy Script V3
 * Sertan Çubukcu (sertancubukcu@gmail.com)
 * 
 * Özellikler:
 * 1. Dil Seçici (TR / EN / İkisi)
 * 2. Ekran Görüntüleri Rayı & Lightbox Büyütücü
 * 3. Bildirim & E-posta Kopyalama
 * 4. Web Audio API Okyanus Kambur Balina Çağrısı & Dev Su Çarpma Sesi
 * 5. Animasyonlu Mitolojik Tuval (Loraks, Transformers Energon, Yu-Gi-Oh Yıldızları)
 * 6. 3B WebGL Eterik Kelebekler Motoru (Three.js 3D Morfo & Kırlangıçkuyruk Kelebekleri)
 * 7. 3B WebGL Kambur Balina Motoru (Three.js 3D Humpback Whale & Ocean Breach)
 * 8. Gerçekçi Optik Cam Islanması & Su Damlaları (RainyDay.js + Fiziksel Su Lensi)
 * 9. Etkileşimli Balina Sıçratma Butonu & Otomatik Periyodik Atlama
 */

// ==========================================
// 1. DİL SEÇİCİ (TR / EN / İKİSİ)
// ==========================================
function initLanguage() {
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
}


// ==========================================
// 2. EKRAN GÖRÜNTÜLERİ KAYDIRMA RAYI & LIGHTBOX
// ==========================================
function initScreenshotsAndLightbox() {
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
}


// ==========================================
// 3. BİLDİRİM & KOPYALAMA İŞLEMLERİ
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

function initCopyActions() {
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
}


// ==========================================
// 4. SES MOTORU (WEB AUDIO API)
// ==========================================
let audioCtx = null;
function initAudio() {
  if (!audioCtx) {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (AudioContextClass) audioCtx = new AudioContextClass();
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}
document.addEventListener('click', initAudio, { once: true });
document.addEventListener('touchstart', initAudio, { once: true });

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
    filter.type = 'bandpass';
    filter.Q.setValueAtTime(4.8, now);
    filter.frequency.setValueAtTime(130, now);
    filter.frequency.exponentialRampToValueAtTime(330, now + 1.2);
    filter.frequency.exponentialRampToValueAtTime(150, now + 2.5);

    osc1.frequency.setValueAtTime(90, now);
    osc1.frequency.exponentialRampToValueAtTime(320, now + 1.1);
    osc1.frequency.exponentialRampToValueAtTime(175, now + 2.0);
    osc1.frequency.exponentialRampToValueAtTime(280, now + 2.8);
    osc1.frequency.exponentialRampToValueAtTime(105, now + 4.0);

    osc2.frequency.setValueAtTime(45, now);
    osc2.frequency.exponentialRampToValueAtTime(160, now + 1.1);
    osc2.frequency.exponentialRampToValueAtTime(50, now + 4.0);

    gain.gain.setValueAtTime(0.001, now);
    gain.gain.linearRampToValueAtTime(0.38, now + 0.6);
    gain.gain.setValueAtTime(0.38, now + 2.6);
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

function playWaterCrash(intensity = 1.0) {
  try {
    initAudio();
    if (!audioCtx) return;
    const now = audioCtx.currentTime;
    const bufferSize = audioCtx.sampleRate * 2.2;
    const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const output = noiseBuffer.getChannelData(0);

    let b0 = 0, b1 = 0, b2 = 0;
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      b0 = 0.99886 * b0 + white * 0.0555179;
      b1 = 0.99332 * b1 + white * 0.0750759;
      b2 = 0.96900 * b2 + white * 0.1538520;
      output[i] = (b0 + b1 + b2 + white * 0.5362) * 0.38;
    }

    const whiteNoise = audioCtx.createBufferSource();
    whiteNoise.buffer = noiseBuffer;

    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.Q.setValueAtTime(5.5, now);
    filter.frequency.setValueAtTime(1500, now);
    filter.frequency.exponentialRampToValueAtTime(110, now + 1.7);

    const gain = audioCtx.createGain();
    gain.gain.setValueAtTime(0.001, now);
    gain.gain.linearRampToValueAtTime(0.85 * intensity, now + 0.06);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 2.2);

    const subOsc = audioCtx.createOscillator();
    const subGain = audioCtx.createGain();
    subOsc.type = 'sine';
    subOsc.frequency.setValueAtTime(70, now);
    subOsc.frequency.exponentialRampToValueAtTime(28, now + 0.7);

    subGain.gain.setValueAtTime(0.95 * intensity, now);
    subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.85);

    subOsc.connect(subGain);
    subGain.connect(audioCtx.destination);

    whiteNoise.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);

    subOsc.start(now);
    whiteNoise.start(now);
    subOsc.stop(now + 0.85);
    whiteNoise.stop(now + 2.2);
  } catch (e) {
    console.warn('Su sesi üretilemedi:', e);
  }
}


// ==========================================

function playThunderSound() {
  try {
    initAudio();
    if (!audioCtx) return;
    const now = audioCtx.currentTime;

    // 1. Initial Sharp Crack
    const crackBuffer = audioCtx.createBuffer(1, audioCtx.sampleRate * 0.4, audioCtx.sampleRate);
    const crackData = crackBuffer.getChannelData(0);
    for (let i = 0; i < crackData.length; i++) {
      crackData[i] = (Math.random() * 2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.08));
    }
    const crackSource = audioCtx.createBufferSource();
    crackSource.buffer = crackBuffer;
    const crackFilter = audioCtx.createBiquadFilter();
    crackFilter.type = 'bandpass';
    crackFilter.frequency.setValueAtTime(600, now);
    crackFilter.frequency.exponentialRampToValueAtTime(180, now + 0.35);
    crackFilter.Q.setValueAtTime(3.5, now);
    const crackGain = audioCtx.createGain();
    crackGain.gain.setValueAtTime(0.75, now);
    crackGain.gain.exponentialRampToValueAtTime(0.001, now + 0.38);
    crackSource.connect(crackFilter);
    crackFilter.connect(crackGain);
    crackGain.connect(audioCtx.destination);
    crackSource.start(now);

    // 2. Deep Rolling Thunder Rumble (3.5 saniye)
    const rumbleLen = audioCtx.sampleRate * 3.5;
    const rumbleBuffer = audioCtx.createBuffer(1, rumbleLen, audioCtx.sampleRate);
    const rumbleData = rumbleBuffer.getChannelData(0);
    let last = 0;
    for (let i = 0; i < rumbleLen; i++) {
      const white = Math.random() * 2 - 1;
      last = (last + (0.02 * white)) / 1.02;
      rumbleData[i] = last * 3.5;
    }
    const rumbleSource = audioCtx.createBufferSource();
    rumbleSource.buffer = rumbleBuffer;
    const rumbleFilter = audioCtx.createBiquadFilter();
    rumbleFilter.type = 'lowpass';
    rumbleFilter.frequency.setValueAtTime(140, now);
    rumbleFilter.frequency.linearRampToValueAtTime(85, now + 2.0);
    rumbleFilter.frequency.linearRampToValueAtTime(45, now + 3.5);
    const rumbleGain = audioCtx.createGain();
    rumbleGain.gain.setValueAtTime(0.001, now);
    rumbleGain.gain.linearRampToValueAtTime(0.9, now + 0.15);
    rumbleGain.gain.exponentialRampToValueAtTime(0.3, now + 1.8);
    rumbleGain.gain.exponentialRampToValueAtTime(0.001, now + 3.5);

    // Sub-bass resonance (48Hz -> 24Hz)
    const subOsc = audioCtx.createOscillator();
    const subGain = audioCtx.createGain();
    subOsc.type = 'triangle';
    subOsc.frequency.setValueAtTime(48, now);
    subOsc.frequency.exponentialRampToValueAtTime(24, now + 2.5);
    subGain.gain.setValueAtTime(0.4, now);
    subGain.gain.exponentialRampToValueAtTime(0.001, now + 2.5);
    subOsc.connect(subGain);
    subGain.connect(audioCtx.destination);
    subOsc.start(now);
    subOsc.stop(now + 2.5);

    rumbleSource.connect(rumbleFilter);
    rumbleFilter.connect(rumbleGain);
    rumbleGain.connect(audioCtx.destination);
    rumbleSource.start(now);
    rumbleSource.stop(now + 3.5);
  } catch (e) {
    console.warn('Gök gürültüsü üretilemedi:', e);
  }
}

// 5. ANİMASYONLU MİTOLOJİK TUVAL (CANVAS)
// ==========================================
function initMythicBgCanvas() {
  const canvas = document.getElementById('mythicBgCanvas');
  if (!canvas) return;
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
// ==========================================
// 6. UÇUŞAN 3B FOTOĞRAFİK KELEBEKLER MOTORU
// (Kullanıcı Talebi: Orijinal Wikimedia Morfo Kanatları ile 3B Çırpınma)
// ==========================================
function initPhotographicButterflies() {
  const container = document.getElementById('butterflyContainer');
  if (!container) return;

  const butterflyTypes = [
    { left: 'assets/real_wing_left_blue.png', right: 'assets/real_wing_right_blue.png' },
    { left: 'assets/real_wing_left_emerald.png', right: 'assets/real_wing_right_emerald.png' },
    { left: 'assets/real_wing_left_gold.png', right: 'assets/real_wing_right_gold.png' },
    { left: 'assets/real_wing_left_purple.png', right: 'assets/real_wing_right_purple.png' }
  ];

  const butterflies = [];
  const count = Math.min(8, Math.max(5, Math.floor(window.innerWidth / 200)));

  for (let i = 0; i < count; i++) {
    const type = butterflyTypes[i % butterflyTypes.length];
    const el = document.createElement('div');
    el.className = 'real-butterfly';
    el.innerHTML = `
      <div class="butterfly-3d-wrap">
        <div class="wing-3d wing-left">
          <img src="${type.left}" alt="Sol Kanat" loading="lazy">
        </div>
        <div class="wing-3d wing-right">
          <img src="${type.right}" alt="Sağ Kanat" loading="lazy">
        </div>
      </div>
    `;
    container.appendChild(el);

    butterflies.push({
      el: el,
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight * 0.8 + 40,
      vx: (Math.random() > 0.5 ? 1 : -1) * (0.85 + Math.random() * 0.95),
      vy: (Math.random() - 0.5) * 0.6,
      scale: 0.85 + Math.random() * 0.35,
      angle: 0,
      phase: Math.random() * Math.PI * 2,
      flutterFreq: 0.045 + Math.random() * 0.03
    });
  }

  function animateButterflies() {
    if (!document.hidden) {
      const w = window.innerWidth;
      const h = window.innerHeight;

      butterflies.forEach(b => {
        b.phase += b.flutterFreq;
        b.x += b.vx;
        b.y += Math.sin(b.phase) * 2.0 + b.vy;

        if (b.vx > 0 && b.x > w + 70) {
          b.x = -70;
          b.y = Math.random() * h * 0.85 + 40;
        } else if (b.vx < 0 && b.x < -70) {
          b.x = w + 70;
          b.y = Math.random() * h * 0.85 + 40;
        }

        if (b.y < 25) b.y = 25;
        if (b.y > h - 80) b.y = h - 80;

        const targetAngle = b.vx > 0 ? (b.vy * 22 + Math.sin(b.phase) * 14) : (180 - (b.vy * 22 + Math.sin(b.phase) * 14));
        b.angle += (targetAngle - b.angle) * 0.1;

        b.el.style.transform = `translate3d(${b.x}px, ${b.y}px, 0) rotate(${b.angle}deg) scale(${b.scale})`;
      });
    }
    requestAnimationFrame(animateButterflies);
  }
  requestAnimationFrame(animateButterflies);
}

// ==========================================
// 7. EKRANIN ALTINDA DALGALI OKYANUS MOTORU
// (Kullanıcı Talebi: Ekranın altı dalgalı okyanus, kaydıkça kaysın)
// ==========================================
function initOceanWaves() {
  const ocean = document.getElementById('oceanWavesCanvas');
  if (!ocean) return;
  const ctx = ocean.getContext('2d');
  let oWidth = 0, oHeight = 0;

  function resizeOcean() {
    oWidth = ocean.width = window.innerWidth;
    oHeight = ocean.height = 190;
  }
  resizeOcean();
  window.addEventListener('resize', resizeOcean);

  let scrollOffset = 0;
  window.addEventListener('scroll', () => {
    scrollOffset = window.scrollY * 0.12;
  });

  let waveTime = 0;
  function renderWaves() {
    waveTime += 0.02;
    ctx.clearRect(0, 0, oWidth, oHeight);

    // Dalga 1: Derin Okyanus (Arka katman)
    ctx.beginPath();
    ctx.moveTo(0, oHeight);
    for (let x = 0; x <= oWidth; x += 10) {
      const y = 80 + Math.sin(x * 0.008 + waveTime * 0.8) * 18 + Math.cos(x * 0.004 + waveTime * 0.5) * 12 + Math.sin(scrollOffset * 0.05) * 6;
      ctx.lineTo(x, y);
    }
    ctx.lineTo(oWidth, oHeight);
    ctx.closePath();
    const grad1 = ctx.createLinearGradient(0, 50, 0, oHeight);
    grad1.addColorStop(0, 'rgba(3, 105, 161, 0.55)');
    grad1.addColorStop(1, 'rgba(7, 24, 48, 0.95)');
    ctx.fillStyle = grad1;
    ctx.fill();

    // Dalga 2: Orta Okyanus Akıntısı
    ctx.beginPath();
    ctx.moveTo(0, oHeight);
    for (let x = 0; x <= oWidth; x += 10) {
      const y = 100 + Math.sin(x * 0.012 - waveTime * 1.1) * 14 + Math.sin(x * 0.02 + waveTime * 1.5) * 8;
      ctx.lineTo(x, y);
    }
    ctx.lineTo(oWidth, oHeight);
    ctx.closePath();
    const grad2 = ctx.createLinearGradient(0, 70, 0, oHeight);
    grad2.addColorStop(0, 'rgba(0, 242, 254, 0.45)');
    grad2.addColorStop(1, 'rgba(10, 37, 64, 0.95)');
    ctx.fillStyle = grad2;
    ctx.fill();

    // Dalga 3: Ön Köpüklü Tepe Dalgası
    ctx.beginPath();
    ctx.moveTo(0, oHeight);
    for (let x = 0; x <= oWidth; x += 8) {
      const y = 115 + Math.sin(x * 0.015 + waveTime * 1.4) * 12 + Math.cos(x * 0.009 - waveTime * 0.9) * 10;
      ctx.lineTo(x, y);
    }
    ctx.lineTo(oWidth, oHeight);
    ctx.closePath();
    const grad3 = ctx.createLinearGradient(0, 90, 0, oHeight);
    grad3.addColorStop(0, 'rgba(56, 189, 248, 0.85)');
    grad3.addColorStop(1, 'rgba(5, 16, 30, 0.98)');
    ctx.fillStyle = grad3;
    ctx.fill();

    // Köpük Çizgisi (Beyaz/Siyan Tepe Işıltısı)
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.85)';
    ctx.beginPath();
    for (let x = 0; x <= oWidth; x += 8) {
      const y = 115 + Math.sin(x * 0.015 + waveTime * 1.4) * 12 + Math.cos(x * 0.009 - waveTime * 0.9) * 10;
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    requestAnimationFrame(renderWaves);
  }
  renderWaves();
}

// ==========================================
// 8. ŞİMŞEK ÇAKMASI VE GÖK GÜRÜLTÜSÜ MOTORU
// (Kullanıcı Talebi: Arada şimşek çaksın sesli olarak)
// ==========================================
function triggerLightning() {
  const overlay = document.getElementById('lightningFlashOverlay');
  if (!overlay) return;

  // Aşama 1: Ön Çakma (60ms)
  overlay.style.opacity = '0.55';
  setTimeout(() => {
    overlay.style.opacity = '0.1';
    // Aşama 2: Ana Güçlü Yıldırım (110ms)
    setTimeout(() => {
      overlay.style.opacity = '0.95';
      playThunderSound();
      setTimeout(() => {
        overlay.style.opacity = '0.35';
        // Aşama 3: Sönüm
        setTimeout(() => {
          overlay.style.opacity = '0';
        }, 180);
      }, 90);
    }, 50);
  }, 60);
}

// ==========================================
// 9. 3B WEBGL KAMBUR BALİNA MOTORU (THREE.JS 3D HUMPBACK WHALE)
// (Kullanıcı Talepleri: Bir tık küçük yap; burun, ağız ve gözleri gerçekçi yap)
// ==========================================
class WhaleThreeEngine {
  constructor(canvas) {
    this.canvas = canvas;
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.isBreaching = false;
    this.breachTime = 0;
    this.breachDuration = 4.6;
    this.hasSprayedBlowhole = false;
    this.hasImpactedWater = false;
    this.lastTime = performance.now();

    this.initScene();
    this.buildWhale();
    this.buildWaterParticles();
    this.bindEvents();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  initScene() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(42, this.width / this.height, 0.1, 1000);
    this.camera.position.set(0, 4, 30);
    this.camera.lookAt(0, 2, 0);

    this.renderer = new THREE.WebGLRenderer({ canvas: this.canvas, antialias: true, alpha: true });
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const sunLight = new THREE.DirectionalLight(0xfff8ee, 2.8);
    sunLight.position.set(12, 22, 16);
    this.scene.add(sunLight);

    const rimLight = new THREE.DirectionalLight(0x00f2fe, 1.8);
    rimLight.position.set(-16, -10, -10);
    this.scene.add(rimLight);

    const oceanAmbient = new THREE.AmbientLight(0x224466, 1.4);
    this.scene.add(oceanAmbient);
  }

  buildWhale() {
    this.whaleGroup = new THREE.Group();

    const numRings = 28;
    const numSegs = 24;
    const positions = [];
    const colors = [];
    const indices = [];

    function getStation(u) {
      let w, h, yOff;
      if (u < 0.2) {
        const t = u / 0.2;
        w = 0.5 + t * 2.5;
        h = 0.4 + t * 1.4;
        yOff = 0.1 * t;
      } else if (u < 0.45) {
        const t = (u - 0.2) / 0.25;
        w = 3.0 + (1 - (t - 0.5) * (t - 0.5) * 4) * 0.8;
        h = 1.8 + t * 1.3;
        yOff = -0.3 * t;
      } else if (u < 0.8) {
        const t = (u - 0.45) / 0.35;
        w = 3.4 * (1 - t * 0.65);
        h = 3.1 * (1 - t * 0.68);
        yOff = -0.3 * (1 - t);
      } else {
        const t = (u - 0.8) / 0.2;
        w = 1.2 * (1 - t * 0.65);
        h = 1.0 * (1 - t * 0.68);
        yOff = 0.1 * t;
      }
      const z = 11 - u * 23;
      return { w, h, yOff, z };
    }

    for (let r = 0; r <= numRings; r++) {
      const u = r / numRings;
      const st = getStation(u);

      for (let s = 0; s <= numSegs; s++) {
        const theta = (s / numSegs) * Math.PI * 2;
        let x = st.w * Math.sin(theta);
        let y = st.yOff + st.h * Math.cos(theta);
        const z = st.z;

        // Ventral throat pleats
        if (Math.cos(theta) < -0.15 && u > 0.08 && u < 0.6) {
          y += Math.cos(theta * 28) * 0.06;
        }

        positions.push(x, y, z);

        // Countershading
        if (Math.cos(theta) < -0.15) {
          colors.push(0.92, 0.95, 0.98);
        } else {
          colors.push(0.08, 0.13, 0.20);
        }
      }
    }

    for (let r = 0; r < numRings; r++) {
      for (let s = 0; s < numSegs; s++) {
        const i1 = r * (numSegs + 1) + s;
        const i2 = (r + 1) * (numSegs + 1) + s;
        const i3 = (r + 1) * (numSegs + 1) + (s + 1);
        const i4 = r * (numSegs + 1) + (s + 1);
        indices.push(i1, i2, i4);
        indices.push(i2, i3, i4);
      }
    }

    const bodyGeo = new THREE.BufferGeometry();
    bodyGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    bodyGeo.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
    bodyGeo.setIndex(indices);
    bodyGeo.computeVertexNormals();

    const bodyMat = new THREE.MeshStandardMaterial({
      vertexColors: true,
      roughness: 0.18,
      metalness: 0.15,
      side: THREE.DoubleSide
    });
    this.bodyMesh = new THREE.Mesh(bodyGeo, bodyMat);
    this.whaleGroup.add(this.bodyMesh);

    // --- ANATOMİK YÜZ VE BAŞ DETAYLARI ---
    const skinMat = new THREE.MeshStandardMaterial({ color: 0x111c29, roughness: 0.2, metalness: 0.12 });
    const knobMat = new THREE.MeshStandardMaterial({ color: 0x182637, roughness: 0.25, metalness: 0.1 });

    // 1. Burun / Nefes Deliği Siperi (Blowhole Splash-Guard Crest & Dual Nostrils)
    const blowholeCrestGeo = new THREE.SphereGeometry(0.35, 12, 12);
    const blowholeCrest = new THREE.Mesh(blowholeCrestGeo, skinMat);
    blowholeCrest.scale.set(0.85, 0.45, 1.45);
    blowholeCrest.position.set(0, 1.48, 6.75);
    this.whaleGroup.add(blowholeCrest);

    // İkili Nefes Deliği Yarıkları
    const nostrilMat = new THREE.MeshBasicMaterial({ color: 0x040608 });
    const nostrilGeo = new THREE.SphereGeometry(0.08, 8, 8);
    const nostrilL = new THREE.Mesh(nostrilGeo, nostrilMat);
    nostrilL.scale.set(0.5, 0.3, 1.6);
    nostrilL.position.set(0.14, 1.55, 6.8);
    nostrilL.rotation.y = -0.15;
    this.whaleGroup.add(nostrilL);

    const nostrilR = new THREE.Mesh(nostrilGeo, nostrilMat);
    nostrilR.scale.set(0.5, 0.3, 1.6);
    nostrilR.position.set(-0.14, 1.55, 6.8);
    nostrilR.rotation.y = 0.15;
    this.whaleGroup.add(nostrilR);

    // 2. Burun Sırtı Duyusal Tüberkülleri (Rostrum Tubercles / Knobs)
    const tubercleCoords = [
      [0, 1.32, 7.8, 0.10],
      [0, 1.08, 8.5, 0.10],
      [0, 0.82, 9.2, 0.09],
      [0, 0.58, 9.8, 0.09],
      [0, 0.32, 10.4, 0.08],
      [0.35, 1.18, 8.0, 0.08],
      [-0.35, 1.18, 8.0, 0.08],
      [0.45, 0.90, 8.8, 0.08],
      [-0.45, 0.90, 8.8, 0.08],
      [0.40, 0.62, 9.6, 0.07],
      [-0.40, 0.62, 9.6, 0.07]
    ];
    tubercleCoords.forEach(([tx, ty, tz, tr]) => {
      const knobGeo = new THREE.SphereGeometry(tr, 8, 8);
      const knobMesh = new THREE.Mesh(knobGeo, knobMat);
      knobMesh.position.set(tx, ty, tz);
      this.whaleGroup.add(knobMesh);
    });

    // 3. Ağız & Alt Çene Ucu Tüberkülü (Symphyseal Knob)
    const chinKnobGeo = new THREE.SphereGeometry(0.18, 10, 10);
    const chinKnobMat = new THREE.MeshStandardMaterial({ color: 0xe6eef8, roughness: 0.25, metalness: 0.1 });
    const chinKnob = new THREE.Mesh(chinKnobGeo, chinKnobMat);
    chinKnob.scale.set(1.1, 0.85, 1.2);
    chinKnob.position.set(0, -0.38, 10.75);
    this.whaleGroup.add(chinKnob);

    // Alt çene kenar yumruları
    const jawKnobs = [
      [0.45, -0.42, 9.8, 0.08],
      [-0.45, -0.42, 9.8, 0.08],
      [0.85, -0.55, 8.6, 0.09],
      [-0.85, -0.55, 8.6, 0.09],
      [1.25, -0.70, 7.4, 0.09],
      [-1.25, -0.70, 7.4, 0.09]
    ];
    jawKnobs.forEach(([jx, jy, jz, jr]) => {
      const jKnob = new THREE.Mesh(new THREE.SphereGeometry(jr, 8, 8), chinKnobMat);
      jKnob.position.set(jx, jy, jz);
      this.whaleGroup.add(jKnob);
    });

    // 4. Gerçekçi Yan Gözler (Lateral Cetacean Eyes on Orbital Swells)
    const eyeSwellGeo = new THREE.SphereGeometry(0.32, 12, 10);
    const eyeMat = new THREE.MeshStandardMaterial({
      color: 0x05070a,
      roughness: 0.04,
      metalness: 0.92
    });
    const glintMat = new THREE.MeshBasicMaterial({ color: 0xffffff });

    function createEye(isLeft) {
      const eyeGroup = new THREE.Group();
      // Fleshy orbital swell
      const swell = new THREE.Mesh(eyeSwellGeo, skinMat);
      swell.scale.set(0.45, 0.85, 1.15);
      eyeGroup.add(swell);

      // Glossy obsidian eyeball
      const eyeball = new THREE.Mesh(new THREE.SphereGeometry(0.13, 14, 14), eyeMat);
      eyeball.position.set(isLeft ? 0.12 : -0.12, 0.02, 0.02);
      eyeGroup.add(eyeball);

      // Corneal specular glint
      const glint = new THREE.Mesh(new THREE.SphereGeometry(0.035, 6, 6), glintMat);
      glint.position.set(isLeft ? 0.22 : -0.22, 0.07, 0.05);
      eyeGroup.add(glint);

      eyeGroup.position.set(isLeft ? 2.18 : -2.18, 0.32, 5.55);
      return eyeGroup;
    }

    this.leftEye = createEye(true);
    this.rightEye = createEye(false);
    this.whaleGroup.add(this.leftEye);
    this.whaleGroup.add(this.rightEye);

    // --- GÖĞÜS YÜZGEÇLERİ (PECTORAL FLIPPERS) ---
    function createFlipper(isLeft) {
      const shape = new THREE.Shape();
      shape.moveTo(0, 0);
      shape.bezierCurveTo(2.5, 0.4, 7.0, -1.2, 9.5, -3.8);
      shape.bezierCurveTo(8.5, -4.2, 5.0, -3.2, 3.0, -2.2);
      shape.bezierCurveTo(1.5, -1.5, 0.5, -0.8, 0, 0);

      const geo = new THREE.ExtrudeGeometry(shape, { depth: 0.25, bevelEnabled: true, bevelSegments: 2, steps: 1, bevelSize: 0.1, bevelThickness: 0.1 });
      geo.computeVertexNormals();
      const mesh = new THREE.Mesh(geo, skinMat);
      const group = new THREE.Group();
      group.add(mesh);
      group.position.set(isLeft ? 3.2 : -3.2, -0.8, 3.2);
      if (isLeft) {
        group.rotation.set(0.2, 0.4, -0.55);
      } else {
        mesh.scale.set(-1, 1, 1);
        group.rotation.set(0.2, -0.4, 0.55);
      }
      return group;
    }

    this.leftFlipper = createFlipper(true);
    this.rightFlipper = createFlipper(false);
    this.whaleGroup.add(this.leftFlipper);
    this.whaleGroup.add(this.rightFlipper);

    // --- KUYRUK YÜZGECİ (TAIL FLUKES) ---
    const flukeShape = new THREE.Shape();
    flukeShape.moveTo(0, 0);
    flukeShape.bezierCurveTo(2.5, 0.3, 5.2, 0.8, 6.8, 1.8);
    flukeShape.bezierCurveTo(6.4, 0.8, 4.5, -0.6, 2.2, -1.2);
    flukeShape.bezierCurveTo(0.8, -1.4, 0.2, -0.8, 0, -0.3);
    flukeShape.bezierCurveTo(-0.2, -0.8, -0.8, -1.4, -2.2, -1.2);
    flukeShape.bezierCurveTo(-4.5, -0.6, -6.4, 0.8, -6.8, 1.8);
    flukeShape.bezierCurveTo(-5.2, 0.8, -2.5, 0.3, 0, 0);

    const flukeGeo = new THREE.ExtrudeGeometry(flukeShape, { depth: 0.18, bevelEnabled: true, bevelSegments: 2, steps: 1, bevelSize: 0.08, bevelThickness: 0.08 });
    flukeGeo.computeVertexNormals();
    const flukeMesh = new THREE.Mesh(flukeGeo, skinMat);

    this.tailGroup = new THREE.Group();
    this.tailGroup.position.set(0, 0.1, -12);
    flukeMesh.rotation.x = Math.PI / 2;
    this.tailGroup.add(flukeMesh);
    this.whaleGroup.add(this.tailGroup);

    // --- SIRT YÜZGECİ (DORSAL FIN) ---
    const dorsalShape = new THREE.Shape();
    dorsalShape.moveTo(0, 0);
    dorsalShape.bezierCurveTo(0.2, 0.8, 0.6, 1.3, 0.4, 1.5);
    dorsalShape.bezierCurveTo(0.1, 1.2, -0.5, 0.4, -1.4, 0);
    dorsalShape.closePath();
    const dorsalGeo = new THREE.ExtrudeGeometry(dorsalShape, { depth: 0.12, bevelEnabled: true, bevelSegments: 1, steps: 1, bevelSize: 0.04, bevelThickness: 0.04 });
    const dorsalMesh = new THREE.Mesh(dorsalGeo, skinMat);
    dorsalMesh.position.set(0, 1.9, -5.5);
    dorsalMesh.rotation.y = Math.PI / 2;
    this.whaleGroup.add(dorsalMesh);

    // Bir tık küçük, zarif ve çevik ölçek (Kullanıcı talebi: scale 0.92)
    this.whaleGroup.scale.set(0.92, 0.92, 0.92);
    this.whaleGroup.position.set(-25, -30, -5);
    this.scene.add(this.whaleGroup);
  }

  buildWaterParticles() {
    const geyserCount = 120;
    const geyserGeo = new THREE.BufferGeometry();
    const geyserPos = new Float32Array(geyserCount * 3);
    this.geyserVel = [];

    for (let i = 0; i < geyserCount; i++) {
      geyserPos[i * 3] = 0;
      geyserPos[i * 3 + 1] = -100;
      geyserPos[i * 3 + 2] = 0;
      this.geyserVel.push({
        vx: (Math.random() - 0.5) * 0.8,
        vy: 2.2 + Math.random() * 2.5,
        vz: (Math.random() - 0.5) * 0.8,
        life: 0
      });
    }
    geyserGeo.setAttribute('position', new THREE.BufferAttribute(geyserPos, 3));
    const geyserMat = new THREE.PointsMaterial({
      color: 0xe0f7ff,
      size: 0.55,
      transparent: true,
      opacity: 0.75,
      blending: THREE.AdditiveBlending
    });
    this.geyserPoints = new THREE.Points(geyserGeo, geyserMat);
    this.scene.add(this.geyserPoints);

    const splashCount = 400;
    const splashGeo = new THREE.BufferGeometry();
    const splashPos = new Float32Array(splashCount * 3);
    this.splashVel = [];

    for (let i = 0; i < splashCount; i++) {
      splashPos[i * 3] = 0;
      splashPos[i * 3 + 1] = -100;
      splashPos[i * 3 + 2] = 0;
      const angle = Math.random() * Math.PI * 2;
      const speed = 1.5 + Math.random() * 8.0;
      this.splashVel.push({
        vx: Math.cos(angle) * speed * 1.5,
        vy: 3.8 + Math.random() * 7.0,
        vz: Math.sin(angle) * speed + 2.5,
        life: 0
      });
    }
    splashGeo.setAttribute('position', new THREE.BufferAttribute(splashPos, 3));
    const splashMat = new THREE.PointsMaterial({
      color: 0xcbeefd,
      size: 0.7,
      transparent: true,
      opacity: 0.88,
      blending: THREE.AdditiveBlending
    });
    this.splashPoints = new THREE.Points(splashGeo, splashMat);
    this.scene.add(this.splashPoints);
  }

  triggerBreach() {
    if (this.isBreaching) return;
    this.isBreaching = true;
    this.breachTime = 0;
    this.hasSprayedBlowhole = false;
    this.hasImpactedWater = false;
    this.lastTime = performance.now();

    setTimeout(() => { playWaterCrash(0.65); }, 250);
  }

  updateBreach(progress) {
    const x = -18 + progress * 36;
    const y = -3 + Math.sin(progress * Math.PI) * 12.0 - (progress > 0.72 ? (progress - 0.72) * 36 : 0);
    const z = -3 + Math.sin(progress * Math.PI) * 8.5;

    this.whaleGroup.position.set(x, y, z);

    const pitch = (0.8 - progress * 1.75);
    const roll = Math.sin(progress * Math.PI) * 2.05;
    const yaw = 0.55 - progress * 0.3;

    this.whaleGroup.rotation.set(pitch, yaw, roll);

    if (this.tailGroup) {
      this.tailGroup.rotation.x = Math.PI / 2 + Math.sin(this.breachTime * 14) * 0.4;
    }
    if (this.leftFlipper && this.rightFlipper) {
      this.leftFlipper.rotation.z = -0.55 + Math.sin(this.breachTime * 10) * 0.25;
      this.rightFlipper.rotation.z = 0.55 - Math.sin(this.breachTime * 10) * 0.25;
    }

    if (progress > 0.34 && !this.hasSprayedBlowhole) {
      this.hasSprayedBlowhole = true;
      playWhaleSong();
      const gPos = this.geyserPoints.geometry.attributes.position.array;
      for (let i = 0; i < this.geyserVel.length; i++) {
        gPos[i * 3] = x + 1.2;
        gPos[i * 3 + 1] = y + 2.2;
        gPos[i * 3 + 2] = z + 2.2;
        this.geyserVel[i].life = 1.0;
      }
      this.geyserPoints.geometry.attributes.position.needsUpdate = true;
    }

    if (progress > 0.72 && !this.hasImpactedWater) {
      this.hasImpactedWater = true;
      playWaterCrash(1.25);
      triggerRealWaterSplash();

      const sPos = this.splashPoints.geometry.attributes.position.array;
      for (let i = 0; i < this.splashVel.length; i++) {
        sPos[i * 3] = x;
        sPos[i * 3 + 1] = -2.5;
        sPos[i * 3 + 2] = z;
        this.splashVel[i].life = 1.0;
      }
      this.splashPoints.geometry.attributes.position.needsUpdate = true;
    }

    if (progress >= 1.0) {
      this.isBreaching = false;
      this.whaleGroup.position.set(-25, -30, -5);
    }
  }

  seekProgress(progress) {
    this.isBreaching = true;
    this.breachTime = progress * this.breachDuration;
    this.updateBreach(progress);
    this.renderer.render(this.scene, this.camera);
  }

  bindEvents() {
    window.addEventListener('resize', () => {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      this.camera.aspect = this.width / this.height;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(this.width, this.height);
    });
  }

  animate() {
    requestAnimationFrame(this.animate);
    const now = performance.now();
    const dt = Math.min(0.08, Math.max(0.005, (now - this.lastTime) * 0.001));
    this.lastTime = now;

    if (this.isBreaching) {
      this.breachTime += dt;
      const progress = Math.min(1.0, this.breachTime / this.breachDuration);
      this.updateBreach(progress);
    }

    if (this.geyserPoints) {
      const gPos = this.geyserPoints.geometry.attributes.position.array;
      for (let i = 0; i < this.geyserVel.length; i++) {
        const v = this.geyserVel[i];
        if (v.life > 0) {
          gPos[i * 3] += v.vx;
          gPos[i * 3 + 1] += v.vy;
          gPos[i * 3 + 2] += v.vz;
          v.vy -= 0.08;
          v.life -= 0.015;
          if (v.life <= 0) gPos[i * 3 + 1] = -100;
        }
      }
      this.geyserPoints.geometry.attributes.position.needsUpdate = true;
    }

    if (this.splashPoints) {
      const sPos = this.splashPoints.geometry.attributes.position.array;
      for (let i = 0; i < this.splashVel.length; i++) {
        const v = this.splashVel[i];
        if (v.life > 0) {
          sPos[i * 3] += v.vx;
          sPos[i * 3 + 1] += v.vy;
          sPos[i * 3 + 2] += v.vz;
          v.vy -= 0.18;
          v.life -= 0.018;
          if (v.life <= 0) sPos[i * 3 + 1] = -100;
        }
      }
      this.splashPoints.geometry.attributes.position.needsUpdate = true;
    }

    this.renderer.render(this.scene, this.camera);
  }
}

// ==========================================
// 10. GERÇEKÇİ OPTİK CAM ISLANMASI & SU DAMLALARI
// (RainyDay.js + Fiziksel Su Lensi Damlaları & Yoğuşma Sisi)
// ==========================================
let rainyEngine = null;
let isRainActive = false;
let splashMistAlpha = 0;
let splashCanvas = null;
let splashCtx = null;
let screenWaterDrops = [];

function initSplashCanvas() {
  splashCanvas = document.getElementById('screenSplashCanvas');
  if (splashCanvas) {
    splashCtx = splashCanvas.getContext('2d');
    splashCanvas.width = window.innerWidth;
    splashCanvas.height = window.innerHeight;
  }
}

function resizeSplash() {
  if (splashCanvas) {
    splashCanvas.width = window.innerWidth;
    splashCanvas.height = window.innerHeight;
  }
}
window.addEventListener('resize', resizeSplash);

function initRainyDay() {
  const bgImg = document.getElementById('nanoBgRef');
  const container = document.getElementById('rainyGlassContainer');
  if (!bgImg || !container || typeof RainyDay === 'undefined') return;

  function setup() {
    try {
      rainyEngine = new RainyDay({
        image: bgImg,
        parentElement: container,
        blur: 10,
        opacity: 0.95,
        fps: 30
      });
      rainyEngine.trail = rainyEngine.TRAIL_DROPS;
      rainyEngine.gravity = rainyEngine.GRAVITY_NON_LINEAR;
      console.log('RainyDay.js optik su lensi hazır.');
    } catch (e) {
      console.warn('RainyDay başlatılamadı:', e);
    }
  }

  if (bgImg.complete && bgImg.naturalWidth > 0) {
    setup();
  } else {
    bgImg.addEventListener('load', setup);
  }
}

function triggerRealWaterSplash() {
  splashMistAlpha = 0.70;

  // 1. Ekranın Tamamına Dağılan 110 Adet Fiziksel Sıvı Cam Damlası
  const count = 110;
  const w = window.innerWidth;
  const h = window.innerHeight;

  for (let i = 0; i < count; i++) {
    const r = 5 + Math.random() * 24;
    const isHeavy = r > 11;

    screenWaterDrops.push({
      x: Math.random() * w,
      y: Math.random() * h * 0.92,
      r: r,
      origR: r,
      vx: (Math.random() - 0.5) * 1.5,
      vy: isHeavy ? (2.0 + Math.random() * 4.0) : (Math.random() * 0.5),
      gravity: isHeavy ? 0.095 : 0.008,
      trail: [],
      alpha: 0.96,
      life: 320 + Math.random() * 200
    });
  }

  // 2. RainyDay.js Optik Arka Plan Kırılması
  if (rainyEngine && !isRainActive) {
    isRainActive = true;
    try {
      rainyEngine.rain([
        [4, 9, 0.6],
        [9, 18, 0.35],
        [18, 30, 0.12]
      ], 35);

      setTimeout(() => {
        if (rainyEngine) {
          rainyEngine.presets = [];
          isRainActive = false;
        }
      }, 7000);
    } catch (e) {
      console.warn('RainyDay su sıçratma hatası:', e);
    }
  }
}

function renderScreenMist() {
  if (!splashCtx && splashCanvas) {
    splashCtx = splashCanvas.getContext('2d');
  }
  if (splashCtx) {
    splashCtx.clearRect(0, 0, splashCanvas.width, splashCanvas.height);

    if (splashMistAlpha > 0.01) {
      const grad = splashCtx.createRadialGradient(
        splashCanvas.width * 0.5, splashCanvas.height * 0.5, 50,
        splashCanvas.width * 0.5, splashCanvas.height * 0.5, Math.max(splashCanvas.width, splashCanvas.height) * 0.75
      );
      grad.addColorStop(0, `rgba(225, 245, 255, ${splashMistAlpha * 0.45})`);
      grad.addColorStop(0.7, `rgba(180, 220, 255, ${splashMistAlpha * 0.35})`);
      grad.addColorStop(1, `rgba(120, 180, 230, ${splashMistAlpha * 0.15})`);

      splashCtx.fillStyle = grad;
      splashCtx.fillRect(0, 0, splashCanvas.width, splashCanvas.height);
      splashMistAlpha *= 0.985;
    }

    for (let i = screenWaterDrops.length - 1; i >= 0; i--) {
      const d = screenWaterDrops[i];
      d.life--;

      if (d.life < 50) {
        d.alpha = (d.life / 50) * 0.96;
        d.r = d.origR * (d.life / 50);
      }

      if (d.r > 9) {
        d.vy += d.gravity;
        d.y += d.vy;
        d.x += (Math.random() - 0.5) * 0.35;
        if (Math.random() > 0.45) {
          d.trail.push({ x: d.x, y: d.y, r: d.r * 0.35, alpha: d.alpha * 0.6 });
        }
      }

      d.trail.forEach(t => {
        t.alpha *= 0.98;
        splashCtx.beginPath();
        splashCtx.arc(t.x, t.y, t.r, 0, Math.PI * 2);
        splashCtx.fillStyle = `rgba(210, 240, 255, ${t.alpha * 0.28})`;
        splashCtx.fill();
      });

      splashCtx.save();
      splashCtx.translate(d.x, d.y);

      splashCtx.beginPath();
      splashCtx.arc(0, 0, d.r, 0, Math.PI * 2);
      splashCtx.fillStyle = `rgba(10, 25, 45, ${d.alpha * 0.4})`;
      splashCtx.fill();

      const innerGrad = splashCtx.createRadialGradient(-d.r * 0.3, -d.r * 0.3, 1, 0, 0, d.r);
      innerGrad.addColorStop(0, `rgba(255, 255, 255, ${d.alpha * 0.95})`);
      innerGrad.addColorStop(0.35, `rgba(205, 238, 255, ${d.alpha * 0.65})`);
      innerGrad.addColorStop(0.75, `rgba(90, 175, 255, ${d.alpha * 0.22})`);
      innerGrad.addColorStop(1, `rgba(255, 255, 255, ${d.alpha * 0.48})`);

      splashCtx.beginPath();
      splashCtx.arc(0, 0, d.r * 0.92, 0, Math.PI * 2);
      splashCtx.fillStyle = innerGrad;
      splashCtx.fill();

      splashCtx.beginPath();
      splashCtx.ellipse(-d.r * 0.32, -d.r * 0.32, d.r * 0.35, d.r * 0.2, -Math.PI / 4, 0, Math.PI * 2);
      splashCtx.fillStyle = `rgba(255, 255, 255, ${d.alpha * 0.96})`;
      splashCtx.fill();

      splashCtx.restore();

      if (d.life <= 0 || d.y > splashCanvas.height + 50) {
        screenWaterDrops.splice(i, 1);
      }
    }
  }
  requestAnimationFrame(renderScreenMist);
}

// ==========================================
// 11. BAŞLATICI & ETKİLEŞİMLİ BUTONLAR
// ==========================================
let whaleEngineInstance = null;

function startAllEngines() {
  initLanguage();
  initScreenshotsAndLightbox();
  initMythicBgCanvas();
  initSplashCanvas();
  renderScreenMist();
  initRainyDay();
  initPhotographicButterflies();
  initOceanWaves();

  const whaleCanvas = document.getElementById('whaleThreeCanvas');
  if (whaleCanvas && typeof THREE !== 'undefined' && !whaleEngineInstance) {
    whaleEngineInstance = new WhaleThreeEngine(whaleCanvas);
    window.whaleEngineInstance = whaleEngineInstance;
  }
  window.triggerRealWaterSplash = triggerRealWaterSplash;
  window.triggerLightning = triggerLightning;

  // Balinayı Çağır Butonu
  const summonBtn = document.getElementById('summonWhaleBtn');
  if (summonBtn) {
    summonBtn.addEventListener('click', (e) => {
      e.preventDefault();
      initAudio();
      triggerLightning();
      if (whaleEngineInstance) {
        whaleEngineInstance.triggerBreach();
      }
    });
  }

  // Sayfa açıldıktan 1.2 saniye sonra ilk görkemli atlayış
  setTimeout(() => {
    if (whaleEngineInstance && !document.hidden) {
      whaleEngineInstance.triggerBreach();
    }
  }, 1200);

  // Periyodik Atlama (Her 30 saniyede bir)
  setInterval(() => {
    if (whaleEngineInstance && !document.hidden && !whaleEngineInstance.isBreaching) {
      whaleEngineInstance.triggerBreach();
    }
  }, 30000);

  // Periyodik Şimşek & Gök Gürültüsü (Her 26 saniyede bir)
  setInterval(() => {
    if (!document.hidden) {
      triggerLightning();
    }
  }, 26000);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', startAllEngines);
} else {
  startAllEngines();
}
