/**
 * ALΣF Portal & Privacy Script
 * Sertan Çubukcu (sertancubukcu@gmail.com)
 * 
 * Özellikler:
 * 1. Dil Seçici (TR / EN / İkisi)
 * 2. Ekran Görüntüleri Rayı & Lightbox Büyütücü
 * 3. Bildirim & E-posta Kopyalama
 * 4. Animasyonlu Mitolojik Tuval (Loraks, Transformers Energon, Yu-Gi-Oh Yıldızları)
 * 5. Uçuşan 3B Kanat Çırpan Eterik Kelebekler
 * 6. Zıplayan & Su Sıçratan Mitolojik Balina (Breaching Whale)
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

  // Küçük telefon çerçevelerine ve yakınlaştırılabilir kartlara tıklama
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
  // 5. ANİMASYONLU MİTOLOJİK TUVAL (CANVAS)
  // Loraks Truffula Halesi, Transformers Energon Ağları & Yu-Gi-Oh Yıldızları
  // ==========================================
  const canvas = document.getElementById('mythicBgCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = 0, height = 0;
    let animId = null;

    function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // 1. Loraks Hüzmeleri (Truffula renkleri: Pembe, Turkuaz, Altın sarısı, Mor)
    const orbs = [
      { x: 0.2, y: 0.25, r: 240, color: 'rgba(255, 51, 153, 0.08)', vx: 0.0003, vy: 0.0002 },
      { x: 0.8, y: 0.35, r: 280, color: 'rgba(0, 242, 254, 0.08)', vx: -0.0002, vy: 0.0003 },
      { x: 0.45, y: 0.75, r: 260, color: 'rgba(255, 215, 0, 0.07)', vx: 0.0002, vy: -0.0003 },
      { x: 0.7, y: 0.85, r: 220, color: 'rgba(168, 85, 247, 0.08)', vx: -0.0003, vy: -0.0002 }
    ];

    // 2. Transformers Energon Düğümleri & Hatları
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

    // 3. Yu-Gi-Oh Yıldız Parıltıları & Kadim Glif Tozları
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
      if (document.hidden) {
        animId = requestAnimationFrame(render);
        return;
      }

      time += 0.012;
      ctx.clearRect(0, 0, width, height);

      // A) Loraks Truffula Hüzmeleri Çizimi
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

      // B) Transformers Energon Enerji Hatları
      for (let i = 0; i < energonNodes.length; i++) {
        const n1 = energonNodes[i];
        n1.x += n1.vx;
        n1.y += n1.vy;
        n1.pulse += n1.pulseSpeed;

        if (n1.x < -10) n1.x = width + 10;
        if (n1.x > width + 10) n1.x = -10;
        if (n1.y < -10) n1.y = height + 10;
        if (n1.y > height + 10) n1.y = -10;

        // Yakındaki Energon düğümlerini bağla
        for (let j = i + 1; j < energonNodes.length; j++) {
          const n2 = energonNodes[j];
          const dx = n1.x - n2.x;
          const dy = n1.y - n2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 140) {
            const alpha = (1 - dist / 140) * 0.18;
            ctx.strokeStyle = `rgba(0, 242, 254, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.beginPath();
            ctx.moveTo(n1.x, n1.y);
            ctx.lineTo(n2.x, n2.y);
            ctx.stroke();
          }
        }

        // Düğüm Parlaması
        const glow = 0.4 + 0.4 * Math.sin(n1.pulse);
        ctx.fillStyle = `rgba(0, 242, 254, ${glow})`;
        ctx.beginPath();
        ctx.arc(n1.x, n1.y, n1.size, 0, Math.PI * 2);
        ctx.fill();
      }

      // C) Yu-Gi-Oh Kadim Yıldız Parıltıları
      stars.forEach(star => {
        star.y += star.vy;
        star.twinkle += star.twinkleSpeed;
        if (star.y < -10) {
          star.y = height + 10;
          star.x = Math.random() * width;
        }

        const alpha = 0.25 + 0.65 * Math.abs(Math.sin(star.twinkle));
        ctx.fillStyle = star.isGolden ? `rgba(255, 215, 0, ${alpha})` : `rgba(255, 255, 255, ${alpha})`;

        // 4 Köşeli Eterik Yıldız Çizimi
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

      animId = requestAnimationFrame(render);
    }
    render();
  }


  // ==========================================
  // 6. UÇUŞAN 3B KANAT ÇIRPAN KELEBEKLER (BUTTERFLIES)
  // ==========================================
  const butterflyContainer = document.getElementById('butterflyContainer');
  if (butterflyContainer) {
    const butterflyColors = ['purple', 'cyan', 'gold', 'truffula'];
    const butterflies = [];
    const totalButterflies = Math.min(7, Math.max(4, Math.floor(window.innerWidth / 220)));

    for (let i = 0; i < totalButterflies; i++) {
      const el = document.createElement('div');
      const color = butterflyColors[i % butterflyColors.length];
      el.className = `butterfly ${color}`;
      el.innerHTML = `
        <div class="wings">
          <div class="wing wing-left"></div>
          <div class="wing wing-right"></div>
        </div>
      `;
      butterflyContainer.appendChild(el);

      butterflies.push({
        el: el,
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight * 0.85 + 40,
        vx: (Math.random() > 0.5 ? 1 : -1) * (0.7 + Math.random() * 0.8),
        vy: (Math.random() - 0.5) * 0.5,
        scale: 0.75 + Math.random() * 0.45,
        angle: 0,
        phase: Math.random() * Math.PI * 2,
        targetY: Math.random() * window.innerHeight * 0.8
      });
    }

    function animateButterflies() {
      if (!document.hidden) {
        const w = window.innerWidth;
        const h = window.innerHeight;

        butterflies.forEach(b => {
          b.phase += 0.035;
          b.x += b.vx;
          b.y += Math.sin(b.phase) * 1.4 + b.vy;

          // Ekran sınırlarını aşınca tersine veya karşı tarafa sar
          if (b.vx > 0 && b.x > w + 40) {
            b.x = -40;
            b.y = Math.random() * h * 0.85 + 40;
          } else if (b.vx < 0 && b.x < -40) {
            b.x = w + 40;
            b.y = Math.random() * h * 0.85 + 40;
          }

          if (b.y < 30) b.y = 30;
          if (b.y > h - 80) b.y = h - 80;

          // Yön açısını yumuşakça ayarla
          const targetAngle = b.vx > 0 ? (b.vy * 25 + Math.sin(b.phase) * 12) : (180 - (b.vy * 25 + Math.sin(b.phase) * 12));
          b.angle += (targetAngle - b.angle) * 0.08;

          b.el.style.transform = `translate3d(${b.x}px, ${b.y}px, 0) rotate(${b.angle}deg) scale(${b.scale})`;
        });
      }
      requestAnimationFrame(animateButterflies);
    }
    requestAnimationFrame(animateButterflies);
  }


  // ==========================================
  // 7. ZIPLAYAN & SU SIÇRATAN MİTOLOJİK BALİNA (BREACHING WHALE)
  // ==========================================
  const whaleContainer = document.getElementById('whaleContainer');
  const summonWhaleBtn = document.getElementById('summonWhaleBtn');
  let isWhaleJumping = false;

  // Balina SVG Konteynerini Oluştur
  if (whaleContainer && !document.getElementById('whaleActor')) {
    const actor = document.createElement('div');
    actor.id = 'whaleActor';
    actor.className = 'whale-actor';
    actor.innerHTML = `
      <svg viewBox="0 0 320 180" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%; filter: drop-shadow(0 0 16px rgba(0, 242, 254, 0.75));">
        <defs>
          <linearGradient id="whaleBodyGrad" x1="0%" y1="0%" x2="100%" y2="80%">
            <stop offset="0%" stop-color="#00f2fe"/>
            <stop offset="45%" stop-color="#2563eb"/>
            <stop offset="85%" stop-color="#7c3aed"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="whaleBellyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#a5f3fc"/>
            <stop offset="60%" stop-color="#38bdf8"/>
            <stop offset="100%" stop-color="#1e293b"/>
          </linearGradient>
          <linearGradient id="runeGlow" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#ffd700"/>
            <stop offset="50%" stop-color="#22d3ee"/>
            <stop offset="100%" stop-color="#ec4899"/>
          </linearGradient>
        </defs>
        <!-- Balina Gövdesi -->
        <path d="M 40 100 C 60 40, 150 25, 230 50 C 270 65, 305 95, 315 110 C 295 105, 260 98, 230 115 C 175 145, 95 155, 40 100 Z" fill="url(#whaleBodyGrad)"/>
        <!-- Karın Çizgileri -->
        <path d="M 85 105 C 130 140, 185 140, 230 115 C 185 125, 130 125, 85 105 Z" fill="url(#whaleBellyGrad)" opacity="0.85"/>
        <!-- Kuyruk Yüzgeci -->
        <path d="M 45 102 C 30 90, 10 75, 5 65 C 12 85, 25 98, 38 103 C 25 108, 10 120, 5 140 C 12 130, 30 115, 45 105 Z" fill="url(#whaleBodyGrad)"/>
        <!-- Yan Yüzgeç -->
        <path d="M 160 105 C 185 135, 195 165, 180 170 C 170 168, 165 145, 145 112 Z" fill="#00e5ff" opacity="0.9"/>
        <!-- Göz & Mitolojik Yu-Gi-Oh İşareti -->
        <circle cx="265" cy="82" r="3.5" fill="#ffd700"/>
        <circle cx="265" cy="82" r="6" stroke="#00f2fe" stroke-width="1" opacity="0.8"/>
        <!-- Sırt Energon Glifleri -->
        <path d="M 120 58 Q 160 48 200 62" stroke="url(#runeGlow)" stroke-width="2.5" stroke-linecap="round" opacity="0.9"/>
        <circle cx="140" cy="54" r="2" fill="#ffd700"/>
        <circle cx="175" cy="53" r="2.5" fill="#00f2fe"/>
        <circle cx="210" cy="65" r="2" fill="#ec4899"/>
      </svg>
    `;
    whaleContainer.appendChild(actor);
  }

  // Su Sıçratma Parçacıkları (Droplets) Oluşturucu
  function spawnWaterSplash(centerXPercent, bottomPx, count = 18) {
    if (!whaleContainer) return;
    const containerW = whaleContainer.offsetWidth || window.innerWidth;
    const originX = (containerW * centerXPercent) / 100;

    // Su Halkası
    const ring = document.createElement('div');
    ring.className = 'water-ring';
    ring.style.left = `${originX - 10}px`;
    ring.style.bottom = `${bottomPx}px`;
    whaleContainer.appendChild(ring);
    setTimeout(() => ring.remove(), 1500);

    // Su Damlaları
    for (let i = 0; i < count; i++) {
      const drop = document.createElement('div');
      drop.className = 'splash-droplet';
      drop.style.left = `${originX}px`;
      drop.style.bottom = `${bottomPx + 6}px`;

      const angle = (Math.PI / 180) * (30 + Math.random() * 120); // Yukarı doğru fışkırma
      const distance = 40 + Math.random() * 95;
      const dx = Math.cos(angle) * distance * (Math.random() > 0.5 ? 1 : -1);
      const dy = -Math.sin(angle) * distance;

      drop.style.setProperty('--dx', `${dx}px`);
      drop.style.setProperty('--dy', `${dy}px`);

      whaleContainer.appendChild(drop);
      setTimeout(() => drop.remove(), 1250);
    }
  }

  // Balinayı Zıplatma Fonksiyonu
  function triggerWhaleBreach() {
    const actor = document.getElementById('whaleActor');
    if (!actor || isWhaleJumping) return;

    isWhaleJumping = true;
    actor.classList.remove('jumping');
    void actor.offsetWidth; // Yeniden tetikleme
    actor.classList.add('jumping');

    // 1. Çıkış Su Sıçratması (Sol taraf ~8%)
    setTimeout(() => {
      spawnWaterSplash(10, 15, 20);
    }, 150);

    // 2. Tepe Noktası Işıltısı (~2.2 sn)
    setTimeout(() => {
      spawnWaterSplash(45, 120, 10);
    }, 2200);

    // 3. İniş & Büyük Su Sıçratması (Sağ taraf ~76%)
    setTimeout(() => {
      spawnWaterSplash(76, 18, 26);
    }, 3400);

    // Bitiş ve Hazır Olma
    setTimeout(() => {
      actor.classList.remove('jumping');
      isWhaleJumping = false;
    }, 4400);
  }

  // Balina Düğmesine Tıklama
  if (summonWhaleBtn) {
    summonWhaleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      triggerWhaleBreach();
      showToast('🌊 Eterik balina suları yararak yükseliyor! 🐋');
    });
  }

  // Otomatik Periyodik Atlama (Her 25 saniyede bir)
  setInterval(() => {
    if (!document.hidden && !isWhaleJumping) {
      triggerWhaleBreach();
    }
  }, 25000);

  // Sayfa yüklendikten 3.5 saniye sonra ilk görkemli atlayış
  setTimeout(() => {
    if (!document.hidden) triggerWhaleBreach();
  }, 3500);

});
