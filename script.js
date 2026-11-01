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
// 6. 3B WEBGL ETERİK KELEBEKLER MOTORU (THREE.JS 3D FLAPPING BUTTERFLIES)
// ==========================================
class ButterfliesThreeEngine {
  constructor(canvas) {
    this.canvas = canvas;
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.butterflies = [];

    this.initScene();
    this.buildButterflies();
    this.bindEvents();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  initScene() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(45, this.width / this.height, 0.1, 1000);
    this.camera.position.set(0, 0, 32);

    this.renderer = new THREE.WebGLRenderer({ canvas: this.canvas, antialias: true, alpha: true });
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const amb = new THREE.AmbientLight(0xffffff, 1.4);
    this.scene.add(amb);
    const dir = new THREE.DirectionalLight(0xfff5e0, 1.1);
    dir.position.set(10, 15, 15);
    this.scene.add(dir);
  }

  createWingTexture(colorType, isLeft) {
    const cvs = document.createElement('canvas');
    cvs.width = 256;
    cvs.height = 340;
    const ctx = cvs.getContext('2d');

    const palettes = {
      blue: { base: '#00d2ff', mid: '#0055ff', dark: '#001144', rim: '#ffffff' },
      emerald: { base: '#00f260', mid: '#0575e6', dark: '#022e1f', rim: '#ffffff' },
      gold: { base: '#ffd700', mid: '#ff8800', dark: '#4a2600', rim: '#ffffff' },
      purple: { base: '#f72585', mid: '#7209b7', dark: '#240046', rim: '#ffffff' }
    };
    const pal = palettes[colorType] || palettes.blue;

    ctx.save();
    if (!isLeft) {
      ctx.translate(256, 0);
      ctx.scale(-1, 1);
    }

    ctx.beginPath();
    ctx.moveTo(20, 160);
    ctx.bezierCurveTo(40, 80, 120, 20, 220, 25);
    ctx.bezierCurveTo(250, 45, 250, 110, 210, 150);
    ctx.bezierCurveTo(240, 190, 230, 270, 170, 310);
    ctx.bezierCurveTo(120, 335, 70, 310, 50, 260);
    ctx.bezierCurveTo(30, 220, 20, 180, 20, 160);
    ctx.closePath();

    const grad = ctx.createRadialGradient(80, 140, 10, 140, 160, 220);
    grad.addColorStop(0, pal.base);
    grad.addColorStop(0.45, pal.mid);
    grad.addColorStop(0.85, pal.dark);
    grad.addColorStop(1, '#050a14');
    ctx.fillStyle = grad;
    ctx.fill();

    ctx.lineWidth = 2.5;
    ctx.strokeStyle = 'rgba(10, 15, 30, 0.75)';
    const veins = [
      [[20, 160], [100, 100], [210, 40]],
      [[20, 160], [120, 115], [225, 80]],
      [[20, 160], [130, 145], [215, 135]],
      [[20, 160], [120, 190], [190, 230]],
      [[20, 160], [90, 230], [150, 290]],
      [[20, 160], [60, 240], [90, 300]]
    ];
    veins.forEach(v => {
      ctx.beginPath();
      ctx.moveTo(v[0][0], v[0][1]);
      ctx.quadraticCurveTo(v[1][0], v[1][1], v[2][0], v[2][1]);
      ctx.stroke();
    });

    ctx.lineWidth = 7;
    ctx.strokeStyle = '#050a14';
    ctx.stroke();

    const dots = [
      [220, 35], [235, 65], [230, 95], [215, 125],
      [225, 180], [220, 220], [195, 265], [160, 298], [115, 320]
    ];
    dots.forEach(([x, y]) => {
      ctx.beginPath();
      ctx.arc(x, y, 3.2, 0, Math.PI * 2);
      ctx.fillStyle = pal.rim;
      ctx.fill();
    });
    ctx.restore();

    const tex = new THREE.CanvasTexture(cvs);
    tex.needsUpdate = true;
    return tex;
  }

  buildButterflies() {
    const species = ['blue', 'emerald', 'gold', 'purple'];
    const count = Math.min(8, Math.max(4, Math.floor(window.innerWidth / 220)));

    for (let i = 0; i < count; i++) {
      const spType = species[i % species.length];
      const leftTex = this.createWingTexture(spType, true);
      const rightTex = this.createWingTexture(spType, false);

      const group = new THREE.Group();

      const bodyGeo = new THREE.CylinderGeometry(0.06, 0.04, 1.4, 8);
      const bodyMat = new THREE.MeshStandardMaterial({ color: 0x111822, roughness: 0.6 });
      const body = new THREE.Mesh(bodyGeo, bodyMat);
      body.rotation.x = Math.PI / 2;
      group.add(body);

      const wingW = 1.4;
      const wingH = 1.85;
      const leftGeo = new THREE.PlaneGeometry(wingW, wingH);
      leftGeo.translate(-wingW * 0.5, 0, 0);
      const leftMat = new THREE.MeshStandardMaterial({
        map: leftTex,
        transparent: true,
        alphaTest: 0.05,
        side: THREE.DoubleSide,
        roughness: 0.35
      });
      const leftWing = new THREE.Mesh(leftGeo, leftMat);
      group.add(leftWing);

      const rightGeo = new THREE.PlaneGeometry(wingW, wingH);
      rightGeo.translate(wingW * 0.5, 0, 0);
      const rightMat = new THREE.MeshStandardMaterial({
        map: rightTex,
        transparent: true,
        alphaTest: 0.05,
        side: THREE.DoubleSide,
        roughness: 0.35
      });
      const rightWing = new THREE.Mesh(rightGeo, rightMat);
      group.add(rightWing);

      const scale = 1.8 + Math.random() * 0.65;
      group.scale.set(scale, scale, scale);

      this.scene.add(group);

      this.butterflies.push({
        group: group,
        leftWing: leftWing,
        rightWing: rightWing,
        x: (Math.random() - 0.5) * 36,
        y: (Math.random() - 0.5) * 20,
        z: (Math.random() - 0.5) * 12,
        vx: (Math.random() > 0.5 ? 1 : -1) * (0.04 + Math.random() * 0.06),
        vy: (Math.random() - 0.5) * 0.035,
        vz: (Math.random() - 0.5) * 0.025,
        flapSpeed: 14 + Math.random() * 6,
        phase: Math.random() * Math.PI * 2
      });
    }
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
    const time = performance.now() * 0.001;

    this.butterflies.forEach(b => {
      b.phase += 0.028;
      b.x += b.vx;
      b.y += Math.sin(b.phase * 2) * 0.045 + b.vy;
      b.z += b.vz;

      if (b.x > 22) { b.x = 22; b.vx = -Math.abs(b.vx); }
      if (b.x < -22) { b.x = -22; b.vx = Math.abs(b.vx); }
      if (b.y > 13) { b.y = 13; b.vy = -Math.abs(b.vy); }
      if (b.y < -13) { b.y = -13; b.vy = Math.abs(b.vy); }
      if (b.z > 8) { b.z = 8; b.vz = -Math.abs(b.vz); }
      if (b.z < -10) { b.z = -10; b.vz = Math.abs(b.vz); }

      b.group.position.set(b.x, b.y, b.z);

      const flap = Math.sin(time * b.flapSpeed) * 0.72;
      b.leftWing.rotation.y = flap;
      b.rightWing.rotation.y = -flap;

      const heading = b.vx > 0 ? 0.35 : -0.35;
      b.group.rotation.set(
        -b.vy * 8 + Math.sin(b.phase) * 0.15,
        b.vx > 0 ? 0.4 : Math.PI - 0.4,
        heading
      );
    });

    this.renderer.render(this.scene, this.camera);
  }
}


// ==========================================
// 7. 3B WEBGL KAMBUR BALİNA MOTORU (THREE.JS 3D HUMPBACK WHALE & OCEAN BREACH)
// ==========================================
class WhaleThreeEngine {
  constructor(canvas) {
    this.canvas = canvas;
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.isBreaching = false;
    this.breachTime = 0;
    this.breachDuration = 4.6; // sn
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

        if (Math.cos(theta) < -0.15 && u > 0.08 && u < 0.6) {
          y += Math.cos(theta * 28) * 0.06;
        }

        if (u < 0.25 && Math.cos(theta) > 0.3) {
          y += Math.sin(u * 40) * Math.cos(theta * 10) * 0.07;
        }

        positions.push(x, y, z);

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

    function createFlipper(isLeft) {
      const flipperShape = new THREE.Shape();
      flipperShape.moveTo(0, 0);
      flipperShape.bezierCurveTo(2.5, 0.4, 7.0, -1.2, 9.5, -3.8);
      flipperShape.bezierCurveTo(8.5, -4.2, 5.0, -3.2, 3.0, -2.2);
      flipperShape.bezierCurveTo(1.5, -1.5, 0.5, -0.8, 0, 0);

      const extrudeSettings = { depth: 0.25, bevelEnabled: true, bevelSegments: 2, steps: 1, bevelSize: 0.1, bevelThickness: 0.1 };
      const flipperGeo = new THREE.ExtrudeGeometry(flipperShape, extrudeSettings);
      flipperGeo.computeVertexNormals();

      const flipperMat = new THREE.MeshStandardMaterial({
        color: isLeft ? 0x111c29 : 0x132030,
        roughness: 0.2,
        metalness: 0.12
      });

      const mesh = new THREE.Mesh(flipperGeo, flipperMat);
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
    const flukeMat = new THREE.MeshStandardMaterial({ color: 0x0f1822, roughness: 0.2, metalness: 0.12 });
    const flukeMesh = new THREE.Mesh(flukeGeo, flukeMat);

    this.tailGroup = new THREE.Group();
    this.tailGroup.position.set(0, 0.1, -12);
    flukeMesh.rotation.x = Math.PI / 2;
    this.tailGroup.add(flukeMesh);
    this.whaleGroup.add(this.tailGroup);

    const dorsalShape = new THREE.Shape();
    dorsalShape.moveTo(0, 0);
    dorsalShape.bezierCurveTo(0.2, 0.8, 0.6, 1.3, 0.4, 1.5);
    dorsalShape.bezierCurveTo(0.1, 1.2, -0.5, 0.4, -1.4, 0);
    dorsalShape.closePath();
    const dorsalGeo = new THREE.ExtrudeGeometry(dorsalShape, { depth: 0.12, bevelEnabled: true, bevelSegments: 1, steps: 1, bevelSize: 0.04, bevelThickness: 0.04 });
    const dorsalMesh = new THREE.Mesh(dorsalGeo, flukeMat);
    dorsalMesh.position.set(0, 1.9, -5.5);
    dorsalMesh.rotation.y = Math.PI / 2;
    this.whaleGroup.add(dorsalMesh);

    this.whaleGroup.position.set(-25, -30, -5);
    this.whaleGroup.scale.set(1.35, 1.35, 1.35);
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
// 8. GERÇEKÇİ OPTİK CAM ISLANMASI & SU DAMLALARI (RAINYDAY.JS + LENS MIST)
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

  // 1. Ekranın Tamamına Dağılan 95 Adet Fiziksel Sıvı Cam Damlası
  const count = 95;
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
// 9. BAŞLATICI & ETKİLEŞİMLİ BUTONLAR
// ==========================================
let whaleEngineInstance = null;
let butterflyEngineInstance = null;

function startAllSystems() {
  initLanguage();
  initScreenshotsAndLightbox();
  initCopyActions();
  initMythicBgCanvas();

  initSplashCanvas();
  renderScreenMist();
  initRainyDay();

  const whaleCanvas = document.getElementById('whaleThreeCanvas');
  if (whaleCanvas && typeof THREE !== 'undefined' && !whaleEngineInstance) {
    whaleEngineInstance = new WhaleThreeEngine(whaleCanvas);
  }

  const butterflyCanvas = document.getElementById('butterflyThreeCanvas');
  if (butterflyCanvas && typeof THREE !== 'undefined' && !butterflyEngineInstance) {
    butterflyEngineInstance = new ButterfliesThreeEngine(butterflyCanvas);
  }

  const summonBtn = document.getElementById('summonWhaleBtn');
  if (summonBtn) {
    summonBtn.addEventListener('click', (e) => {
      e.preventDefault();
      initAudio();
      if (whaleEngineInstance) {
        whaleEngineInstance.triggerBreach();
        showToast('🌊 Kambur balina atladı, ekranınız sırılsıklam oldu! 🐋');
      }
    });
  }

  setTimeout(() => {
    if (whaleEngineInstance && !document.hidden) {
      whaleEngineInstance.triggerBreach();
    }
  }, 3500);

  setInterval(() => {
    if (whaleEngineInstance && !document.hidden && !whaleEngineInstance.isBreaching) {
      whaleEngineInstance.triggerBreach();
    }
  }, 28000);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', startAllSystems);
} else {
  startAllSystems();
}
