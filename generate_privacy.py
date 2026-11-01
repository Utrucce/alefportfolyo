# -*- coding: utf-8 -*-
"""
Generator for privacy.html (Google Play Store & GDPR/KVKK Compliant Privacy Policy Portal)
"""

import os

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

html_content = """<!DOCTYPE html>
<html lang="tr" data-lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#07080e">
  <title>ALΣF | Gizlilik Politikası ve Güvenlik Protokolü (GDPR &amp; KVKK)</title>
  <meta name="description" content="Sertan Çubukcu tarafından geliştirilen ve yayınlanan BÜTÜN mobil uygulamalar (ALΣF MEB-AGS, ALΣF Türkçe ÖABT, ALΣF KPSS, ALΣF EKYS, İslam Vakti, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko) için Google Play Store, KVKK ve GDPR uyumlu gizlilik politikası ve veri güvenliği bildirimi.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Animasyonlu Rengârenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <!-- Optik Cam Kırılması İçin Referans Görsel (RainyDay.js) -->
  <img id="nanoBgRef" src="assets/site_bg_nano.png" style="display:none;" alt="Arka Plan Referansı" crossorigin="anonymous">

  <!-- Şimşek Çakması Işık Katmanı -->
  <div id="lightningFlashOverlay" aria-hidden="true"></div>

  <!-- Optik Cam Kırılması İçin Referans Görsel (RainyDay.js) -->
  <img id="nanoBgRef" src="assets/site_bg_nano.png" style="display:none;" alt="Arka Plan Referansı" crossorigin="anonymous">

  <!-- Animasyonlu Rengarenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <canvas id="mythicBgCanvas"></canvas>

  <!-- Uçuşan 3B Fotoğrafik Eterik Kelebekler (Orijinal Morfo Kanatları) -->
  <div id="butterflyContainer" aria-hidden="true"></div>

  <!-- Ekranın Altında Dalgalanan Doğal Okyanus (Paralaks Destekli) -->
  <canvas id="oceanWavesCanvas" aria-hidden="true"></canvas>

  <!-- 3B WebGL Kambur Balina & Okyanus Sıçraması Tuvali (Three.js 3D Humpback Whale & Breach) -->
  <canvas id="whaleThreeCanvas" aria-hidden="true"></canvas>

  <!-- Gerçekçi Optik Cam Islanması & Su Damlaları (RainyDay.js + Fiziksel Su Lensi) -->
  <div id="rainyGlassContainer" aria-hidden="true"></div>
  <canvas id="screenSplashCanvas" aria-hidden="true"></canvas>

  <button id="summonWhaleBtn" class="whale-trigger-btn" aria-label="Balinayı Zıplat" title="Mitolojik Balinayı Çağır">
    <span style="font-size: 1.15rem;">🌊</span> Balinayı Zıplat <span style="font-size: 1.15rem;">🐋</span>
  </button>


  <!-- Arka Plan Küreleri -->
  <div class="orb orb-1" aria-hidden="true"></div>
  <div class="orb orb-2" aria-hidden="true"></div>
  <div class="orb orb-3" aria-hidden="true"></div>

  <!-- Üst Gezinme Çubuğu (Mobilde Göreceli / Relative) -->
  <header class="site-header">
    <div class="container nav-wrapper">
      <a href="index.html" class="brand-group" aria-label="ALΣF Ana Sayfa">
        <div class="brand-logos">
          <img src="assets/kurt.png" alt="Kurt Arma" class="nav-logo-thumb">
          <img src="assets/logo-photoroom.png" alt="Sertan Çubukcu Logo" class="nav-logo-thumb">
          <img src="assets/alef-logo.png" alt="ALΣF Logo" class="nav-logo-thumb">
        </div>
        <div class="brand-text">
          <h1>AL<span class="sigma">Σ</span>F</h1>
        </div>
      </a>

      <!-- Gezinme Bağlantıları -->
      <nav class="nav-links">
        <a href="index.html">Ana Sayfa</a>
        <a href="index.html#hal-tercumesi">Hâl Tercümesi</a>
        <a href="#politika">Güvenlik İlkeleri</a>
        <a href="#gdpr-kvkk">GDPR &amp; KVKK</a>
        <a href="#goruntuler">Uygulama Görüntüleri</a>
        <a href="#yayinlar">Yayınlar</a>
        <a href="#iletisim">İletişim</a>
      </nav>

      <!-- Dil Seçici -->
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

    <!-- Giriş (Hero) Başlığı -->
    <section class="hero" id="tanitim">
      <div class="badge badge-green">
        <span class="badge-dot"></span>
        <span>Google Play Store • EğitimYayın • KVKK • GDPR Uyumlu Resmî Güvenlik Belgesi</span>
      </div>

      <h1 class="hero-title">
        AL<span class="sigma">Σ</span>F<br>
        <span class="text-gradient">Gizlilik Politikası ve Güvenlik Protokolü</span>
      </h1>

      <p class="hero-subtitle text-justify">
        Bu Gizlilik Politikası ve Güvenlik Protokolü; geliştirici ve yazar Sertan Çubukcu tarafından geliştirilen ve yayınlanan <strong>BÜTÜN mobil uygulamalar</strong> (AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS, AL<span class="sigma">Σ</span>F Türkçe ÖABT, AL<span class="sigma">Σ</span>F KPSS, AL<span class="sigma">Σ</span>F EKYS, İslam Vakti: Omuz Omuza, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko ve gelecekte yayınlanacak bütün sürümler), EğitimYayın Mağazası, Google Play Kitapları, çevrim içi internet servisleri ve Telegram eğitim botları ekosistemi için eksiksiz ve resmi güvenlik beyanıdır.
      </p>

      <div style="font-size: 0.88rem; color: var(--color-cyan-light); margin-bottom: 20px;">
        Son Güncelleme: <strong>Ekim 2026 / October 2026</strong> • Sürüm: <strong>v1.2.6</strong>
      </div>

      <div class="action-bar">
        <button id="copyPolicyBtn" class="btn btn-copy">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          Google Play İçin Metni Kopyala
        </button>
        <a href="index.html" class="btn btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          Ana Sayfaya Dön
        </a>
        <a href="#goruntuler" class="btn btn-green">Uygulama Görüntüleri</a>
        <a href="#yayinlar" class="btn btn-store">EğitimYayın &amp; Kitaplar</a>
      </div>
    </section>

    <!-- Geliştirici ve Marka Logoları -->
    <div class="social-grid" style="margin-bottom: 45px;">
      <div class="social-card">
        <img src="assets/mebags_phone_icon.png" alt="MEB-AGS Logo" style="width: 48px; height: 48px; border-radius: 10px;">
        <div class="social-meta">
          <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS</h3>
          <span style="font-size: 0.8rem; color: var(--text-muted);">Android Mobil Hazırlık Uygulaması</span>
        </div>
      </div>
      <div class="social-card">
        <img src="assets/alef_turkce_oabt_orange.png" alt="Türkçe ÖABT Turuncu Logo" style="width: 48px; height: 48px; border-radius: 10px;">
        <div class="social-meta">
          <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">AL<span class="sigma">Σ</span>F Türkçe ÖABT</h3>
          <span style="font-size: 0.8rem; color: var(--text-muted);">Alan Bilgisi Hazırlık Platformu</span>
        </div>
      </div>
      <div class="social-card">
        <img src="assets/logo-photoroom.png" alt="Sertan Çubukcu Logo" style="width: 48px; height: 48px; border-radius: 10px;">
        <div class="social-meta">
          <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">Sertan Çubukcu</h3>
          <span style="font-size: 0.8rem; color: var(--text-muted);">Geliştirici &amp; Yazar Kurumsal Kimliği</span>
        </div>
      </div>
      <div class="social-card">
        <img src="assets/kurt.png" alt="Kurt Arma" style="width: 48px; height: 48px; border-radius: 10px;">
        <div class="social-meta">
          <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">Kurt Arma</h3>
          <span style="font-size: 0.8rem; color: var(--text-muted);">Özgün Mühür &amp; Güvenlik Simgesi</span>
        </div>
      </div>
    </div>

    <!-- Gizlilik Politikası Ana Metni (Türkçe / English / Bilingual) -->
    <section class="policy-box" id="politika">
      <div class="dual-lang-container">

        <!-- TÜRKÇE GİZLİLİK POLİTİKASI -->
        <article class="content-tr policy-full-tr" lang="tr">
          
          <div class="policy-clause">
            <h3>1. Veri Sorumlusu ve Bütün Uygulamaları Kapsayan Genel Hüküm</h3>
            <p class="text-justify">
              Bu Gizlilik Politikası ve Güvenlik Protokolü, geliştirici ve yazar <strong>Sertan Çubukcu</strong> tarafından geliştirilen ve yayınlanan <strong>BÜTÜN mobil uygulamalar</strong> (AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS, AL<span class="sigma">Σ</span>F Türkçe ÖABT, AL<span class="sigma">Σ</span>F KPSS, AL<span class="sigma">Σ</span>F EKYS, İslam Vakti: Omuz Omuza, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko ve gelecekte yayınlanacak bütün mobil sürümler ile projeler), <strong>EğitimYayın Mağazası</strong>, <strong>Google Play Kitapları</strong>, çevrim içi internet servisleri ve Telegram eğitim botları ekosisteminin veri güvenliği ve gizlilik standartlarını belirler. Bu politika bildirimi, sayılan ve yayınlanan uygulamaların <strong>bütünü</strong> için istisnasız, eksiksiz ve bağlayıcı olarak geçerlidir.
            </p>
            <div class="policy-highlight-box">
              <strong>Veri Sorumlusu:</strong> Sertan Çubukcu<br>
              <strong>E-posta:</strong> sertancubukcu@gmail.com<br>
              <strong>Kapsam:</strong> Geliştiricinin Bütün Mobil Uygulamaları ve Eğitim Ekosistemi<br>
              <strong>Yetkili Portal:</strong> ALΣF Eğitim ve Yayıncılık Ekosistemi
            </div>
          </div>

          <div class="policy-clause">
            <h3>2. Toplanan ve Toplanmayan Veriler (Sıfır Kişisel Veri İlkesi)</h3>
            <p class="text-justify">
              Uygulamalarımız kullanıcı gizliliğini temel tasarım ilkesi olarak kabul eder. 
              Uygulamayı kullanırken adınız, soyadınız, T.C. kimlik numaranız, telefon numaranız, 
              e-posta adresiniz veya rehber bilgileriniz <strong>kesinlikle toplanmaz, işlenmez ve sunucularımıza aktarılmaz</strong>.
            </p>
            <p class="text-justify">
              Uygulama içerisinde kullanıcı hesabı açma zorunluluğu bulunmamaktadır. Adaylar uygulamayı anonim olarak 
              ve internet bağlantısına ihtiyaç duymadan çevrim dışı biçimde kullanabilirler.
            </p>
          </div>

          <div class="policy-clause">
            <h3>3. Cihaz İçi Yerel Depolama (On-Device Storage)</h3>
            <p class="text-justify">
              Kullanıcının soru çözme ilerlemesi, çözülen deneme sonuçları, puan istatistikleri, 
              kaydedilen ders notları ve favori bilgi kartları <strong>yalnızca kullanıcının kendi cihazında</strong> 
              (yerel SharedPreferences ve yerel SQLite veritabanı içerisinde) saklanır. 
              Bu veriler hiçbir harici bulut sunucusuna gönderilmez; tamamen cihaz sahibinin denetimindedir.
            </p>
          </div>

          <div class="policy-clause">
            <h3>4. Konum ve Donanım İzinleri</h3>
            <p class="text-justify">
              Uygulama paketlerimiz içerisindeki kıble bulma ve namaz vakitleri araçlarında (İslam Vakti &amp; Kıble Bulucu), 
              cihazın pusula sensörü ve anlık konum bilgisi <strong>yalnızca yerel matematiksel açı hesaplaması</strong> amacıyla kullanılır.
            </p>
            <div class="policy-highlight-box cyan">
              <strong>Konum Güvenliği:</strong> Cihazın konum koordinatları hiçbir sunucuya iletilmez, 
              uzak bir veritabanına kaydedilmez veya üçüncü taraflarla paylaşılmaz. Hesaplama tamamlandıktan sonra anlık bellekten silinir.
            </div>
          </div>

          <div class="policy-clause">
            <h3>5. Üçüncü Taraf SDK'lar ve Google Play Hizmetleri</h3>
            <p class="text-justify">
              Uygulamalarımız, Android işletim sistemi standartlarına uygun olarak Google Play Hizmetleri (Google Play Services) 
              ve Google AdMob altyapısını kullanabilir. Bu servisler, Google'ın kendi gizlilik ilkeleri çerçevesinde 
              anonimleştirilmiş cihaz tanıtıcısı (Advertising ID), çökme teşhis raporları (Crashlytics) ve temel performans analitiği toplayabilir.
            </p>
            <p class="text-justify">
              Kullanıcılar cihazlarının "Ayarlar &gt; Google &gt; Reklamlar" menüsünden kişiselleştirilmiş reklam kimliğini diledikleri zaman sıfırlayabilir veya devre dışı bırakabilirler.
            </p>
          </div>

          <div class="policy-clause" id="gdpr-kvkk">
            <h3>6. AB Genel Veri Koruma Tüzüğü (GDPR) Uyumluluk Beyanı</h3>
            <p class="text-justify">
              Avrupa Birliği Genel Veri Koruma Tüzüğü (GDPR - General Data Protection Regulation) uyarınca, 
              Avrupa Ekonomik Alanı (AEA) içerisindeki kullanıcılarımıza aşağıdaki yasal güvenceler sunulmaktadır:
            </p>
            <ul style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px;">
              <li><strong>Hukuki Sebep (GDPR Madde 6):</strong> Uygulamalarımızda kişisel veri işlenmemektedir. Yerel tercihler kullanıcının rızası ve meşru menfaat temelinde cihazda tutulur.</li>
              <li><strong>Erişim ve Düzeltme Hakkı (Madde 15-16):</strong> Kullanıcı bütün verilerine cihaz üzerindeki panellerden anında erişebilir.</li>
              <li><strong>Silme ve Unutulma Hakkı (Madde 17):</strong> Harici sunucuda hiçbir veri tutulmadığı için cihaz ayarlarından uygulama verilerini temizleyerek bütün veriler anında kalıcı olarak silinir.</li>
              <li><strong>İtiraz ve Kısıtlama Hakkı (Madde 18-21):</strong> Kullanıcı cihaz izinlerini (konum, bildirim) dilediği an kapatabilir.</li>
              <li><strong>Denetim Makamına Şikâyet Hakkı (Madde 77):</strong> Kullanıcılar ilgili veri koruma denetim otoritesine başvurma hakkına sahiptir.</li>
            </ul>
          </div>

          <div class="policy-clause">
            <h3>7. 6698 Sayılı KVKK Uyarınca Kullanıcı Hakları</h3>
            <p class="text-justify">
              Türkiye Cumhuriyeti 6698 sayılı Kişisel Verilerin Korunması Kanunu'nun (KVKK) 11. maddesi uyarınca kullanıcılar; 
              kişisel verilerinin işlenip işlenmediğini öğrenme, işlenmişse bilgi talep etme ve verilerin silinmesini isteme hakkına sahiptir. 
              Uygulamamız sunucu tarafında hiçbir kimlik veya profil verisi barındırmadığından, bu haklar cihaz düzeyinde tam koruma altındadır.
            </p>
          </div>

          <div class="policy-clause" id="cocuk-guvenligi">
            <h3>8. Çocukların Gizliliği (COPPA &amp; Google Play Aile Politikası)</h3>
            <p class="text-justify">
              Uygulamalarımız genel kitleye, öğretmen adaylarına ve öğrencilere yöneliktir. 
              13 yaşın altındaki çocuklardan bilerek ve isteyerek hiçbir kişisel bilgi toplanmamaktadır. 
              COPPA (Children's Online Privacy Protection Act) ve Google Play Aile Politikaları gereksinimlerine tam uyum sağlanmaktadır.
            </p>
          </div>

          <div class="policy-clause">
            <h3>9. Veri Silme, Sıfırlama ve Kullanıcı Talepleri</h3>
            <p class="text-justify">
              Uygulamada depolanan bütün test, soru ve deneme verilerini sıfırlamak isteyen kullanıcılar; 
              telefonlarının <strong>Ayarlar &gt; Uygulamalar &gt; ALΣF &gt; Depolama &gt; Verileri Temizle</strong> adımını izleyerek 
              veya uygulamayı cihazlarından kaldırarak bütün yerel verileri anında ve geri döndürülemez biçimde yok edebilirler.
            </p>
          </div>

          <div class="policy-clause">
            <h3>10. Kriptografik Lisans ve Telif Koruması</h3>
            <p class="text-justify">
              Eğitim materyalleri, deneme soruları ve ders notları 5846 sayılı Fikir ve Sanat Eserleri Kanunu ile uluslararası telif mevzuatıyla korunmaktadır. 
              Uygulama kodları ve dijital lisanslar kriptografik token ve imza doğrulaması ile güvence altına alınmıştır.
            </p>
          </div>

          <div class="policy-clause">
            <h3>11. İletişim Bilgileri</h3>
            <p class="text-justify">
              Gizlilik politikamız, veri güvenliği süreçlerimiz veya telif bildirimleri ile ilgili her türlü soru, 
              öneri ve resmi talepleriniz için doğrudan geliştiriciye ulaşabilirsiniz:
            </p>
            <div class="policy-highlight-box purple">
              <strong>Geliştirici &amp; Yazar:</strong> Sertan Çubukcu<br>
              <strong>E-posta:</strong> sertancubukcu@gmail.com<br>
              <strong>Bionluk Profili:</strong> <a href="https://bionluk.com/utrucce" target="_blank" rel="noopener noreferrer" style="color: var(--color-cyan-light);">bionluk.com/utrucce</a><br>
              <strong>YouTube:</strong> 1 Dakikada Türkçe ÖABT
            </div>
          </div>

        </article>

        <!-- ENGLISH PRIVACY POLICY (GOOGLE PLAY COMPLIANT) -->
        <article class="content-en policy-full-en" lang="en" hidden>
          
          <div class="policy-clause">
            <h3>1. Data Controller &amp; Comprehensive Scope for All Applications</h3>
            <p class="text-justify">
              This Privacy Policy and Security Protocol applies comprehensively to <strong>ALL mobile applications</strong> developed and published by <strong>Sertan Çubukcu</strong> (including ALΣF - MEB - AGS, ALΣF Türkçe ÖABT, ALΣF KPSS, ALΣF EKYS, İslam Vakti: Omuz Omuza, Qibla Finder, Karargâh, Mergen, Pırtıl, Asayiş Berko, and all current and future releases), the <strong>EğitimYayın Store</strong>, <strong>Google Play Books</strong>, associated web services, and Telegram educational bots. This policy is binding and universally applicable to all software products of the developer.
            </p>
            <div class="policy-highlight-box">
              <strong>Data Controller:</strong> Sertan Çubukcu<br>
              <strong>Email:</strong> sertancubukcu@gmail.com<br>
              <strong>Scope:</strong> All Current and Future Mobile Applications<br>
              <strong>Ecosystem:</strong> ALΣF Educational &amp; Publishing Ecosystem
            </div>
          </div>

          <div class="policy-clause">
            <h3>2. Information We Collect (Zero Personal Data Principle)</h3>
            <p class="text-justify">
              Our applications are built with privacy by design. We <strong>do not collect, transmit, store, or sell</strong> 
              any personal information such as your real name, national ID, phone number, email address, or contacts. 
              No user account or registration is required to use the full functionality of the apps.
            </p>
          </div>

          <div class="policy-clause">
            <h3>3. On-Device Local Data Storage</h3>
            <p class="text-justify">
              All learning progress, solved questions, exam scores, flashcards, and preferences are stored 
              <strong>strictly locally on your device</strong> using secure local SQLite and SharedPreferences. 
              This data never leaves your device and is never synced to external servers without explicit user request.
            </p>
          </div>

          <div class="policy-clause">
            <h3>4. Device Hardware &amp; Location Permissions</h3>
            <p class="text-justify">
              For companion utility modules requiring direction calculation (such as Qibla compass and local prayer times), 
              the app accesses device compass sensors and coarse/fine location strictly in real-time.
            </p>
            <div class="policy-highlight-box cyan">
              <strong>Location Privacy Guarantee:</strong> Location coordinates are processed exclusively on the user's device 
              and are neither transmitted to external servers nor logged permanently.
            </div>
          </div>

          <div class="policy-clause">
            <h3>5. Third-Party Services &amp; Google Play SDKs</h3>
            <p class="text-justify">
              The applications may integrate standard Google Play Services and Google AdMob SDKs for non-personalized advertising, 
              diagnostic crash reports, and system integrity verification. These third-party services operate in accordance with Google's Privacy Policy. 
              Users may reset or opt-out of ad tracking at any time via Android device settings (Settings &gt; Google &gt; Ads).
            </p>
          </div>

          <div class="policy-clause">
            <h3>6. General Data Protection Regulation (GDPR) Disclosure</h3>
            <p class="text-justify">
              In compliance with the European Union GDPR, users residing in the European Economic Area (EEA) benefit from the following rights:
            </p>
            <ul style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px;">
              <li><strong>Legal Basis (GDPR Art. 6):</strong> The app processes zero personal data. Necessary local preferences are stored on legitimate interest and user consent.</li>
              <li><strong>Rights of Access &amp; Rectification (Art. 15-16):</strong> Users maintain direct control over all data stored within the app interface.</li>
              <li><strong>Right to Erasure (Art. 17):</strong> Since no data is retained on external servers, uninstalling the application or clearing app data instantly deletes all local records.</li>
              <li><strong>Right to Lodge a Complaint (Art. 77):</strong> Users have the right to lodge a complaint with an appropriate supervisory data protection authority.</li>
            </ul>
          </div>

          <div class="policy-clause">
            <h3>7. Children's Privacy (COPPA &amp; Family Policy)</h3>
            <p class="text-justify">
              Our applications comply with COPPA (Children's Online Privacy Protection Act) and the Google Play Families Policy. 
              We do not knowingly collect or solicit personal information from children under the age of 13.
            </p>
          </div>

          <div class="policy-clause">
            <h3>8. Data Deletion and Retention</h3>
            <p class="text-justify">
              Users can erase all data at any time by going to: 
              <strong>Android Settings &gt; Apps &gt; ALΣF &gt; Storage &gt; Clear Data</strong>, 
              or simply by uninstalling the application from their device.
            </p>
          </div>

          <div class="policy-clause">
            <h3>9. Contact Information</h3>
            <p class="text-justify">
              If you have any questions, inquiries, or feedback regarding this Privacy Policy and Security Protocol, please contact:
            </p>
            <div class="policy-highlight-box purple">
              <strong>Developer:</strong> Sertan Çubukcu<br>
              <strong>Email:</strong> sertancubukcu@gmail.com<br>
              <strong>Bionluk Profile:</strong> <a href="https://bionluk.com/utrucce" target="_blank" rel="noopener noreferrer" style="color: var(--color-cyan-light);">bionluk.com/utrucce</a>
            </div>
          </div>

        </article>

      </div>
    </section>

    <!-- Uygulama Ekran Görüntüleri Galerisi -->
    <section class="screenshots-section" id="goruntuler">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
            Uygulama Ekran Görüntüleri
          </h2>
          <p class="text-justify">Uygulamalarımızın mobil arayüzleri, test modülleri ve güvenlik mimarisi (Büyütmek için tıklayın):</p>
        </div>
        <div class="carousel-nav-btns">
          <button id="prevScreenshot" class="carousel-arrow" aria-label="Önceki">&#8592;</button>
          <button id="nextScreenshot" class="carousel-arrow" aria-label="Sonraki">&#8594;</button>
        </div>
      </div>

      <div class="carousel-track" id="screenshotTrack">
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_1.png" alt="ALΣF Giriş ve Ana Menü" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Giriş ve Ana Menü</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_2.png" alt="ALΣF Modül ve Konu Seçimi" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Modül ve Konu Seçimi</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_3.png" alt="ALΣF Soru Listesi" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Soru Listesi &amp; Filtreler</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_4.png" alt="ALΣF Soru Çözümü" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Soru Çözümü &amp; Açıklamalar</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_5.png" alt="ALΣF Performans İstatistikleri" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Performans İstatistikleri</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_6.png" alt="ALΣF Zaman Ayarlı Deneme Sınavı" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Zaman Ayarlı Deneme Sınavı</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_7.png" alt="ALΣF Kişiselleştirilmiş Notlar" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Kişiselleştirilmiş Notlar</span></div>
          </div>
        </div>
        <div class="phone-mockup" title="Büyütmek için tıklayın">
          <div class="phone-screen">
            <img src="assets/ekran_goruntusu_8.png" alt="ALΣF Sınav Geri Sayımı" loading="lazy">
            <div class="phone-overlay"><span class="phone-caption">Sınav Geri Sayımı &amp; Raporlar</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bionluk Özel Banner -->
    <div class="bionluk-banner-card" style="margin: 40px 0;">
      <div>
        <div class="bionluk-badge">Bionluk Uzman Hizmeti</div>
        <h3 style="font-size: 1.35rem; font-weight: 800; color: #fff; margin: 0 0 6px;">utrucce - Metin ve Video Editörü | Bionluk</h3>
        <p class="text-justify" style="color: var(--text-secondary); margin: 0; font-size: 0.94rem;">
          Metin tahlili, soru kitapçığı redaksiyonu, kitap mizanpajı ve profesyonel editörlük hizmetleri için Bionluk profilimizi ziyaret edebilirsiniz.
        </p>
      </div>
      <a href="https://bionluk.com/utrucce" target="_blank" rel="noopener noreferrer" class="btn btn-bionluk">
        Bionluk Profiline Git &rarr;
      </a>
    </div>

    <!-- Yayınlar & Kitaplar Bölümü -->
    <section id="yayinlar" style="margin: 50px 0 65px;">
      <div class="section-head">
        <div>
          <h2>
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            Yayın Mağazası &amp; Google Play Kitapları
          </h2>
          <p class="text-justify">Sertan Çubukcu tarafından kaleme alınan lisanslı eğitim yayınları ve dijital eserler:</p>
        </div>
      </div>

      <!-- EğitimYayın Mağaza Kartı -->
      <div class="store-banner">
        <img src="assets/google_play_developer_logo.jpg" alt="EğitimYayın Logo" class="store-banner-logo">
        <div style="flex: 1;">
          <div class="badge badge-green" style="margin-bottom: 6px;"><span class="badge-dot"></span>Resmî Satış &amp; Dağıtım Mağazası</div>
          <h3 style="font-size: 1.4rem; font-weight: 800; margin: 0 0 8px; color: #fff;">AL<span class="sigma">Σ</span>F | Sertan Çubukcu | EğitimYayın</h3>
          <p class="text-justify" style="color: var(--text-secondary); margin: 0 0 14px; font-size: 0.94rem;">
            Türkçe Öğretmenliği ÖABT ve Millî Eğitim Akademisi hazırlık soru bankaları ve özel deneme setleri güvenli satış portalı.
          </p>
          <a href="https://egitimyayin.com/magaza.php?slug=alef-sertan-cubukcu" target="_blank" rel="noopener noreferrer" class="btn btn-store">
            EğitimYayın Mağazasına Git &rarr;
          </a>
        </div>
      </div>

      <!-- Google Play Kitaplar (Utrucce Dahil) -->
      <div class="books-grid">
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Utrucce?id=7RdaEQAAQBAJ&hl=tr" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div class="book-cover-wrap"><img src="assets/book_utrucce.jpg" alt="Utrucce Kapağı" loading="lazy"></div>
          <div class="book-info">
            <div class="badge badge-green" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 5,0 • Ücretsiz</div>
            <h3>Utrucce</h3>
            <span class="book-author">Sertan Çubukcu</span>
          </div>
          <div class="book-cta"><span>Google Play'de İncele</span> &rarr;</div>
        </a>
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_P%C4%B1rt%C4%B1l_Terakki_2_T%C3%BCrk%C3%A7e_%C3%96ABT?id=F9jWEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div class="book-cover-wrap"><img src="assets/book_cover_F9jWEQAAQBAJ.jpg" alt="Pırtıl Terakki-2 Kapağı" loading="lazy"></div>
          <div class="book-info">
            <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 3,4 • Ücretsiz</div>
            <h3>Pırtıl Terakki-2, Türkçe ÖABT</h3>
            <span class="book-author">Sertan Çubukcu</span>
          </div>
          <div class="book-cta"><span>Google Play'de İncele</span> &rarr;</div>
        </a>
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_T%C3%BCrk%C3%A7e_%C3%96ABT_Denemesi_P%C4%B1rt%C4%B1l_Terakki?id=TzTMEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div class="book-cover-wrap"><img src="assets/book_cover_TzTMEQAAQBAJ.jpg" alt="Türkçe ÖABT Denemesi Kapağı" loading="lazy"></div>
          <div class="book-info">
            <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 2,3 • Ücretsiz</div>
            <h3>Türkçe ÖABT Denemesi, Pırtıl-Terakki</h3>
            <span class="book-author">Sertan Çubukcu</span>
          </div>
          <div class="book-cta"><span>Google Play'de İncele</span> &rarr;</div>
        </a>
        <a href="https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Halk_Edebiyat%C4%B1_Girizg%C3%A2h_Soru_Mecmua?id=_uPKEQAAQBAJ" target="_blank" rel="noopener noreferrer" class="book-card-3d">
          <div class="book-cover-wrap"><img src="assets/book_cover__uPKEQAAQBAJ.jpg" alt="Halk Edebiyatı Kapağı" loading="lazy"></div>
          <div class="book-info">
            <div class="badge" style="font-size: 0.72rem; padding: 2px 8px; margin-bottom: 6px;">★ 4,2 • Ücretsiz</div>
            <h3>Halk Edebiyatı - Girizgâh</h3>
            <span class="book-author">Sertan Çubukcu</span>
          </div>
          <div class="book-cta"><span>Google Play'de İncele</span> &rarr;</div>
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
          <p class="text-justify">Resmî iletişim ve destek adreslerimiz:</p>
        </div>
      </div>

      <div class="social-grid">
        <a href="https://www.youtube.com/@1dakidat%C3%BCrk%C3%A7e%C3%B6abt" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #ff0000; background: rgba(255, 0, 0, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </div>
          <div>
            <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">YouTube</h3>
            <span style="font-size: 0.82rem; color: var(--text-muted);">1 Dakikada Türkçe ÖABT</span>
          </div>
        </a>
        <a href="https://www.instagram.com/sertancubukcu/" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #e1306c; background: rgba(225, 48, 108, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"></circle></svg>
          </div>
          <div>
            <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">Instagram</h3>
            <span style="font-size: 0.82rem; color: var(--text-muted);">@sertancubukcu</span>
          </div>
        </a>
        <a href="https://www.linkedin.com/in/sertan%C3%A7ubukcu/" target="_blank" rel="noopener noreferrer" class="social-card">
          <div class="social-icon-box" style="color: #0a66c2; background: rgba(10, 102, 194, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </div>
          <div>
            <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">LinkedIn</h3>
            <span style="font-size: 0.82rem; color: var(--text-muted);">Sertan Çubukcu</span>
          </div>
        </a>
        <a href="mailto:sertancubukcu@gmail.com" class="social-card" data-copy-email>
          <div class="social-icon-box" style="color: #ea4335; background: rgba(234, 67, 53, 0.1);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"></circle></svg>
          </div>
          <div>
            <h3 style="font-size: 1.05rem; margin: 0 0 2px; color: #fff;">Gmail</h3>
            <span style="font-size: 0.82rem; color: var(--text-muted);">sertancubukcu@gmail.com</span>
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
            <strong style="color: #fff; display: block; font-size: 1rem;">AL<span class="sigma">Σ</span>F Güvenlik Protokolü</strong>
            <span style="font-size: 0.8rem; color: var(--text-muted);">KVKK &amp; GDPR Kapsamlı Veri Bildirimi</span>
          </div>
        </div>
        <div>
          <a href="index.html" class="btn btn-outline" style="font-size: 0.84rem;">
            Ana Sayfaya Dön &rarr;
          </a>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 AL<span class="sigma">Σ</span>F • Yazar &amp; Geliştirici: Sertan Çubukcu. Bütün hakları saklıdır.
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

  <script src="assets/three.min.js"></script>
  <script src="assets/rainyday.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "privacy.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated privacy.html successfully.")
