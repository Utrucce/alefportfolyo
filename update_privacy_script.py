# -*- coding: utf-8 -*-
import os

filepath = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_privacy.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace #amiral-gemileri
content = content.replace('href="#amiral-gemileri"', 'href="#uygulamalar"')
content = content.replace('id="amiral-gemileri"', 'id="uygulamalar"')
content = content.replace('<!-- Amiral Gemisi Uygulamalarımız ve Ekran Görüntüleri -->', '<!-- Uygulamalarımız ve Ekran Görüntüleri -->')

# 2. Add Hâl Tercümesi to nav links if not present
old_nav = '''      <!-- Gezinme Bağlantıları (Privacy kelimesi kaldırılmış) -->
      <nav class="nav-links">
        <a href="index.html">Ana Sayfa</a>
        <a href="#politika">Güvenlik İlkeleri</a>'''

new_nav = '''      <!-- Gezinme Bağlantıları (Privacy kelimesi kaldırılmış) -->
      <nav class="nav-links">
        <a href="index.html">Ana Sayfa</a>
        <a href="index.html#hal-tercumesi">Hâl Tercümesi</a>
        <a href="#politika">Güvenlik İlkeleri</a>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)

# 3. Update Title & Meta description
old_meta = '<meta name="description" content="Sertan Çubukcu tarafından geliştirilen ALΣF MΣB-AGS ve Türkçe ÖABT uygulamalarının Google Play Store, KVKK ve GDPR uyumlu gizlilik politikası ve veri güvenliği bildirimi.">'
new_meta = '<meta name="description" content="Sertan Çubukcu tarafından geliştirilen ve yayınlanan BÜTÜN mobil uygulamalar (ALΣF MEB-AGS, ALΣF Türkçe ÖABT, ALΣF KPSS, ALΣF EKYS, İslam Vakti, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko) için Google Play Store, KVKK ve GDPR uyumlu gizlilik politikası ve veri güvenliği bildirimi.">'
content = content.replace(old_meta, new_meta)

# 4. Update Hero Subtitle
old_sub = '''      <p class="hero-subtitle text-justify">
        Millî Eğitim Bakanlığı Akademi Giriş Sınavı (M<span class="sigma">Σ</span>B - AGS) ve Türkçe ÖABT adayları için tasarlanan 
        AL<span class="sigma">Σ</span>F mobil uygulaması, EğitimYayın Mağazası, Google Play Kitapları, çevrim içi internet servisleri, 
        Telegram eğitim botları ve geliştirilmekte olan Android uygulamalarının veri güvenliği, kriptografik lisans ve kullanıcı hakları beyanıdır.
      </p>'''

new_sub = '''      <p class="hero-subtitle text-justify">
        Bu Gizlilik Politikası ve Güvenlik Protokolü; geliştirici ve yazar Sertan Çubukcu tarafından geliştirilen ve yayınlanan <strong>BÜTÜN mobil uygulamalar</strong> (AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS, AL<span class="sigma">Σ</span>F Türkçe ÖABT, AL<span class="sigma">Σ</span>F KPSS, AL<span class="sigma">Σ</span>F EKYS, İslam Vakti: Omuz Omuza, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko ve gelecekte yayınlanacak bütün sürümler), EğitimYayın Mağazası, Google Play Kitapları, çevrim içi internet servisleri ve Telegram eğitim botları ekosistemi için eksiksiz ve resmi güvenlik beyanıdır.
      </p>'''

content = content.replace(old_sub, new_sub)

# 5. Update Section 1 TR
old_sec1_tr = '''          <div class="policy-clause">
            <h3>1. Veri Sorumlusu ve Genel Kapsam</h3>
            <p class="text-justify">
              Bu Gizlilik Politikası, geliştirici ve yazar <strong>Sertan Çubukcu</strong> tarafından üretilen 
              <strong>AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS</strong>, 
              <strong>AL<span class="sigma">Σ</span>F Türkçe ÖABT</strong> mobil uygulamaları, 
              <strong>EğitimYayın Mağazası</strong>, <strong>Google Play Kitapları</strong>, 
              çevrim içi internet araçları ve Telegram botları ekosisteminin veri güvenliği ve gizlilik standartlarını belirler.
            </p>
            <div class="policy-highlight-box">
              <strong>Veri Sorumlusu:</strong> Sertan Çubukcu<br>
              <strong>E-posta:</strong> sertancubukcu@gmail.com<br>
              <strong>Yetkili Portal:</strong> ALΣF Eğitim ve Yayıncılık Ekosistemi
            </div>
          </div>'''

new_sec1_tr = '''          <div class="policy-clause">
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
          </div>'''

content = content.replace(old_sec1_tr, new_sec1_tr)

# 6. Update Section 1 EN
old_sec1_en = '''          <div class="policy-clause">
            <h3>1. Data Controller &amp; Scope</h3>
            <p class="text-justify">
              This Privacy Policy applies to the mobile applications <strong>ALΣF - MEB - AGS</strong>, 
              <strong>ALΣF Türkçe ÖABT</strong>, the <strong>EğitimYayın Store</strong>, <strong>Google Play Books</strong>, 
              associated web services, and Telegram educational bots developed and published by <strong>Sertan Çubukcu</strong>.
            </p>
            <div class="policy-highlight-box">
              <strong>Data Controller:</strong> Sertan Çubukcu<br>
              <strong>Email:</strong> sertancubukcu@gmail.com<br>
              <strong>Ecosystem:</strong> ALΣF Educational &amp; Publishing Ecosystem
            </div>
          </div>'''

new_sec1_en = '''          <div class="policy-clause">
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
          </div>'''

content = content.replace(old_sec1_en, new_sec1_en)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_privacy.py successfully.")
