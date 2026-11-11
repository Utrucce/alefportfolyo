# -*- coding: utf-8 -*-
"""
Full Site Builder for ALΣF Education & Privacy Portal
Includes:
- Hâl Tercümesi (Curriculum Vitae) section
- Removed all "Amiral gemisi" phrases
- Stated that Privacy Policy covers ALL applications
- Terminated all active experiences (Çınar Koleji: 31 Mayıs, Aygaz: geçen Temmuz)
- Omitted references
"""

import os

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

# ========================================================
# 1. STYLES.CSS
# ========================================================
css_content = """/* ========================================================
   ALΣF (ALEF) EĞİTİM & GİZLİLİK PORTALI
   Modern Siber Neon & Cam Efektli (Glassmorphic) Tasarım
   Mor (#a855f7) - Mavi (#06b6d4, #3b82f6) - Yeşil (#10b981) Paleti
   Mobil Öncelikli & Sıfır Taşma (Mobile First & Zero Overflow)
======================================================== */

:root {
  --bg-dark: #07080e;
  --bg-dark-secondary: #0c0f1a;
  --bg-card: rgba(15, 18, 30, 0.78);
  --bg-card-hover: rgba(24, 30, 50, 0.92);
  --bg-card-solid: #111422;
  
  --color-purple: #a855f7;
  --color-purple-light: #c084fc;
  --color-purple-glow: rgba(168, 85, 247, 0.35);
  
  --color-cyan: #06b6d4;
  --color-cyan-light: #22d3ee;
  --color-blue: #3b82f6;
  --color-blue-glow: rgba(6, 182, 212, 0.35);
  
  --color-green: #10b981;
  --color-green-light: #34d399;
  --color-green-glow: rgba(16, 185, 129, 0.35);
  
  --color-amber: #f59e0b;
  --color-orange: #fb923c;
  --color-telegram: #229ED9;
  --color-bionluk: #00b274;
  
  --text-main: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --text-dark: #0f172a;
  
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-glow: rgba(168, 85, 247, 0.35);
  --border-green: rgba(16, 185, 129, 0.35);
  --border-cyan: rgba(6, 182, 212, 0.35);
  
  --gradient-tri: linear-gradient(135deg, #a855f7 0%, #06b6d4 50%, #10b981 100%);
  --gradient-purple-blue: linear-gradient(135deg, #a855f7 0%, #3b82f6 100%);
  --gradient-blue-green: linear-gradient(135deg, #06b6d4 0%, #10b981 100%);
  --gradient-orange-amber: linear-gradient(135deg, #f97316 0%, #f59e0b 100%);
  
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-full: 9999px;
  
  --transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.45);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.6);
  --shadow-neon: 0 0 25px rgba(168, 85, 247, 0.25);
}

/* ================= Global Reset & Box Sizing ================= */
*, *::before, *::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  -webkit-text-size-adjust: 100%;
}

body {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-dark);
  color: var(--text-main);
  font-family: 'Outfit', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.65;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

/* Arka Plan Işıltıları */
.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(120px);
  pointer-events: none;
  z-index: 0;
  opacity: 0.16;
}
.orb-1 {
  width: 480px;
  height: 480px;
  background: radial-gradient(circle, var(--color-purple) 0%, transparent 70%);
  top: -100px;
  left: -100px;
}
.orb-2 {
  width: 520px;
  height: 520px;
  background: radial-gradient(circle, var(--color-cyan) 0%, transparent 70%);
  top: 40%;
  right: -140px;
}
.orb-3 {
  width: 550px;
  height: 550px;
  background: radial-gradient(circle, var(--color-green) 0%, transparent 70%);
  bottom: -140px;
  left: 20%;
}

/* Ana Taşıyıcı */
.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

/* İki Yana Yaslama */
.text-justify {
  text-align: justify;
  text-justify: inter-word;
  hyphens: auto;
}

/* Sigma Özel Stili */
.sigma {
  font-family: 'Times New Roman', 'Georgia', serif;
  font-weight: 800;
  background: var(--gradient-tri);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
  padding: 0 1px;
}

/* Renk Geçişli Metinler */
.text-gradient {
  background: var(--gradient-tri);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.text-gradient-purple {
  background: var(--gradient-purple-blue);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.text-gradient-green {
  background: var(--gradient-blue-green);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.text-gradient-orange {
  background: var(--gradient-orange-amber);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* ================= Üst Gezinme Çubuğu (Navbar) ================= */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(7, 8, 14, 0.92);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 12px 0;
  transition: var(--transition);
}

.nav-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.brand-group {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--text-main);
  flex-shrink: 0;
}

.brand-logos {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-logo-thumb {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  border: 1px solid var(--border-subtle);
  background: #000;
}

.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: 0.5px;
  line-height: 1.2;
}
.brand-text span {
  font-size: 0.72rem;
  color: var(--text-muted);
  display: block;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.nav-links a {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  transition: var(--transition);
  white-space: nowrap;
}

.nav-links a:hover,
.nav-links a.active {
  color: #fff;
  background: rgba(168, 85, 247, 0.15);
  border: 1px solid rgba(168, 85, 247, 0.3);
}

/* Dil Seçici */
.lang-switcher-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.lang-switcher {
  display: inline-flex;
  background: #111422;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 3px;
  gap: 3px;
  max-width: 100%;
}

.lang-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 7px 15px;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  min-height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.lang-btn:hover {
  color: #fff;
}

.lang-btn.active {
  background: var(--gradient-purple-blue);
  color: #fff;
  box-shadow: 0 2px 10px rgba(168, 85, 247, 0.4);
}

/* ================= Butonlar ================= */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: var(--radius-md);
  font-size: 0.92rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: var(--transition);
  border: 1px solid transparent;
  max-width: 100%;
  text-align: center;
  box-sizing: border-box;
  overflow-wrap: break-word;
  word-break: break-word;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-primary {
  background: var(--gradient-purple-blue);
  color: #fff;
  box-shadow: 0 4px 18px var(--color-purple-glow);
}
.btn-primary:hover {
  box-shadow: 0 6px 24px rgba(168, 85, 247, 0.6);
}

.btn-green {
  background: var(--gradient-blue-green);
  color: #fff;
  box-shadow: 0 4px 18px var(--color-green-glow);
}
.btn-green:hover {
  box-shadow: 0 6px 24px rgba(16, 185, 129, 0.6);
}

.btn-orange {
  background: var(--gradient-orange-amber);
  color: #fff;
  box-shadow: 0 4px 18px rgba(249, 115, 22, 0.4);
}
.btn-orange:hover {
  box-shadow: 0 6px 24px rgba(249, 115, 22, 0.6);
}

.btn-bionluk {
  background: linear-gradient(135deg, #00b274 0%, #059669 100%);
  color: #fff;
  box-shadow: 0 4px 18px rgba(0, 178, 116, 0.4);
}
.btn-bionluk:hover {
  box-shadow: 0 6px 24px rgba(0, 178, 116, 0.6);
  transform: translateY(-2px);
}

.btn-store {
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  color: #fff;
  box-shadow: 0 4px 18px rgba(59, 130, 246, 0.4);
}
.btn-store:hover {
  box-shadow: 0 6px 24px rgba(59, 130, 246, 0.6);
}

.btn-outline {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  color: var(--text-main);
}
.btn-outline:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
}

.btn-copy {
  background: #1e2235;
  color: var(--color-cyan-light);
  border: 1px solid rgba(6, 182, 212, 0.3);
  font-size: 0.84rem;
  padding: 8px 16px;
}
.btn-copy:hover {
  background: rgba(6, 182, 212, 0.15);
  border-color: var(--color-cyan);
}

.action-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 26px;
  width: 100%;
}

/* ================= Giriş (Hero) Bölümü ================= */
.hero {
  padding: 55px 0 35px;
  text-align: center;
  position: relative;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  border-radius: var(--radius-full);
  background: rgba(168, 85, 247, 0.12);
  border: 1px solid rgba(168, 85, 247, 0.3);
  color: var(--color-purple-light);
  font-size: 0.82rem;
  font-weight: 600;
  margin-bottom: 20px;
  max-width: 100%;
  box-sizing: border-box;
}

.badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-purple-light);
  box-shadow: 0 0 10px var(--color-purple);
  flex-shrink: 0;
}

.badge-green {
  background: rgba(16, 185, 129, 0.12);
  border-color: rgba(16, 185, 129, 0.3);
  color: var(--color-green-light);
}
.badge-green .badge-dot {
  background: var(--color-green-light);
  box-shadow: 0 0 10px var(--color-green);
}

.badge-orange {
  background: rgba(249, 115, 22, 0.12);
  border-color: rgba(249, 115, 22, 0.3);
  color: var(--color-orange);
}
.badge-orange .badge-dot {
  background: var(--color-orange);
  box-shadow: 0 0 10px var(--color-orange);
}

.hero-title {
  font-size: 2.85rem;
  font-weight: 900;
  line-height: 1.18;
  margin: 0 auto 18px;
  max-width: 950px;
  letter-spacing: -0.5px;
}

.hero-subtitle {
  font-size: 1.08rem;
  color: var(--text-secondary);
  max-width: 880px;
  margin: 0 auto 16px;
  line-height: 1.8;
}

/* Bölüm Başlıkları */
.section-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.section-head h2 {
  font-size: 1.95rem;
  font-weight: 800;
  margin: 0 0 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  line-height: 1.25;
}

.section-head p {
  color: var(--text-muted);
  margin: 0;
  font-size: 0.98rem;
  max-width: 800px;
}

/* ================= Başlıca Uygulamalarımız (Dual Showcase) ================= */
.flagship-showcase {
  margin: 45px 0 65px;
}

.flagship-card {
  background: var(--bg-card);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 32px 28px;
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  transition: var(--transition);
}

.flagship-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.flagship-card.mebags::before {
  background: var(--gradient-tri);
}
.flagship-card.oabt::before {
  background: var(--gradient-orange-amber);
}

.flagship-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.flagship-brand-wrap {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}

.flagship-logos-box {
  display: flex;
  align-items: center;
  gap: 12px;
}

.flagship-logo-img {
  width: 72px;
  height: 72px;
  border-radius: var(--radius-md);
  object-fit: cover;
  border: 2px solid var(--border-subtle);
  box-shadow: var(--shadow-md);
  background: #000;
}

.flagship-title-box h3 {
  font-size: 1.65rem;
  font-weight: 800;
  margin: 0 0 6px;
  line-height: 1.2;
}

.flagship-title-box p {
  margin: 0;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.flagship-meta-badges {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.flagship-desc {
  font-size: 1.02rem;
  color: var(--text-secondary);
  line-height: 1.8;
  margin-bottom: 24px;
}

.flagship-features-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  gap: 14px;
  margin-bottom: 26px;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 12px 14px;
  font-size: 0.92rem;
  color: var(--text-secondary);
}

.feature-item svg {
  color: var(--color-green-light);
  flex-shrink: 0;
  margin-top: 2px;
}

/* ================= Ekran Görüntüleri Kaydırma Rayı (Carousel) ================= */
.screenshot-carousel-wrap {
  position: relative;
  margin-top: 20px;
}

.carousel-nav-btns {
  display: flex;
  align-items: center;
  gap: 10px;
}

.carousel-arrow {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #141724;
  border: 1px solid var(--border-subtle);
  color: var(--text-main);
  font-size: 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.carousel-arrow:hover {
  background: var(--color-purple);
  color: #fff;
  border-color: var(--color-purple);
}

.screenshot-track {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 8px 4px 18px;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: var(--color-purple-light) #111422;
}

.screenshot-track::-webkit-scrollbar {
  height: 6px;
}
.screenshot-track::-webkit-scrollbar-track {
  background: #111422;
  border-radius: 4px;
}
.screenshot-track::-webkit-scrollbar-thumb {
  background: var(--color-purple);
  border-radius: 4px;
}

.phone-mockup {
  flex: 0 0 240px;
  scroll-snap-align: start;
  background: #0f111c;
  border: 2px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  padding: 8px;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.phone-mockup:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: var(--color-cyan);
  box-shadow: 0 16px 35px rgba(6, 182, 212, 0.25);
}

.phone-screen-wrap {
  border-radius: 18px;
  overflow: hidden;
  aspect-ratio: 9 / 16;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.phone-screen-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.phone-caption {
  font-size: 0.82rem;
  font-weight: 600;
  text-align: center;
  color: var(--text-secondary);
  padding: 8px 4px 2px;
  line-height: 1.35;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ================= AR-GE Uygulamalar Izgarası ================= */
.apps-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 20px;
  margin-top: 24px;
}

.app-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}

.app-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-tri);
  opacity: 0.8;
}

.app-card:hover {
  transform: translateY(-6px);
  border-color: var(--color-cyan);
  background: var(--bg-card-hover);
  box-shadow: 0 14px 35px rgba(6, 182, 212, 0.2);
}

.app-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}

.app-icon {
  width: 60px;
  height: 60px;
  border-radius: var(--radius-md);
  object-fit: cover;
  background: #000;
  border: 1px solid var(--border-subtle);
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

.app-meta h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 4px;
  line-height: 1.25;
}

.app-status {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: rgba(16, 185, 129, 0.12);
  color: var(--color-green-light);
  border: 1px solid rgba(16, 185, 129, 0.3);
}
.app-status.status-arge {
  background: rgba(168, 85, 247, 0.12);
  color: var(--color-purple-light);
  border-color: rgba(168, 85, 247, 0.3);
}

.app-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0 0 16px;
  flex-grow: 1;
}

.app-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-subtle);
  padding-top: 12px;
  margin-top: auto;
}

.app-tech-pill {
  font-size: 0.76rem;
  color: var(--text-muted);
}

/* ================= İnternet Platformları Izgarası ================= */
.web-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr));
  gap: 20px;
  margin-top: 24px;
}

.web-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px 22px;
  text-decoration: none;
  color: var(--text-main);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}

.web-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-blue-green);
  opacity: 0.8;
}

.web-card:hover {
  transform: translateY(-6px);
  border-color: var(--color-green-light);
  background: var(--bg-card-hover);
  box-shadow: 0 14px 35px rgba(16, 185, 129, 0.22);
}

.web-header {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 12px;
}

.web-icon-wrap {
  width: 46px;
  height: 46px;
  border-radius: var(--radius-sm);
  background: rgba(6, 182, 212, 0.12);
  border: 1px solid rgba(6, 182, 212, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-cyan-light);
  flex-shrink: 0;
}

.web-title-box h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 4px;
}

.web-url {
  font-size: 0.75rem;
  color: var(--color-cyan-light);
  word-break: break-all;
}

.web-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0 0 16px;
}

.web-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--color-green-light);
  font-size: 0.88rem;
  font-weight: 600;
  margin-top: auto;
  max-width: 100%;
  word-break: break-word;
}

/* ================= Bionluk Özel Banner ================= */
.bionluk-banner-card {
  background: linear-gradient(135deg, rgba(0, 178, 116, 0.14) 0%, rgba(15, 23, 42, 0.88) 100%);
  border: 1px solid rgba(0, 178, 116, 0.45);
  border-radius: var(--radius-lg);
  padding: 24px 26px;
  margin: 22px 0 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  box-shadow: 0 10px 30px rgba(0, 178, 116, 0.18);
  flex-wrap: wrap;
}

.bionluk-content {
  flex: 1 1 300px;
}

.bionluk-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  background: rgba(0, 178, 116, 0.22);
  border: 1px solid rgba(0, 178, 116, 0.5);
  color: #34d399;
  font-size: 0.76rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.bionluk-content h3 {
  font-size: 1.35rem;
  font-weight: 800;
  margin: 0 0 6px;
  color: #fff;
}

.bionluk-content p {
  font-size: 0.94rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.6;
}

.telegram-banner-box {
  margin: 20px 0 28px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border-subtle);
  background: #000;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
}

.telegram-banner-box img {
  width: 100%;
  height: auto;
  display: block;
}

/* ================= Telegram Botları ve Toplulukları Izgarası ================= */
.bots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: 18px;
  margin-top: 20px;
}

.bot-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 20px 18px;
  text-decoration: none;
  color: var(--text-main);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}

.bot-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--color-telegram);
  opacity: 0.8;
}

.bot-card:hover {
  transform: translateY(-5px);
  border-color: var(--color-telegram);
  background: var(--bg-card-hover);
  box-shadow: 0 12px 30px rgba(34, 158, 217, 0.25);
}

.bot-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.bot-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(34, 158, 217, 0.4);
  background: #000;
  flex-shrink: 0;
}

.bot-meta h3 {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0 0 2px;
}

.bot-badge {
  font-size: 0.74rem;
  color: var(--color-telegram);
  font-weight: 600;
}

.bot-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0 0 14px;
}

.bot-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--color-telegram);
  font-size: 0.84rem;
  font-weight: 700;
  margin-top: auto;
  max-width: 100%;
  word-break: break-word;
}

/* Telegram Grupları Izgarası */
.groups-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: 18px;
  margin-top: 22px;
}

.group-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 22px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-decoration: none;
  color: var(--text-main);
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}

.group-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-blue-green);
  opacity: 0.8;
}

.group-card:hover {
  transform: translateY(-6px);
  border-color: var(--color-green-light);
  background: var(--bg-card-hover);
  box-shadow: 0 14px 35px rgba(16, 185, 129, 0.22);
}

.group-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 10px;
}

.group-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--color-green-light);
}

.group-title h3 {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0 0 2px;
  line-height: 1.25;
}
.group-title span {
  font-size: 0.74rem;
  color: var(--color-green-light);
  font-weight: 600;
}

.group-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0 0 14px;
}

.group-cta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: var(--radius-sm);
  background: var(--gradient-blue-green);
  color: #fff;
  font-size: 0.86rem;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
  transition: var(--transition);
  text-align: center;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  word-break: break-word;
}

.group-card:hover .group-cta {
  box-shadow: 0 6px 22px rgba(16, 185, 129, 0.5);
  transform: translateY(-2px);
}

/* ================= 3D Kitaplar Izgarası ================= */
.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr));
  gap: 22px;
  margin-top: 24px;
}

.book-card-3d {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 22px 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-decoration: none;
  color: var(--text-main);
  transition: var(--transition);
  perspective: 1000px;
}

.book-card-3d:hover {
  transform: translateY(-8px);
  border-color: var(--color-purple);
  box-shadow: 0 16px 35px var(--color-purple-glow);
}

.book-cover-wrap {
  width: 100%;
  aspect-ratio: 1 / 1.35;
  border-radius: 10px;
  overflow: hidden;
  background: #111422;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  margin-bottom: 14px;
  transition: var(--transition);
  transform-style: preserve-3d;
  display: flex;
  align-items: center;
  justify-content: center;
}

.book-cover-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.book-card-3d:hover .book-cover-wrap {
  transform: rotateY(-6deg) scale(1.03);
}

.book-info h3 {
  font-size: 1.02rem;
  font-weight: 700;
  margin: 0 0 6px;
  line-height: 1.3;
}

.book-author {
  font-size: 0.8rem;
  color: var(--color-cyan-light);
  margin-bottom: 8px;
  display: block;
}

.book-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--color-purple-light);
  font-size: 0.84rem;
  font-weight: 700;
  margin-top: auto;
  max-width: 100%;
  word-break: break-word;
}

/* ================= EğitimYayın Mağaza Panosu ================= */
.store-banner {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.12) 0%, rgba(168, 85, 247, 0.12) 100%);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: var(--radius-xl);
  padding: 30px;
  margin: 35px 0 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  box-shadow: var(--shadow-lg);
  flex-wrap: wrap;
}

.store-banner-content {
  flex: 1 1 350px;
}

.store-banner-logo {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-md);
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.15);
  box-shadow: var(--shadow-md);
}

/* ================= Sosyal Kanallar Izgarası ================= */
.social-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 16px;
  margin-top: 24px;
}

.social-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 18px;
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  color: var(--text-main);
  transition: var(--transition);
}

.social-card:hover {
  transform: translateY(-4px);
  border-color: var(--color-cyan);
  background: var(--bg-card-hover);
  box-shadow: 0 10px 25px rgba(6, 182, 212, 0.2);
}

.social-icon-box {
  width: 46px;
  height: 46px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: rgba(255, 255, 255, 0.05);
}

.social-meta h3 {
  font-size: 0.98rem;
  font-weight: 700;
  margin: 0 0 2px;
}
.social-meta span {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* ================= HÂL TERCÜMESİ (CV / ÖZGEÇMİŞ) TASARIMI ================= */
.cv-hero-card {
  background: linear-gradient(135deg, rgba(168, 85, 247, 0.12) 0%, rgba(6, 182, 212, 0.10) 50%, rgba(16, 185, 129, 0.10) 100%);
  border: 1px solid rgba(168, 85, 247, 0.35);
  border-radius: var(--radius-xl);
  padding: 36px 32px;
  margin-bottom: 35px;
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 26px;
  flex-wrap: wrap;
}

.cv-avatar-box {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.cv-avatar-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--color-purple-light);
  box-shadow: 0 0 25px var(--color-purple-glow);
  background: #000;
}

.cv-hero-info h3 {
  font-size: 1.85rem;
  font-weight: 900;
  margin: 0 0 4px;
}

.cv-hero-title {
  font-size: 1.05rem;
  color: var(--color-cyan-light);
  font-weight: 600;
  margin-bottom: 10px;
  display: block;
}

.cv-contact-chips {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  font-size: 0.86rem;
  color: var(--text-muted);
}

.cv-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  text-decoration: none;
}

.cv-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 540px), 1fr));
  gap: 26px;
}

.cv-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  box-shadow: var(--shadow-md);
  position: relative;
  overflow: hidden;
}

.cv-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-tri);
}

.cv-card-head {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-subtle);
}

.cv-card-head h4 {
  font-size: 1.25rem;
  font-weight: 800;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 10px;
  color: #fff;
}

.cv-timeline {
  display: flex;
  flex-direction: column;
  gap: 22px;
  position: relative;
  padding-left: 20px;
  border-left: 2px solid rgba(168, 85, 247, 0.25);
}

.cv-timeline-item {
  position: relative;
}

.cv-timeline-item::before {
  content: "";
  position: absolute;
  left: -27px;
  top: 5px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--color-purple);
  box-shadow: 0 0 10px var(--color-purple-light);
  border: 2px solid #000;
}

.cv-timeline-item.green::before {
  background: var(--color-green);
  box-shadow: 0 0 10px var(--color-green-light);
}

.cv-timeline-item.cyan::before {
  background: var(--color-cyan);
  box-shadow: 0 0 10px var(--color-cyan-light);
}

.cv-item-title {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0 0 2px;
  color: #fff;
}

.cv-item-company {
  font-size: 0.9rem;
  color: var(--color-cyan-light);
  font-weight: 600;
  display: block;
  margin-bottom: 4px;
}

.cv-item-date {
  display: inline-block;
  font-size: 0.78rem;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-muted);
  margin-bottom: 8px;
  border: 1px solid var(--border-subtle);
}

.cv-item-date.ended {
  background: rgba(239, 68, 68, 0.12);
  color: #fca5a5;
  border-color: rgba(239, 68, 68, 0.3);
}

.cv-item-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
}

.cv-badge-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.cv-badge-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  font-size: 0.86rem;
  color: var(--text-secondary);
  transition: var(--transition);
}

.cv-badge-item:hover {
  background: rgba(168, 85, 247, 0.1);
  border-color: var(--color-purple);
  color: #fff;
  transform: translateY(-2px);
}

/* ================= Gizlilik Politikası & GDPR Düzeni ================= */
.policy-box {
  background: var(--bg-card);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 36px 32px;
  margin: 30px 0 50px;
  box-shadow: var(--shadow-lg);
}

.dual-lang-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
}

.policy-clause {
  margin-bottom: 28px;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 24px;
}
.policy-clause:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.policy-clause h3 {
  font-size: 1.3rem;
  font-weight: 800;
  margin: 0 0 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--text-main);
}

.policy-clause p {
  color: var(--text-secondary);
  font-size: 0.98rem;
  line-height: 1.8;
  margin: 0 0 12px;
}

.policy-highlight-box {
  background: rgba(16, 185, 129, 0.06);
  border-left: 4px solid var(--color-green-light);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 0.94rem;
  color: var(--text-secondary);
  line-height: 1.7;
}

.policy-highlight-box.purple {
  background: rgba(168, 85, 247, 0.06);
  border-left-color: var(--color-purple);
}

.policy-highlight-box.cyan {
  background: rgba(6, 182, 212, 0.06);
  border-left-color: var(--color-cyan);
}

/* ================= Büyük Görüntüleyici (Lightbox) ================= */
.lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.92);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.lightbox-modal.active {
  display: flex;
}

.lightbox-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.lightbox-content img {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: var(--radius-md);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
}

.lightbox-caption {
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  margin-top: 14px;
  text-align: center;
}

.lightbox-close {
  position: absolute;
  top: -45px;
  right: 0;
  background: none;
  border: none;
  color: #fff;
  font-size: 2rem;
  cursor: pointer;
  padding: 8px;
  line-height: 1;
}

/* ================= Bildirim (Toast) ================= */
.toast-notice {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1100;
  background: var(--bg-card-solid);
  border: 1px solid var(--color-cyan);
  color: var(--text-main);
  padding: 12px 20px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  font-size: 0.92rem;
  font-weight: 600;
  opacity: 0;
  transform: translateY(20px);
  transition: var(--transition);
  pointer-events: none;
}
.toast-notice.show {
  opacity: 1;
  transform: translateY(0);
}

/* ================= Altbilgi (Footer) ================= */
.site-footer {
  background: #05060a;
  border-top: 1px solid var(--border-subtle);
  padding: 45px 0 30px;
  margin-top: 70px;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.footer-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 25px;
  flex-wrap: wrap;
}

.footer-bottom {
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding-top: 20px;
  font-size: 0.84rem;
}

/* ================= TELEFON VE MOBİL UYARLAMALARI (CRITICAL FIX) ================= */
@media (max-width: 860px) {
  .site-header {
    position: relative !important;
    top: auto !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    background: #090b14 !important;
    padding: 10px 0 !important;
  }
  
  .nav-wrapper {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  
  .brand-group {
    justify-content: center;
  }
  
  .nav-links {
    justify-content: center;
    gap: 6px;
    overflow-x: auto;
    flex-wrap: nowrap;
    padding-bottom: 4px;
    -webkit-overflow-scrolling: touch;
  }
  
  .nav-links a {
    font-size: 0.8rem;
    padding: 6px 10px;
    flex-shrink: 0;
  }
  
  .lang-switcher-wrap {
    justify-content: center;
  }
  
  .lang-btn {
    padding: 6px 12px;
    font-size: 0.78rem;
  }

  .cv-grid {
    grid-template-columns: 1fr;
  }
  .cv-hero-card {
    padding: 24px 18px;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 35px 0 20px;
  }
  .hero-title {
    font-size: 1.95rem;
  }
  .hero-subtitle {
    font-size: 0.96rem;
  }
  .section-head h2 {
    font-size: 1.55rem;
  }
  .flagship-card {
    padding: 22px 16px;
  }
  .flagship-logo-img {
    width: 56px;
    height: 56px;
  }
  .flagship-title-box h3 {
    font-size: 1.35rem;
  }
  .policy-box {
    padding: 22px 16px;
  }
  .phone-mockup {
    flex: 0 0 210px;
  }
  .bionluk-banner-card {
    padding: 20px 16px;
  }
  .store-banner {
    padding: 22px 18px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 14px;
  }
  .hero-title {
    font-size: 1.6rem;
  }
  .hero-subtitle {
    font-size: 0.9rem;
  }
  .action-bar {
    flex-direction: column;
  }
  .btn {
    width: 100%;
    padding: 12px 16px;
  }
  .lang-switcher {
    width: 100%;
    display: flex;
  }
  .lang-btn {
    flex: 1;
    padding: 7px 6px;
    font-size: 0.75rem;
  }
  .phone-mockup {
    flex: 0 0 76vw;
    max-width: 250px;
  }
  .flagship-header {
    flex-direction: column;
  }
  .flagship-brand-wrap {
    flex-direction: column;
    align-items: flex-start;
  }
  .section-head {
    flex-direction: column;
    align-items: flex-start;
  }
  .toast-notice {
    left: 14px;
    right: 14px;
    bottom: 14px;
    text-align: center;
  }
}
"""

with open(os.path.join(BASE_DIR, "styles.css"), "w", encoding="utf-8") as f:
    f.write(css_content)
print("Updated styles.css with Hâl Tercümesi styles and without Amiral gemisi.")
