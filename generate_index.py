# -*- coding: utf-8 -*-
"""
Generator for index.html (Showcase Portal with Hâl Tercümesi)
"""

import os

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

html_content = """<!DOCTYPE html>
<html lang="tr" data-lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#07080e">
  <title>ALΣF (ALEF) - MΣB-AGS &amp; Türkçe ÖABT | Eğitim, Yayın ve Dijital Projeler Portalı</title>
  <meta name="description" content="Sertan Çubukcu tarafından geliştirilen ALΣF MΣB-AGS, Türkçe ÖABT, EğitimYayın Mağazası, Google Play Kitapları, canlı internet platformları, Telegram botları ve Hâl Tercümesi portali.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Arka Plan Küreleri -->
  <div class="orb orb-1" aria-hidden="true"></div>
  <div class="orb orb-2" aria-hidden="true"></div>
  <div class="orb orb-3" aria-hidden="true"></div>

  <!-- Üst Gezinme Çubuğu (Mobilde Göreceli / Relative Konumlandırma) -->
  <header class="site-header">
    <div class="container nav-wrapper">
      <a href="index.html" class="brand-group">
        <div class="brand-logos">
          <img src="assets/kurt.png" alt="Kurt Arma" class="nav-logo-thumb">
          <img src="assets/logo-photoroom.png" alt="Sertan Çubukcu Logo" class="nav-logo-thumb">
          <img src="assets/alef-logo.png" alt="ALΣF Logo" class="nav-logo-thumb">
        </div>
        <div class="brand-text">
          <h1>AL<span class="sigma">Σ</span>F</h1>
          <span>M<span class="sigma">Σ</span>B - AGS &amp; Türkçe ÖABT</span>
        </div>
      </a>

      <!-- Gezinme Bağlantıları -->
      <nav class="nav-links">
        <a href="#tanitim">Tanıtım</a>
        <a href="#ana-uygulamalar">Uygulamalar</a>
        <a href="#hal-tercumesi">Hâl Tercümesi</a>
        <a href="#yayinlar">Kitaplar &amp; Mağaza</a>
        <a href="#internet-projeleri">İnternet Projeleri</a>
        <a href="#arge-uygulamalar">AR-GE</a>
        <a href="#telegram-ekosistemi">Telegram</a>
        <a href="#goruntuler">Görüntüler</a>
        <a href="#iletisim">İletişim</a>
        <a href="privacy.html" class="active">Gizlilik İlkeleri</a>
      </nav>

      <!-- Dil Seçici (Taşmasız ve Dokunmatik Dostu) -->
      <div class="lang-switcher-wrap">
        <div class="lang-switcher" role="group" aria-label="Dil Seçimi">
          <button class="lang-btn active" data-lang="tr" aria-pressed="true">Türkçe</button>
          <button class="lang-btn" data-lang="en" aria-pressed="false">English</button>
          <button class="lang-btn" data-lang="both" aria-pressed="false">İkisi</button>
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- Giriş (Hero) Bölümü -->
    <section class="hero" id="tanitim">
      <div class="badge">
        <span class="badge-dot"></span>
        <span>2026 M<span class="sigma">Σ</span>B - AGS &amp; Türkçe ÖABT Müfredatına Tam Uyumlu</span>
      </div>

      <h1 class="hero-title">
        Öğretmenlik ve Akademi Yolunda<br>
        <span class="text-gradient">AL<span class="sigma">Σ</span>F ile Zirveye Adım At</span>
      </h1>

      <p class="hero-subtitle text-justify">
        Millî Eğitim Bakanlığı Akademi Giriş Sınavı (M<span class="sigma">Σ</span>B - AGS) ve Türkçe ÖABT adayları için 
        titizlikle geliştirilen kapsamlı soru havuzu, deneme sınavları, konu özetleri, <strong>EğitimYayın Mağazası</strong>, 
        <strong>Google Play Kitapları</strong>, canlı internet platformları, 8 adet etkileşimli Telegram eğitim botu ve 
        geliştirilmekte olan yeni nesil Android uygulamalarıyla eksiksiz bir eğitim ekosistemi.
      </p>

      <div class="action-bar">
        <a href="#ana-uygulamalar" class="btn btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
          Yayınlanan Uygulamalar
        </a>
        <a href="#hal-tercumesi" class="btn btn-green">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          Hâl Tercümesi (Özgeçmiş)
        </a>
        <a href="#yayinlar" class="btn btn-store">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          EğitimYayın &amp; Kitaplar
        </a>
        <a href="privacy.html" class="btn btn-outline">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          Gizlilik Politikası
        </a>
      </div>
    </section>

    <!-- Yayınlanan ve Aktif Uygulamalarımız (MEB-AGS ve Türkçe ÖABT Dual Showcase) -->
    <section class="flagship-showcase" id="ana-uygulamalar">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="url(#triGrad)" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            Yayınlanan ve Aktif Uygulamalarımız
          </h2>
          <p class="text-justify">
            Adaylarımızın sınav hazırlığında doğrudan kullandığı, hem telefondan hem de bilgisayardan gerçek logoları ve canlı arayüz görüntüleriyle sunulan başlıca mobil platformlarımız:
          </p>
        </div>
      </div>

      <!-- 1. ALΣF - MΣB - AGS (Yayında Olan Başlıca Uygulama) -->
      <div class="flagship-card mebags">
        <div class="flagship-header">
          <div class="flagship-brand-wrap">
            <div class="flagship-logos-box">
              <img src="assets/mebags_phone_icon.png" alt="ALΣF MEB-AGS Telefon Logosu" class="flagship-logo-img" title="Telefondaki Gerçek Logo">
              <img src="assets/mebags_pc_logo.jpg" alt="Millî Eğitim Akademisi Logosu" class="flagship-logo-img" title="Millî Eğitim Akademisi Kurumsal Logosu">
            </div>
            <div class="flagship-title-box">
              <h3>AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS</h3>
              <p>Millî Eğitim Bakanlığı Akademi Giriş Sınavı Hazırlık Uygulaması</p>
            </div>
          </div>
          <div class="flagship-meta-badges">
            <span class="badge badge-green"><span class="badge-dot"></span>Yayında • 2026 Müfredatı</span>
            <span class="badge"><span class="badge-dot"></span>10.990+ Soru</span>
          </div>
        </div>

        <p class="flagship-desc text-justify">
          Millî Eğitim Bakanlığı Akademi Giriş Sınavı (M<span class="sigma">Σ</span>B - AGS) için hazırlanan; 1739 sayılı Millî Eğitim Temel Kanunu, 
          222 sayılı İlköğretim ve Eğitim Kanunu, 1982 Anayasası, Eğitim Bilimleri, Tarih, Coğrafya ve Türkçe modüllerini içeren 
          kapsamlı soru bankası ve sınav simülasyonu.
        </p>

        <div class="flagship-features-list">
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>10.990+ Özgün ve Denetimli Soru Havuzu</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Görsel Hafıza ve Bilgi Heybesi Kartları</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Kelime Avı ve Eğitici Oyun Modları</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>İnternetsiz Çevrim Dışı Çalışabilme Yeteneği</span>
          </div>
        </div>

        <!-- MEB-AGS Gerçek Telefon Ekran Görüntüleri Galerisi -->
        <div class="screenshot-carousel-wrap" data-carousel="mebags">
          <div class="section-head" style="margin-bottom: 12px;">
            <h4 style="margin: 0; font-size: 1.1rem; color: var(--color-cyan-light);">Gerçek Telefon Ekran Görüntüleri (M<span class="sigma">Σ</span>B - AGS):</h4>
            <div class="carousel-nav-btns">
              <button class="carousel-arrow" data-dir="prev" aria-label="Önceki">&#8592;</button>
              <button class="carousel-arrow" data-dir="next" aria-label="Sonraki">&#8594;</button>
            </div>
          </div>

          <div class="screenshot-track">
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_1.jpg" alt="MΣB-AGS Ana Menü ve İlerleme Paneli" loading="lazy"></div>
              <div class="phone-caption">Gösterge Paneli &amp; İlerleme</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_2.jpg" alt="MΣB-AGS Oyun Modu Seçimi" loading="lazy"></div>
              <div class="phone-caption">Oyun Modları &amp; Kelime Avı</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_3.jpg" alt="MΣB-AGS Bilgi Kartı Kategorileri" loading="lazy"></div>
              <div class="phone-caption">Bilgi Kartı ve Mevzuat Kategorileri</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_4.jpg" alt="MΣB-AGS Görsel Hafıza Paneli" loading="lazy"></div>
              <div class="phone-caption">Görsel Hafıza (Tarih, Coğrafya)</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_5.jpg" alt="MΣB-AGS Ders Kartı ve Harita Notu" loading="lazy"></div>
              <div class="phone-caption">Ders Kartı &amp; Harita Notları</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_6.jpg" alt="MΣB-AGS Soru Çözüm Ekranı" loading="lazy"></div>
              <div class="phone-caption">Soru Çözümü &amp; Tahlil</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_7.jpg" alt="MΣB-AGS Zaman Ayarlı Test" loading="lazy"></div>
              <div class="phone-caption">Zaman Ayarlı Test &amp; Skor</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/mebags_8.jpg" alt="MΣB-AGS Teşekkür ve Notlar" loading="lazy"></div>
              <div class="phone-caption">Uygulama Bilgilendirme &amp; Notlar</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. ALΣF Türkçe ÖABT (Gerçek Turuncu Logo) -->
      <div class="flagship-card oabt">
        <div class="flagship-header">
          <div class="flagship-brand-wrap">
            <div class="flagship-logos-box">
              <img src="assets/alef_turkce_oabt_orange.png" alt="ALΣF Türkçe ÖABT Gerçek Turuncu Logo" class="flagship-logo-img" title="Gerçek Turuncu Logo">
              <img src="assets/alef_turkce_oabt_emblem.png" alt="ALΣF Türkçe ÖABT Amblemi" class="flagship-logo-img" title="Kurumsal Amblem Logosu">
              <img src="assets/turkeoabt_phone_icon.png" alt="Telefondaki Türkçe ÖABT Logosu" class="flagship-logo-img" title="Telefondaki Gerçek Logo">
            </div>
            <div class="flagship-title-box">
              <h3>AL<span class="sigma">Σ</span>F Türkçe ÖABT</h3>
              <p>Türkçe Öğretmenliği Alan Bilgisi Sınavı Hazırlık Platformu</p>
            </div>
          </div>
          <div class="flagship-meta-badges">
            <span class="badge badge-orange"><span class="badge-dot"></span>Türkçe Öğretmenliği • 1 Dakikada Türkçe ÖABT</span>
            <span class="badge"><span class="badge-dot"></span>9.910+ Soru</span>
          </div>
        </div>

        <p class="flagship-desc text-justify">
          Eski Türk Edebiyatı, Yeni Türk Edebiyatı, Halk Edebiyatı, Dilbilimi, Dört Temel Beceri (Okuma, Dinleme, Konuşma, Yazma) 
          ve Alan Eğitimi alanlarında derinlemesine soru arşivi, Dede Korkut nasihatleri ve Pırtılcan araç deposunu bir araya getiren 
          kapsamlı alan eğitimi uygulaması.
        </p>

        <div class="flagship-features-list">
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>9.910+ Alan Bilgisi ve Beceri Sorusu</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Dede Korkut Nasihatleri ve Edebi Taktikler</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Pırtılcan Araç Deposu ve Terim Sözlüğü</span>
          </div>
          <div class="feature-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Cihaz İçi Şifrelenmiş Yerel Güvenlik</span>
          </div>
        </div>

        <!-- Türkçe ÖABT Gerçek Telefon Ekran Görüntüleri Galerisi -->
        <div class="screenshot-carousel-wrap" data-carousel="oabt">
          <div class="section-head" style="margin-bottom: 12px;">
            <h4 style="margin: 0; font-size: 1.1rem; color: var(--color-orange);">Gerçek Telefon Ekran Görüntüleri (Türkçe ÖABT):</h4>
            <div class="carousel-nav-btns">
              <button class="carousel-arrow" data-dir="prev" aria-label="Önceki">&#8592;</button>
              <button class="carousel-arrow" data-dir="next" aria-label="Sonraki">&#8594;</button>
            </div>
          </div>

          <div class="screenshot-track">
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_1.png" alt="Türkçe ÖABT Ana Menü ve İlerleme" loading="lazy"></div>
              <div class="phone-caption">Ana Menü &amp; Genel İlerleme</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_2.png" alt="Türkçe ÖABT Kelime Avı Oyunu" loading="lazy"></div>
              <div class="phone-caption">Kelime Avı Oyunu</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_3.png" alt="Türkçe ÖABT Görsel Hafıza Notları" loading="lazy"></div>
              <div class="phone-caption">Görsel Hafıza &amp; İnfografikler</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_4.png" alt="Türkçe ÖABT Hafıza Kartı Sorusu" loading="lazy"></div>
              <div class="phone-caption">Hafıza Kartı Soru Ekranı</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_5.png" alt="Türkçe ÖABT Hafıza Kartı Cevabı" loading="lazy"></div>
              <div class="phone-caption">Hafıza Kartı Cevap Modülü</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_6.png" alt="Dede Korkut Nasihati" loading="lazy"></div>
              <div class="phone-caption">Dede Korkut'un Nasihati</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_7.png" alt="Oyun Modları ve İstatistikler" loading="lazy"></div>
              <div class="phone-caption">Oyun Modları &amp; İstatistikler</div>
            </div>
            <div class="phone-mockup" title="Büyütmek için tıklayın">
              <div class="phone-screen-wrap"><img src="assets/oabt_8.png" alt="Pırtılcan Araç Deposu" loading="lazy"></div>
              <div class="phone-caption">Pırtılcan Araç Deposu</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HÂL TERCÜMESİ (CV / ÖZGEÇMİŞ) BÖLÜMÜ -->
    <section id="hal-tercumesi" style="margin: 55px 0 70px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            Hâl Tercümesi (Sertan Çubukcu)
          </h2>
          <p class="text-justify">
            Türkçe Öğretmeni, Eğitim Yazarı ve Mobil Uygulama Geliştiricisi Sertan Çubukcu'nun akademik ve mesleki özgeçmişi:
          </p>
        </div>
      </div>

      <!-- Profil Özet Kartı -->
      <div class="cv-hero-card">
        <div class="cv-avatar-box">
          <img src="assets/logo-photoroom.png" alt="Sertan Çubukcu Fotoğrafı" class="cv-avatar-img">
          <div class="cv-hero-info">
            <h3>Sertan Çubukcu</h3>
            <span class="cv-hero-title">Türkçe Öğretmeni | Öğretmen Yetiştirme Programı Mezunu</span>
            <div class="cv-contact-chips">
              <span class="cv-chip">🎓 Yıldız Teknik Üniversitesi</span>
              <span class="cv-chip">📍 İstanbul</span>
              <a href="mailto:sertancubukcu@gmail.com" class="cv-chip" data-copy-email>✉️ sertancubukcu@gmail.com</a>
              <span class="cv-chip">🗣️ İngilizce (B1)</span>
            </div>
          </div>
        </div>
        <div>
          <a href="https://www.linkedin.com/in/sertan%C3%A7ubukcu/" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="font-size: 0.86rem;">
            LinkedIn Profilini İncele &rarr;
          </a>
        </div>
      </div>

      <!-- CV Detay Izgarası -->
      <div class="cv-grid">

        <!-- 1. Kısa Öz Tanıtım & Vizyon -->
        <div class="cv-card" style="grid-column: 1 / -1;">
          <div class="cv-card-head">
            <h4>📖 Kısa Öz Tanıtım &amp; Eğitim Vizyonu</h4>
          </div>
          <p class="text-justify" style="color: var(--text-secondary); line-height: 1.8; margin: 0; font-size: 0.96rem;">
            Gelişime açık bir öğretmen ve araştırmacı olarak; Türkçe Öğretmenliği alanında edindiğim lisans eğitimi ve Öğretmen Yetiştirme Programı tecrübem sayesinde eğitim dünyasında uzmanlaşmayı, modern eğitim tekniklerini, dijital yetkinlikleri ve yenilikçi yaklaşımları sınıf ortamına entegre edebilmeyi hedefliyorum. Çevrim içi ve fiziksel eğitim fırsatlarını takip ederek hayat boyu eğitim anlayışını benimsiyor; insan odaklı, pedagojik uzmanlıkla zenginleştirilmiş etkili bir iletişim modelini esas alıyorum. Öğretmenlik mesleğinin gerektirdiği pedagojik birikimin yanında eğitim yazılımları, mobil soru bankaları ve interaktif öğrenme araçları geliştirerek dijital eğitim alanında katma değer üretiyorum.
          </p>
        </div>

        <!-- 2. Eğitim Bilgileri -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>🎓 Eğitim</h4>
          </div>
          <div class="cv-timeline">
            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Lisans Derecesi, Türkçe Öğretmenliği</h5>
              <span class="cv-item-company">Yıldız Teknik Üniversitesi, İstanbul</span>
              <span class="cv-item-date">Eylül 2021 – Ocak 2025</span>
              <p class="cv-item-desc text-justify">
                Türk Dili, Dilbilim, Eski ve Yeni Türk Edebiyatı, Halk Bilimi, Dört Temel Dil Becerisi (Okuma, Dinleme, Konuşma, Yazma), Eğitim Psikolojisi, Öğretim Teknolojileri ve Ölçme-Değerlendirme alanlarında kapsamlı lisans eğitimi.
              </p>
            </div>
          </div>
        </div>

        <!-- 3. Bilimsel Projeler & Araştırmalar -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>🔬 Bilimsel Projeler</h4>
          </div>
          <div class="cv-timeline">
            <div class="cv-timeline-item cyan">
              <h5 class="cv-item-title">TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projesi</h5>
              <span class="cv-item-company">TÜBİTAK Bilim İnsanı Destek Programları Başkanlığı</span>
              <span class="cv-item-date ended">Mayıs 2025 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                <strong>Proje Başlığı:</strong> "Sosyal Aidiyet ve Okuma Performansı İlişkisinde Aile Motivasyonunun Aracılığı: PISA Tabanlı İkincil Bir Analiz". Uluslararası PISA eğitim verileri üzerinden okuma becerileri ile aile faktörünün yapısal eşitlik modellemesiyle tahlili.
              </p>
            </div>
          </div>
        </div>

        <!-- 4. İş Deneyimi (Bütün Aktifler Sonlandırılmıştır) -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>💼 İş Deneyimi</h4>
          </div>
          <div class="cv-timeline">
            <div class="cv-timeline-item green">
              <h5 class="cv-item-title">Öğretmen Yetiştirme Programı</h5>
              <span class="cv-item-company">Çınar Koleji, Başakşehir / İstanbul</span>
              <span class="cv-item-date ended">Aralık 2024 – 31 Mayıs 2025 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                Modern maarif modeli uygulamaları, aktif öğrenme etkinlikleri, sınıf içi pedagojik süreçler ve ders materyali geliştirme çalışmaları.
              </p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Depo Çalışanı, Dönemlik İşçi (Günlük)</h5>
              <span class="cv-item-company">Aygaz A.Ş., İstanbul</span>
              <span class="cv-item-date ended">Nisan 2023 – Temmuz 2024 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                Merkezî e-ticaret lojistik süreçleri, stok yönetimi, takım koordinasyonu ve operasyonel disiplin.
              </p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Kargo Çalışanı</h5>
              <span class="cv-item-company">MNG Kargo (DHL Group), Esenyurt / İstanbul</span>
              <span class="cv-item-date">Şubat 2020 – Ağustos 2020</span>
              <p class="cv-item-desc text-justify">Lojistik sevkiyat, tasnif ve dağıtım operasyonları yönetimi.</p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Paketleme Elemanı</h5>
              <span class="cv-item-company">Tempo Şekerleme, Arnavutköy / İstanbul</span>
              <span class="cv-item-date">Mayıs 2018 – Ocak 2019</span>
              <p class="cv-item-desc text-justify">Üretim bandı kalite kontrol ve hijyenik paketleme süreçleri.</p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Kasiyer</h5>
              <span class="cv-item-company">Şok Marketler, Esenyurt / İstanbul</span>
              <span class="cv-item-date">Mart 2016 – Ağustos 2016</span>
              <p class="cv-item-desc text-justify">Müşteri iletişimi, kasa yönetimi ve reyon düzeni.</p>
            </div>
          </div>
        </div>

        <!-- 5. Stajlar & Öğretmenlik Uygulamaları -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>🏫 Stajlar &amp; Öğretmenlik Uygulaması</h4>
          </div>
          <div class="cv-timeline">
            <div class="cv-timeline-item green">
              <h5 class="cv-item-title">Stajyer Öğretmen</h5>
              <span class="cv-item-company">Çınar Koleji, Başakşehir / İstanbul</span>
              <span class="cv-item-date ended">Kasım 2024 – 31 Mayıs 2025 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                Rehber öğretmen eşliğinde ortaokul kademesinde ders gözlemleri, soru çözümü etütleri ve pedagojik rehberlik uygulamaları.
              </p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Öğretmenlik Uygulaması (Millî Eğitim Bakanlığı)</h5>
              <span class="cv-item-company">T.C. Esenler Yunus Emre Ortaokulu, Esenler / İstanbul</span>
              <span class="cv-item-date">Eylül 2023 – Haziran 2024</span>
              <p class="cv-item-desc text-justify">
                MEB müfredatı kapsamında haftalık ders anlatımları, ölçme-değerlendirme araçları hazırlama ve sınıf yönetimi uygulamaları.
              </p>
            </div>
          </div>
        </div>

        <!-- 6. Gönüllülük Faaliyetleri -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>🤝 Gönüllülük Faaliyetleri</h4>
          </div>
          <div class="cv-timeline">
            <div class="cv-timeline-item cyan">
              <h5 class="cv-item-title">Gönüllü Eğitmen</h5>
              <span class="cv-item-company">Okul Destek Derneği, İstanbul</span>
              <span class="cv-item-date ended">Ekim 2024 – 2025 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                Sosyo-ekonomik açıdan dezavantajlı öğrencilere yönelik çevrim içi Türkçe dersleri, okuma atölyeleri ve eğitimde fırsat eşitliği çalışmaları.
              </p>
            </div>

            <div class="cv-timeline-item">
              <h5 class="cv-item-title">Editör</h5>
              <span class="cv-item-company">Yıldız Teknik Üniversitesi Dil Atölyesi Kulübü, İstanbul</span>
              <span class="cv-item-date ended">Aralık 2021 – 2025 (Tamamlandı)</span>
              <p class="cv-item-desc text-justify">
                Kültür, edebiyat ve dilbilim bültenlerinin içerik planlaması, edebi metin tahlili ve yayın redaksiyonu koordinasyonu.
              </p>
            </div>
          </div>
        </div>

        <!-- 7. Sertifikalar ve Yetkinlikler -->
        <div class="cv-card">
          <div class="cv-card-head">
            <h4>📜 Sertifikalar &amp; Yetkinlik Rozetleri</h4>
          </div>
          <div class="cv-badge-list">
            <span class="cv-badge-item">🎯 YetGen Öğretmen Eğitim Programı (Mayıs 2025)</span>
            <span class="cv-badge-item">🗣️ İngilizce B1 Düzeyi (Aralık 2024)</span>
            <span class="cv-badge-item">💬 Etkili İletişim Stratejileri (Aralık 2024)</span>
            <span class="cv-badge-item">⏳ Zaman Yönetimi (Aralık 2024)</span>
            <span class="cv-badge-item">🧘 Öğretmenin Psikolojik Dayanıklılığı (Aralık 2024)</span>
            <span class="cv-badge-item">📊 Veri Bilimine Giriş (Aralık 2024)</span>
            <span class="cv-badge-item">🧩 Problem Çözme Teknikleri (Kasım 2024)</span>
            <span class="cv-badge-item">🎤 Topluluk Önünde Konuşma &amp; Sunum (Kasım 2024)</span>
            <span class="cv-badge-item">📝 Microsoft Word Temelleri (Kasım 2024)</span>
            <span class="cv-badge-item">💼 İş İngilizcesi (Kasım 2024)</span>
            <span class="cv-badge-item">🤖 Arduino ile Robotiğe Giriş (Kasım 2024)</span>
            <span class="cv-badge-item">⚡ Atılganlık Becerileri (Aralık 2023)</span>
            <span class="cv-badge-item">🤝 Zor Öğrencilerle İletişim (Aralık 2023)</span>
            <span class="cv-badge-item">📱 Dijital Yaşam Becerileri (Mart 2023)</span>
            <span class="cv-badge-item">💻 72 Saatlik Bilgisayarsız Robotik Kodlama (Temmuz 2021)</span>
          </div>
        </div>

      </div>
    </section>

    <!-- Yayınlar & Mağaza Bölümü (EğitimYayın ve 7 Google Play Kitabı) -->
    <section id="yayinlar" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            Yayın Mağazası &amp; Dijital Kitaplarımız
          </h2>
          <p class="text-justify">
            Sertan Çubukcu tarafından kaleme alınan Türkçe ÖABT, M<span class="sigma">Σ</span>B-AGS hazırlık kitapları, denemeler ve eğitim mağazası vitrini:
          </p>
        </div>
      </div>

      <!-- EğitimYayın Mağaza Panosu -->
      <div class="store-banner">
        <img src="assets/google_play_developer_logo.jpg" alt="EğitimYayın Sertan Çubukcu Mağaza Logosu" class="store-banner-logo">
        <div class="store-banner-content">
          <div class="badge badge-green" style="margin-bottom: 8px;"><span class="badge-dot"></span>Satış &amp; Dağıtım Mağazası</div>
          <h3 style="font-size: 1.45rem; font-weight: 800; margin: 0 0 8px; color: #fff;">AL<span class="sigma">Σ</span>F | Sertan Çubukcu | EğitimYayın</h3>
          <p class="text-justify" style="color: var(--text-secondary); margin: 0 0 16px; font-size: 0.95rem; line-height: 1.7;">
            Türkçe Öğretmenliği ÖABT ve Millî Eğitim Akademisi hazırlık sürecine yönelik basılı ve dijital soru bankalarımız, 
            özel deneme setlerimiz ve lisanslı ders notlarımızın doğrudan temin edilebileceği güvenli mağaza portalı.
          </p>
          <a href="https://egitimyayin.com/magaza.php?slug=alef-sertan-cubukcu" target="_blank" rel="noopener noreferrer" class="btn btn-store">
            Mağazayı Ziyaret Et &rarr;
          </a>
        </div>
      </div>

      <!-- Google Play Kitaplar Koleksiyonu (Utrucce Dahil 7 Eser) -->
      <div class="section-head" style="margin-top: 30px;">
        <div>
          <h3 style="font-size: 1.35rem; font-weight: 800; margin: 0 0 6px;">Google Play'de Kitaplar Koleksiyonu</h3>
          <p class="text-justify">Doğrudan cihazınıza indirebileceğiniz veya internet üzerinden okuyabileceğiniz dijital eserlerimiz:</p>
        </div>
        <a href="https://play.google.com/store/books/collection/cluster?gsr=SheCARQKEAoMN1JkYUVRQUFRQkFKEAkQBA%3D%3D:S:ANO1ljJsHAw&hl=tr" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="font-size: 0.84rem;">
          Bütün Koleksiyonu Görüntüle &rarr;
        </a>
      </div>

      <div class="books-grid">

        <!-- 1. Utrucce (Yeni Eser) -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Utrucce?id=7RdaEQAAQBAJ&hl=tr" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_utrucce.jpg" alt="Utrucce Kitap Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge badge-green" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 5,0 • Ücretsiz</div>
              <h3>Utrucce</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 2. Pırtıl Terakki-2 -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_P%C4%B1rt%C4%B1l_Terakki_2_T%C3%BCrk%C3%A7e_%C3%96ABT?id=F9jWEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover_F9jWEQAAQBAJ.jpg" alt="Pırtıl Terakki-2 Kitap Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 3,4 • Ücretsiz</div>
              <h3>Pırtıl Terakki-2, Türkçe ÖABT</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 3. Türkçe ÖABT Denemesi, Pırtıl-Terakki -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_T%C3%BCrk%C3%A7e_%C3%96ABT_Denemesi_P%C4%B1rt%C4%B1l_Terakki?id=TzTMEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover_TzTMEQAAQBAJ.jpg" alt="Türkçe ÖABT Denemesi Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 2,3 • Ücretsiz</div>
              <h3>Türkçe ÖABT Denemesi, Pırtıl-Terakki</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 4. Halk Edebiyatı - Girizgâh -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Halk_Edebiyat%C4%B1_Girizg%C3%A2h_Soru_Mecmua?id=_uPKEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover__uPKEQAAQBAJ.jpg" alt="Halk Edebiyatı Girizgâh Kitap Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 4,2 • Ücretsiz</div>
              <h3>Halk Edebiyatı - Girizgâh, Soru Mecmuası</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 5. 2024 Maarif Karikatürleştirilmiş Öğrenme Çıktıları -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_2024_Ortaokul_T%C3%BCrk%C3%A7e_%C3%96%C4%9Fretim_Progra?id=xuPKEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover_xuPKEQAAQBAJ.jpg" alt="2024 Maarif Öğrenme Çıktıları Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 4,7 • Ücretsiz</div>
              <h3>2024 Maarif Karikatürleştirilmiş Çıktılar</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 6. Mihenk Zühre / Türkçe ÖABT -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Mihenk_Z%C3%BChre_T%C3%BCrk%C3%A7e_%C3%96ABT?id=NLMCEgAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover_NLMCEgAAQBAJ.jpg" alt="Mihenk Zühre Kitap Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 4,3 • Ücretsiz</div>
              <h3>Mihenk Zühre / Türkçe ÖABT</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

        <!-- 7. Türkçe ÖABT Denemesi / Pırtlak-1 -->
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_T%C3%BCrk%C3%A7e_%C3%96ABT_Denemesi_P%C4%B1rtlak_1?id=RBLZEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div>
            <div class="book-cover-wrap">
              <img src="assets/book_cover_RBLZEQAAQBAJ.jpg" alt="Pırtlak-1 Kitap Kapağı" loading="lazy">
            </div>
            <div class="book-info">
              <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 4,2 • Ücretsiz</div>
              <h3>Türkçe ÖABT Denemesi / Pırtlak-1</h3>
              <span class="book-author">Sertan Çubukcu</span>
            </div>
          </div>
          <div class="book-cta">
            <span>Google Play'de İncele</span> &rarr;
          </div>
        </a>

      </div>
    </section>

    <!-- Canlı İnternet Platformları & Eğitim Portalları -->
    <section id="internet-projeleri" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            Canlı İnternet Platformları &amp; Eğitim Portalları
          </h2>
          <p class="text-justify">
            Adaylar, öğrenciler ve araştırmacılar için geliştirdiğimiz, tarayıcınız üzerinden doğrudan erişebileceğiniz aktif çevrim içi internet servislerimiz:
          </p>
        </div>
      </div>

      <div class="web-grid">

        <!-- 1. Pıtrak Nüsha -->
        <a href="https://pitraknusha.onrender.com/" target="_blank" rel="noopener noreferrer" class="web-card">
          <div>
            <div class="web-header">
              <div class="web-icon-wrap">🏷️</div>
              <div class="web-title-box">
                <span class="badge badge-green" style="font-size: 0.7rem; padding: 2px 6px; margin-bottom: 4px;">Canlı İnternet Servisi</span>
                <h3>Pıtrak Nüsha</h3>
                <span class="web-url">pitraknusha.onrender.com</span>
              </div>
            </div>
            <p class="web-desc text-justify">
              Türkçe ve edebiyat alanında kavram haritaları, etiketli pratik not arşivi ve görsel hafıza kartlarıyla hızlı tekrar ve tahlil portalı.
            </p>
          </div>
          <div class="web-cta">
            <span>Platforma Git</span> &rarr;
          </div>
        </a>

        <!-- 2. Radyo Tiyatrosu -->
        <a href="https://radyotiyatrosu.onrender.com/" target="_blank" rel="noopener noreferrer" class="web-card">
          <div>
            <div class="web-header">
              <div class="web-icon-wrap">🎙️</div>
              <div class="web-title-box">
                <span class="badge badge-green" style="font-size: 0.7rem; padding: 2px 6px; margin-bottom: 4px;">Sesli Kültür Portalı</span>
                <h3>Radyo Tiyatrosu</h3>
                <span class="web-url">radyotiyatrosu.onrender.com</span>
              </div>
            </div>
            <p class="web-desc text-justify">
              Klasik Türk ve dünya edebiyatı eserlerinin seslendirildiği, dinleyerek öğrenmeyi pekiştiren estetik ve geniş radyo tiyatrosu arşivi.
            </p>
          </div>
          <div class="web-cta">
            <span>Tiyatroyu Dinle</span> &rarr;
          </div>
        </a>

        <!-- 3. ALΣF Psikoloji -->
        <a href="https://alef-psikoloji.onrender.com/" target="_blank" rel="noopener noreferrer" class="web-card">
          <div>
            <div class="web-header">
              <div class="web-icon-wrap">🧠</div>
              <div class="web-title-box">
                <span class="badge badge-green" style="font-size: 0.7rem; padding: 2px 6px; margin-bottom: 4px;">Eğitim Bilimleri</span>
                <h3>AL<span class="sigma">Σ</span>F Psikoloji</h3>
                <span class="web-url">alef-psikoloji.onrender.com</span>
              </div>
            </div>
            <p class="web-desc text-justify">
              M<span class="sigma">Σ</span>B-AGS ve KPSS adayları için gelişim psikolojisi, öğrenme kuramları, rehberlik ve özel eğitim bilgi bankası.
            </p>
          </div>
          <div class="web-cta">
            <span>Portala Bağlan</span> &rarr;
          </div>
        </a>

        <!-- 4. Utrucce: Afet Dersleri -->
        <a href="https://utrucce.github.io/afed-dersleri/" target="_blank" rel="noopener noreferrer" class="web-card">
          <div>
            <div class="web-header">
              <div class="web-icon-wrap">🚨</div>
              <div class="web-title-box">
                <span class="badge badge-green" style="font-size: 0.7rem; padding: 2px 6px; margin-bottom: 4px;">Maarif Bilinci</span>
                <h3>Utrucce: Afet Dersleri</h3>
                <span class="web-url">utrucce.github.io/afed-dersleri</span>
              </div>
            </div>
            <p class="web-desc text-justify">
              Yeni maarif modeliyle tam uyumlu; afet farkındalığı, deprem bilinci, ilk yardım ve acil durum kolay eğitim mecmuası.
            </p>
          </div>
          <div class="web-cta">
            <span>Dersleri İncele</span> &rarr;
          </div>
        </a>

      </div>
    </section>

    <!-- Geliştirilmekte Olan Android Uygulamalarımız (AR-GE Laboratuvarı) -->
    <section id="arge-uygulamalar" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
            Geliştirilmekte Olan Android Uygulamalarımız (AR-GE)
          </h2>
          <p class="text-justify">
            Sertan Çubukcu tarafından geliştirme ve test süreçleri devam eden, KPSS ve EKYS için telefondan alınan gerçek logolarıyla ve özgün altyapılarıyla yakında adaylarla buluşacak mobil uygulamalar:
          </p>
        </div>
      </div>

      <div class="apps-grid">

        <!-- 1. ALΣF KPSS (Telefondaki gerçek logo: kpss_phone_icon.png) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/kpss_phone_icon.png" alt="ALΣF KPSS Logosu" class="app-icon">
              <div class="app-meta">
                <h3>AL<span class="sigma">Σ</span>F KPSS</h3>
                <span class="app-status">Kapalı Beta Sürümünde</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Genel Yetenek ve Genel Kültür, Tarih, Coğrafya ve Yurttaşlık alanlarında akıllı soru bankası, deneme sınavları ve görsel hafıza kartları modülü.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Android • Çevrim Dışı</span>
            <span class="badge" style="font-size: 0.72rem; padding: 2px 8px;">KPSS 2026</span>
          </div>
        </div>

        <!-- 2. ALΣF EKYS (Telefondaki gerçek logo: ekys_phone_icon.png) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/ekys_phone_icon.png" alt="ALΣF EKYS Logosu" class="app-icon">
              <div class="app-meta">
                <h3>AL<span class="sigma">Σ</span>F EKYS</h3>
                <span class="app-status status-arge">Geliştirme Aşamasında</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Millî Eğitim Bakanlığı Eğitim Kurumlarına Yönetici Seçme Sınavı mevzuat, anayasa, protokol kuralları ve yönetim bilimleri simülasyonu.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Android • Mevzuat</span>
            <span class="badge" style="font-size: 0.72rem; padding: 2px 8px;">EKYS 2026</span>
          </div>
        </div>

        <!-- 3. ALΣF Türkçe ÖABT (Gerçek turuncu logo) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/alef_turkce_oabt_orange.png" alt="ALΣF Türkçe ÖABT Turuncu Logo" class="app-icon">
              <div class="app-meta">
                <h3>AL<span class="sigma">Σ</span>F Türkçe ÖABT</h3>
                <span class="app-status">Yayında • Türkçe ÖABT</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Eski ve Yeni Türk Edebiyatı, Dilbilimi, Halk Edebiyatı ve Alan Eğitimi kapsamlı soru ve deneme havuzu.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Android • Yerel Güvenlik</span>
            <span class="badge badge-orange" style="font-size: 0.72rem; padding: 2px 8px;">Türkçe ÖABT</span>
          </div>
        </div>

        <!-- 4. Mergen -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-mergen.jpg" alt="Mergen Logosu" class="app-icon">
              <div class="app-meta">
                <h3>Mergen</h3>
                <span class="app-status">Alfa Deneme Motoru</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Zaman ayarlı deneme sınavı analiz motoru, net hesaplama algoritmaları ve kişiselleştirilmiş eksik giderme rehberi.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Sınav Analiz Motoru</span>
            <span class="badge" style="font-size: 0.72rem; padding: 2px 8px;">Ölçme &amp; Değerlendirme</span>
          </div>
        </div>

        <!-- 5. Pırtıl (İnternetsiz Yerel Sûnî Zekâ) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-pirtil.jpg" alt="Pırtıl Logosu" class="app-icon">
              <div class="app-meta">
                <h3>Pırtıl</h3>
                <span class="app-status status-arge">Yerel Sûnî Zekâ</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Eğitilmek üzere geliştirilen, doğrudan telefonda çalışan, internet bağlantısı gerektirmeyen tamamen yerel sûnî zekâ (cihaz içi yapay öğrenme) asistanı.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Cihaz İçi Sûnî Zekâ</span>
            <span class="badge badge-green" style="font-size: 0.72rem; padding: 2px 8px;">Yerel Öğrenme</span>
          </div>
        </div>

        <!-- 6. Karargâh (Veri ve Telefon Güvenliği) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-karargah.png" alt="Karargâh Logosu" class="app-icon">
              <div class="app-meta">
                <h3>Karargâh</h3>
                <span class="app-status status-arge">Veri &amp; Telefon Güvenliği</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Telefon, veri ve sistem güvenliği mimarisi; izinsiz erişim kalkanı, şifreli yerel çalışma alanı ve disiplinli sınav hazırlık karargâhı.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Güvenlik &amp; Kalkan</span>
            <span class="badge" style="font-size: 0.72rem; padding: 2px 8px;">Sistem Koruması</span>
          </div>
        </div>

        <!-- 7. İslam Vakti: Omuz Omuza (Zikirçeker) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-islam-vakti.png" alt="İslam Vakti Logosu" class="app-icon">
              <div class="app-meta">
                <h3>İslam Vakti: Omuz Omuza</h3>
                <span class="app-status">Sürüm Hazırlığında</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Ezan vakitleri, zikirçeker, manevi zincir, Hüdhüd güvenli tarayıcı ve Utrucce irfan kartları içeren kapsamlı manevi yaşam rehberi.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Android • Yerel Hesaplama</span>
            <span class="badge badge-green" style="font-size: 0.72rem; padding: 2px 8px;">Manevi Yaşam</span>
          </div>
        </div>

        <!-- 8. Asayiş Berko -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-asayis-berko.jpg" alt="Asayiş Berko Logosu" class="app-icon">
              <div class="app-meta">
                <h3>Asayiş Berko</h3>
                <span class="app-status status-arge">Ahlak &amp; Güvenlik Kalkanı</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Topluluk koruma mekanizmaları, zararlı içerik filtreleme ve cihaz düzeyinde güvenlik algoritmaları kalkanı.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">İçerik Filtreleme</span>
            <span class="badge" style="font-size: 0.72rem; padding: 2px 8px;">Topluluk Emniyeti</span>
          </div>
        </div>

        <!-- 9. Kıble Bulucu (Konum sensörlü) -->
        <div class="app-card">
          <div>
            <div class="app-top">
              <img src="assets/app-kible-bulucu.png" alt="Kıble Bulucu Gerçek Logosu" class="app-icon">
              <div class="app-meta">
                <h3>Kıble Bulucu</h3>
                <span class="app-status">Donanım Sensörlü Pusula</span>
              </div>
            </div>
            <p class="app-desc text-justify">
              Konum ve manyetik pusula sensörleriyle Kâbe yönünü sıfır hata ile tespit eden, harita entegrasyonlu bağımsız araç.
            </p>
          </div>
          <div class="app-footer">
            <span class="app-tech-pill">Manyetik Sensör &amp; Konum</span>
            <span class="badge badge-green" style="font-size: 0.72rem; padding: 2px 8px;">Yerel Donanım</span>
          </div>
        </div>

      </div>
    </section>

    <!-- İslam Vakti & Kıble Bulucu Canlı Ekran Görüntüleri Galerisi -->
    <section id="goruntuler" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
            İslam Vakti &amp; Kıble Bulucu Canlı Ekran Görüntüleri
          </h2>
          <p class="text-justify">
            Uygulamanın gerçek telefon ekran görüntüleri; donanım destekli kıble pusulası, namaz vakitleri, zikirçeker ve irfan modülleri (Büyütmek için tıklayın):
          </p>
        </div>
        <div class="carousel-nav-btns">
          <button class="carousel-arrow" id="prevScreenshot" aria-label="Önceki">&#8592;</button>
          <button class="carousel-arrow" id="nextScreenshot" aria-label="Sonraki">&#8594;</button>
        </div>
      </div>

      <div class="screenshot-carousel-wrap" data-carousel="islamvakti">
        <div class="screenshot-track" id="screenshotTrack">
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/01_Namaz_Vakitleri_ve_Sayac.png" alt="Namaz Vakitleri ve Sayaç" loading="lazy"></div>
            <div class="phone-caption">⏰ Vakitler &amp; Geri Sayım</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/02_Kible_Pusulasi_ve_Harita.png" alt="Kıble Pusulası ve Harita" loading="lazy"></div>
            <div class="phone-caption">🧭 Kıble Bulucu &amp; Pusula</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/03_Manevi_Bahce_ve_Ciftlik.png" alt="Manevi Bahçe ve Çiftlik" loading="lazy"></div>
            <div class="phone-caption">🌱 Manevi Bahçe &amp; İbadet</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/04_Zikirmatik_ve_Manevi_Zincir.png" alt="Zikirçeker ve Manevi Zincir" loading="lazy"></div>
            <div class="phone-caption">📿 Zikirçeker &amp; Zincir</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/05_Islami_Araclar_ve_Kesfet.png" alt="İslami Araçlar ve Keşfet" loading="lazy"></div>
            <div class="phone-caption">🔍 Araçlar ve Keşfet</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/06_Utrucce_Irfan_Kartlari.png" alt="Utrucce İrfan Kartları" loading="lazy"></div>
            <div class="phone-caption">📜 İrfan Bilgi Kartları</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/07_Hudhud_Guvenli_Tarayici.png" alt="Hüdhüd Güvenli Tarayıcı" loading="lazy"></div>
            <div class="phone-caption">🕊️ Hüdhüd Güvenli Tarayıcı</div>
          </div>
          <div class="phone-mockup" title="Büyütmek için tıklayın">
            <div class="phone-screen-wrap"><img src="assets/08_Pirtil_Medya_Oynatici.png" alt="Pırtıl Medya Oynatıcı" loading="lazy"></div>
            <div class="phone-caption">🎧 Medya &amp; Ses Oynatıcı</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Telegram Eğitim Botlarımız & Bionluk Bağlantısı -->
    <section id="telegram-ekosistemi" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" style="color: var(--color-telegram);"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
            Telegram Eğitim Botlarımız (8 Etkileşimli Bot)
          </h2>
          <p class="text-justify">
            Sınava hazırlık sürecinizi 7/24 destekleyen, soru çözen, tahlil yapan ve akıllı denemeler sunan Telegram botlarımız. İstediğiniz karta tıklayarak hemen Telegram'da başlatabilirsiniz:
          </p>
        </div>
      </div>

      <!-- Bionluk Özel Bağlantı Kartı -->
      <div class="bionluk-banner-card">
        <div class="bionluk-content">
          <div class="bionluk-badge">Bionluk Uzman Hizmeti</div>
          <h3>utrucce - Metin ve Video Editörü | Bionluk</h3>
          <p class="text-justify">
            Edebi metin tahlili, soru kitapçığı dizgisi, redaksiyon, eğitim içerikleri üretimi ve video kurgu alanındaki profesyonel çalışmalarımız için Bionluk profilimizi doğrudan ziyaret edebilirsiniz.
          </p>
        </div>
        <a href="https://bionluk.com/utrucce" target="_blank" rel="noopener noreferrer" class="btn btn-bionluk">
          Bionluk Profiline Git &rarr;
        </a>
      </div>

      <!-- Telegram Tanıtım Panosu -->
      <div class="telegram-banner-box zoomable" title="Büyütmek için tıklayın">
        <img src="assets/telegram-banner.png" alt="Telegram Bot Tanıtım Panosu" loading="lazy">
      </div>

      <!-- Telegram Botları Izgarası (8 Bot) -->
      <div class="bots-grid">

        <!-- 1. Pırtıl -->
        <a href="https://t.me/PirtilTurkceBot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-pirtil.jpg" alt="Pırtıl Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Pırtıl 🐛</h3>
                <span class="bot-badge">@PirtilTurkceBot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Türkçe ÖABT ve M<span class="sigma">Σ</span>B-AGS adayları için interaktif soru çözüm, konu anlatım ve pratik öğrenme asistanı.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 2. BayYazar -->
        <a href="https://t.me/BayYazar_Bot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-bayyazar.jpg" alt="BayYazar Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>BayYazar ✍️</h3>
                <span class="bot-badge">@BayYazar_Bot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Türk ve Dünya edebiyatında eser-yazar eşleştirmeleri, edebi dönemler ve akılda kalıcı hafıza teknikleri motoru.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 3. Mergen -->
        <a href="https://t.me/Mergen_DenemeBot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-mergen.jpg" alt="Mergen Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Mergen 🏹</h3>
                <span class="bot-badge">@Mergen_DenemeBot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Zaman ayarlı deneme sınavları, puan hesaplama modülleri ve net analizi sunan akıllı ölçme ve değerlendirme botu.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 4. Kırçıl Pehlivan -->
        <a href="https://t.me/Kircil_Pehlivanbot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-kircil.jpg" alt="Kırçıl Pehlivan Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Kırçıl Pehlivan 🤼</h3>
                <span class="bot-badge">@Kircil_Pehlivanbot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Zorluk derecesi yüksek çeldiricili sorularla pehlivan meydanında adayları sınava hazırlayan antrenman botu.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 5. Mısra-ı Berceste -->
        <a href="https://t.me/Berceste_EdebiBot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-berceste.jpg" alt="Mısra-ı Berceste Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Mısra-ı Berceste 📜</h3>
                <span class="bot-badge">@Berceste_EdebiBot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Eski Türk Edebiyatı, Divan şiiri, aruz vezni, edebi sanatlar ve şerh çalışmalarına odaklı derinlikli edebiyat botu.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 6. Pıtrak -->
        <a href="https://t.me/Pitrak_EtiketBot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-pitrak.jpg" alt="Pıtrak Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Pıtrak 🏷️</h3>
                <span class="bot-badge">@Pitrak_EtiketBot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Kavram haritaları, etiketli pratik soru havuzu ve görsel hafıza kartlarıyla hızlı tekrar imkânı sunan arşiv botu.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 7. Asayiş Berkemal -->
        <a href="https://t.me/Ahlak_KalkanBot" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-asayis.jpg" alt="Asayiş Berkemal Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Asayiş Berkemal 🛡️</h3>
                <span class="bot-badge">@Ahlak_KalkanBot</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Akademi Pırtılları ve eğitim gruplarında spam ve huzur kaçıran içerikleri engelleyen ahlak ve düzen kalkanı.</p>
          </div>
          <div class="bot-btn">
            <span>Bota Git</span> &rarr;
          </div>
        </a>

        <!-- 8. Muallim-i Sani -->
        <a href="https://t.me/pirtillaturkceoabt" target="_blank" rel="noopener noreferrer" class="bot-card">
          <div>
            <div class="bot-top">
              <img src="assets/bot-muallim.jpg" alt="Muallim-i Sani Bot" class="bot-avatar">
              <div class="bot-meta">
                <h3>Muallim-i Sani 🎓</h3>
                <span class="bot-badge">Eğitim Rehberi</span>
              </div>
            </div>
            <p class="bot-desc text-justify">Farabi'nin izinde ikinci öğretmen düsturuyla dilbilim, pedagoji ve metin şerhi alanında adaylara rehberlik eden başöğretici.</p>
          </div>
          <div class="bot-btn">
            <span>Toplulukta Keşfet</span> &rarr;
          </div>
        </a>

      </div>

      <!-- Telegram Topluluklarımız ve Gruplarımız -->
      <div class="section-head" style="margin-top: 45px;">
        <div>
          <h3 style="font-size: 1.35rem; font-weight: 800; margin: 0 0 6px;">Telegram Topluluklarımız ve Gruplarımız</h3>
          <p class="text-justify">Öğretmen adayları ve öğrencilerin soru tartıştığı ve bilgi paylaştığı etkileşimli kanallarımız:</p>
        </div>
      </div>

      <div class="groups-grid">

        <!-- 1. ALΣF Türkçe ÖABT | Akademi Pırtılları -->
        <a href="https://t.me/pirtillaturkceoabt" target="_blank" rel="noopener noreferrer" class="group-card">
          <div>
            <div class="group-header">
              <div class="group-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              </div>
              <div class="group-title">
                <h3>AL<span class="sigma">Σ</span>F Türkçe ÖABT<br>Akademi Pırtılları 🐛🍊</h3>
                <span>@pirtillaturkceoabt</span>
              </div>
            </div>
            <p class="group-desc text-justify">Türkçe Öğretmenliği ÖABT sınavına hazırlanan adayların ana soru tartışma, rehberlik ve dayanışma topluluğu.</p>
          </div>
          <div class="group-cta">
            <span>Gruba Katıl &rarr;</span>
          </div>
        </a>

        <!-- 2. Türkçe ÖABT Anket Grubu -->
        <a href="https://t.me/turkceoabtanket" target="_blank" rel="noopener noreferrer" class="group-card">
          <div>
            <div class="group-header">
              <div class="group-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
              </div>
              <div class="group-title">
                <h3>Türkçe ÖABT Anket Grubu 📊</h3>
                <span>@turkceoabtanket</span>
              </div>
            </div>
            <p class="group-desc text-justify">Her gün yayınlanan özgün anket soruları, çeldirici analizleri ve anlık doğru/yanlış geri bildirimleriyle hızlı antrenman kanalı.</p>
          </div>
          <div class="group-cta">
            <span>Gruba Katıl &rarr;</span>
          </div>
        </a>

        <!-- 3. ALΣF MEB-AGS -->
        <a href="https://t.me/alefags" target="_blank" rel="noopener noreferrer" class="group-card">
          <div>
            <div class="group-header">
              <div class="group-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
              </div>
              <div class="group-title">
                <h3>AL<span class="sigma">Σ</span>F M<span class="sigma">Σ</span>B - AGS 🏛️</h3>
                <span>@alefags</span>
              </div>
            </div>
            <p class="group-desc text-justify">Millî Eğitim Bakanlığı Akademi Giriş Sınavı (M<span class="sigma">Σ</span>B-AGS) müfredatına özel mevzuat, eğitim bilimleri ve genel yetenek grubu.</p>
          </div>
          <div class="group-cta">
            <span>Gruba Katıl &rarr;</span>
          </div>
        </a>

        <!-- 4. ALΣF Pırtılları YKS -->
        <a href="https://t.me/alefyks" target="_blank" rel="noopener noreferrer" class="group-card">
          <div>
            <div class="group-header">
              <div class="group-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
              </div>
              <div class="group-title">
                <h3>AL<span class="sigma">Σ</span>F Pırtılları YKS 🎯</h3>
                <span>@alefyks</span>
              </div>
            </div>
            <p class="group-desc text-justify">Yükseköğretim Kurumları Sınavı (TYT Türkçe &amp; AYT Edebiyat) adayları için soru çözümleri, taktikler ve rehberlik alanı.</p>
          </div>
          <div class="group-cta">
            <span>Gruba Katıl &rarr;</span>
          </div>
        </a>

      </div>
    </section>

    <!-- Sosyal Medya ve İletişim Kanallarımız -->
    <section id="iletisim" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            Sosyal Medya ve İletişim Kanallarımız
          </h2>
          <p class="text-justify">Geliştirici ve Yazar Sertan Çubukcu ile doğrudan bağlantı kurun veya eğitim yayınlarımızı takip edin:</p>
        </div>
      </div>

      <div class="social-grid">

        <!-- 1. YouTube -->
        <a href="https://www.youtube.com/@1dakidat%C3%BCrk%C3%A7e%C3%B6abt" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #ff0000; background: rgba(255, 0, 0, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </div>
          <div class="social-meta">
            <h3>YouTube</h3>
            <span>1 Dakikada Türkçe ÖABT</span>
          </div>
        </a>

        <!-- 2. Instagram -->
        <a href="https://www.instagram.com/sertancubukcu/" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #e1306c; background: rgba(225, 48, 108, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </div>
          <div class="social-meta">
            <h3>Instagram</h3>
            <span>@sertancubukcu</span>
          </div>
        </a>

        <!-- 3. LinkedIn -->
        <a href="https://www.linkedin.com/in/sertan%C3%A7ubukcu/" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #0a66c2; background: rgba(10, 102, 194, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </div>
          <div class="social-meta">
            <h3>LinkedIn</h3>
            <span>Sertan Çubukcu</span>
          </div>
        </a>

        <!-- 4. Gmail (SADECE sertancubukcu@gmail.com) -->
        <a href="mailto:sertancubukcu@gmail.com" class="social-card" data-copy-email>
          <div class="social-icon-box" style="color: #ea4335; background: rgba(234, 67, 53, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L12 9.491l8.073-5.998C21.69 2.28 24 3.434 24 5.457z"/></svg>
          </div>
          <div class="social-meta">
            <h3>Gmail</h3>
            <span>sertancubukcu@gmail.com</span>
          </div>
        </a>

        <!-- 5. Bionluk -->
        <a href="https://bionluk.com/utrucce" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #00b274; background: rgba(0, 178, 116, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"></circle></svg>
          </div>
          <div class="social-meta">
            <h3>Bionluk</h3>
            <span>utrucce</span>
          </div>
        </a>

      </div>
    </section>

  </main>

  <!-- Altbilgi (Footer) - "Bütün hakları saklıdır" kuralına tam uyumlu -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div style="display: flex; align-items: center; gap: 12px;">
          <img src="assets/kurt.png" alt="Kurt Arma" style="width: 34px; height: 34px; border-radius: 6px;">
          <div>
            <strong style="color: #fff; display: block; font-size: 1rem;">AL<span class="sigma">Σ</span>F Eğitim Ekosistemi</strong>
            <span style="font-size: 0.8rem; color: var(--text-muted);">M<span class="sigma">Σ</span>B - AGS &amp; Türkçe ÖABT Hazırlık</span>
          </div>
        </div>
        <div>
          <a href="privacy.html" class="btn btn-outline" style="font-size: 0.84rem;">
            Gizlilik Politikası ve Güvenlik Protokolü &rarr;
          </a>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS • Yazar &amp; Geliştirici: Sertan Çubukcu. Bütün hakları saklıdır.
      </div>
    </div>
  </footer>

  <!-- Büyük Görüntüleyici (Lightbox Modal) -->
  <div id="lightboxModal" class="lightbox-modal" role="dialog" aria-modal="true" aria-label="Görsel Büyütücü">
    <button id="lightboxClose" class="lightbox-close" aria-label="Kapat">&times;</button>
    <div class="lightbox-content">
      <img id="lightboxImg" src="" alt="Genişletilmiş Görüntü">
      <div id="lightboxCaption" class="lightbox-caption"></div>
    </div>
  </div>

  <!-- Bildirim Kutusu (Toast) -->
  <div id="toastNotice" class="toast-notice"></div>

  <script src="script.js"></script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print("Updated index.html with Hâl Tercümesi successfully.")
