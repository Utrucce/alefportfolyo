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
// 1. TAM SİTE DİL MOTORU (TÜRKÇE / ENGLISH)
// ==========================================
const ALEF_I18N_MAP = {
  "Balinayı Zıplat": "Jump the Whale",
  "Tanıtım": "Overview",
  "Uygulamalar": "Apps",
  "Görüntüler": "Screenshots",
  "Hâl Tercümesi": "Curriculum Vitae",
  "Kitaplar & Mağaza": "Books & Store",
  "İnternet Projeleri": "Web Projects",
  "Telegram": "Telegram",
  "İletişim": "Contact",
  "Gizlilik İlkeleri": "Privacy Principles",
  "Gizlilik Politikası": "Privacy Policy",
  "Gizlilik Politikası →": "Privacy Policy →",
  "Güvenlik İlkeleri": "Security Principles",
  "Güvenlik İlkeleri →": "Security Principles →",
  "Ana Sayfa": "Home",
  "Ana Sayfaya Dön": "Back to Home",
  "Ana Sayfaya Dön →": "Back to Home →",
  "GDPR & KVKK": "GDPR & KVKK",
  "Uygulama Görüntüleri": "App Screenshots",
  "Yayınlar": "Publications",
  "EğitimYayın & Kitaplar": "EğitimYayın & Books",
  "🐺 Türk Söylenceler Sözlüğü": "🐺 Dictionary of Turkic Myths",
  "Öğretmenlik ve Millî Eğitim Akademisi Hazırlık Portalı": "Teaching & National Education Academy Preparation Portal",
  "Öğretmenlik ve Akademi Yolunda": "On the Path to Teaching and the Academy",
  "F ile Zirveye Adım At": "F — Step to the Peak",
  "Millî Eğitim Bakanlığı Akademi Giriş Sınavı (M": "A complete educational ecosystem meticulously developed for Republic of Türkiye Ministry of National Education Academy Entrance Exam (M",
  "B - AGS) ve Türkçe ÖABT adayları için titizlikle geliştirilen kapsamlı soru havuzu, deneme sınavları, konu özetleri,": "B - AGS) and Turkish Teaching (ÖABT) candidates, featuring an extensive question bank, practice exams, topic summaries,",
  "EğitimYayın Mağazası": "EğitimYayın Store",
  "Google Play Kitapları": "Google Play Books",
  "Türk Söylenceler Sözlüğü": "Dictionary of Turkic Myths",
  "dijital kültür portalı, canlı internet platformları, 8 adet etkileşimli Telegram eğitim botu ve geliştirilmekte olan yeni nesil Android uygulamalarıyla eksiksiz bir eğitim ekosistemi.": "digital culture portal, live web platforms, 8 interactive Telegram educational bots, and next-generation Android applications.",
  "Google Play Store • EğitimYayın • KVKK • GDPR Uyumlu Resmî Güvenlik Belgesi": "Official Security Document Compliant with Google Play Store • EğitimYayın • KVKK • GDPR",
  "Gizlilik Politikası ve Güvenlik Protokolü": "Privacy Policy and Security Protocol",
  "Bu Gizlilik Politikası ve Güvenlik Protokolü; geliştirici ve yazar Sertan Çubukcu tarafından geliştirilen ve yayınlanan": "This Privacy Policy and Security Protocol is the complete and official security statement for",
  "BÜTÜN mobil uygulamalar": "ALL mobile applications",
  "F EKYS, İslam Vakti: Omuz Omuza, Kıble Bulucu, Karargâh, Mergen, Pırtıl, Asayiş Berko ve gelecekte yayınlanacak bütün sürümler), EğitimYayın Mağazası, Google Play Kitapları, çevrim içi internet servisleri ve Telegram eğitim botları ekosistemi için eksiksiz ve resmi güvenlik beyanıdır.": "F EKYS, Islamic Time: Shoulder to Shoulder, Qibla Finder, Karargâh, Mergen, Pırtıl, Asayiş Berko, and all future releases) developed and published by developer and author Sertan Çubukcu, as well as the EğitimYayın Store, Google Play Books, online web services, and the Telegram educational bots ecosystem.",
  "Son Güncelleme:": "Last Updated:",
  "Ekim 2026 / October 2026": "October 2026",
  "• Sürüm:": "• Version:",
  "Android Mobil Hazırlık Uygulaması": "Android Mobile Preparation App",
  "Alan Bilgisi Hazırlık Platformu": "Field Knowledge Preparation Platform",
  "Geliştirici & Yazar Kurumsal Kimliği": "Developer & Author Corporate Identity",
  "Kurt Arma": "Wolf Crest",
  "Özgün Mühür & Güvenlik Simgesi": "Original Seal & Security Emblem",
  "Mobil Uygulamalarımız": "Our Mobile Applications",
  "Adaylarımızın sınav hazırlığında ve günlük manevi yaşamında doğrudan kullandığı, hem telefondan hem de bilgisayardan gerçek logolarıyla sunulan mobil platformlarımız:": "Our mobile platforms presented with their authentic logos, directly used by candidates in exam preparation and daily spiritual life:",
  "Millî Eğitim Akademisi Hazırlık": "National Education Academy Prep",
  "✓ Yayında": "✓ Live",
  "10.990+ Soru": "10,990+ Questions",
  "Akademi Giriş Sınavı müfredatına tam uyumlu deneme sınavları, mevzuat soru bankası, bilgi kartları ve internetsiz çalışma desteği.": "Practice exams fully aligned with the Academy Entrance Exam curriculum, legislation question bank, flashcards, and offline study support.",
  "Ekran Görüntüleri →": "Screenshots →",
  "İncele →": "Explore →",
  "Telegram Botu →": "Telegram Bot →",
  "Alan Bilgisi ve Eğitimi": "Subject Knowledge & Education",
  "Edebiyat & Dil": "Literature & Language",
  "Eski Türk Dili, Yeni Türk Edebiyatı, Halk Edebiyatı ve Alan Eğitimi modülleriyle Türkçe öğretmen adaylarına özel akademik hazırlık platformu.": "Academic preparation platform tailored for Turkish language teacher candidates with Old Turkic Language, Modern Turkish Literature, Folk Literature, and Field Education modules.",
  "Genel Yetenek & Genel Kültür": "General Aptitude & General Culture",
  "ÖSYM Formatı": "ÖSYM Format",
  "Tarih, Coğrafya, Vatandaşlık ve Türkçe alanlarında tam kapsamlı soru havuzu, denemeler ve detaylı çözümler.": "Comprehensive question pool, practice exams, and detailed solutions in History, Geography, Civics, and Turkish.",
  "Eğitim Kurumları Yöneticiliği": "Educational Institutions Management",
  "Mevzuat & Yönetim": "Legislation & Management",
  "Müdür ve müdür yardımcılığı sınavlarına hazırlanan eğitimciler için güncel mevzuat testleri ve deneme modülleri.": "Up-to-date legislation tests and practice exam modules for educators preparing for principal and vice-principal exams.",
  "İslam Vakti: Omuz Omuza": "Islamic Time: Shoulder to Shoulder",
  "Manevi Yaşam & İbadet": "Spiritual Life & Worship",
  "Çevrim Dışı": "Offline",
  "Namaz vakitleri, zikirçeker, manevi bahçe ve irfan kartları içeren kullanıcı dostu mobil manevi yaşam rehberi.": "User-friendly mobile spiritual life guide featuring prayer times, dhikr counter, spiritual garden, and wisdom cards.",
  "Kıble Bulucu": "Qibla Finder",
  "Pusula ve Harita Destekli": "Compass & Map Supported",
  "Hassas Açı": "Precision Angle",
  "Cihazın donanım pusulasını kullanarak konumu sunucuya iletmeden anlık yerel matematiksel açıyla kıble tayini yapar.": "Determines Qibla direction with real-time local mathematical angle calculation using the device's hardware compass without transmitting location to any server.",
  "Veri ve Telefon Güvenliği": "Data & Phone Security",
  "Güvenlik & Gizlilik": "Security & Privacy",
  "Kullanıcı verilerinin cihaz içinde güvenle saklanması ve telefon güvenliğinin denetlenmesi için geliştirilen yerel güvenlik kalkanı.": "Local security shield developed for storing user data safely on-device and auditing phone security.",
  "Akıl ve Strateji Motoru": "Mind & Strategy Engine",
  "Eğitim AR-GE": "Education R&D",
  "Soru analiz algoritmaları ve sınav stratejileri geliştiren akıllı soru tahlil asistanı.": "Intelligent question analysis assistant that develops question analysis algorithms and exam strategies.",
  "Yerel Sûnî Zekâ": "On-Device Artificial Intelligence",
  "İnternetsiz Model": "Offline Model",
  "Eğitilmek üzere olan, doğrudan telefonda çalışan ve hiçbir internet bağlantısına ihtiyaç duymayan yerel sûnî zekâ çekirdeği.": "On-device artificial intelligence core currently in training that runs directly on the phone without requiring any internet connection.",
  "Dijital Güvenlik ve Emniyet": "Digital Security & Safety",
  "Yerel Denetim": "Local Audit",
  "Zararlı içerikleri filtreleyen ve dijital cihaz emniyetini sağlayan koruyucu mobil güvenlik çözümü.": "Protective mobile security solution that filters harmful content and ensures digital device safety.",
  "F Uygulama Ekran Görüntüleri": "F Application Screenshots",
  "Uygulama Ekran Görüntüleri": "Application Screenshots",
  "Mobil uygulamalarımızın modern arayüzü, soru çözüm modülleri ve manevi araçları (Büyütmek için görsele tıklayın):": "Modern interface, question-solving modules, and spiritual tools of our mobile applications (Click on an image to enlarge):",
  "Uygulamalarımızın mobil arayüzleri, test modülleri ve güvenlik mimarisi (Büyütmek için tıklayın):": "Mobile interfaces, test modules, and security architecture of our applications (Click to enlarge):",
  "Giriş ve Ana Menü": "Home & Main Menu",
  "Modül ve Konu Seçimi": "Module & Topic Selection",
  "Soru Listesi & Filtreler": "Question List & Filters",
  "Soru Çözümü & Açıklamalar": "Question Solving & Explanations",
  "Performans İstatistikleri": "Performance Statistics",
  "Zaman Ayarlı Deneme Sınavı": "Timed Practice Exam",
  "Kişiselleştirilmiş Notlar": "Personalized Notes",
  "Sınav Geri Sayımı & Raporlar": "Exam Countdown & Reports",
  "Namaz Vakitleri & Sayaç": "Prayer Times & Countdown",
  "Kıble Pusulası & Konum": "Qibla Compass & Location",
  "Manevi Bahçe & Çiftlik": "Spiritual Garden & Farm",
  "Zikirçeker & Manevi Zincir": "Dhikr Counter & Spiritual Chain",
  "İslami Araçlar & Keşfet": "Islamic Tools & Explore",
  "Utrucce İrfan Kartları": "Utrucce Wisdom Cards",
  "Hüdhüd Güvenli Tarayıcı": "Hüdhüd Secure Browser",
  "Pırtıl Medya Oynatıcı": "Pırtıl Media Player",
  "📄 Hâl Tercümesi Belgesi Al": "📄 Get Curriculum Vitae Document",
  "ALΣF • Yıldız Teknik Üniversitesi": "ALΣF • Yıldız Technical University",
  "📍 İstanbul, Türkiye": "📍 Istanbul, Türkiye",
  "Hakkında": "About",
  "Gelişime açık bir öğretmen adayı olarak; Türkçe Öğretmenliği alanında edindiğim; lisans eğitimi sayesinde eğitim dünyasında uzmanlaşmayı hedefliyorum. Ayrıca gönüllü öğretmenlik tecrübem vesilesiyle modern eğitim tekniklerini ve yenilikçi yaklaşımları sınıf ortamına entegre edebilme becerim gelişmektedir. Çevrim içi ve fiziksel eğitim ortamlarındaki fırsatları takip ederek; sürekli gelişmeyi ve hayat boyu eğitim anlayışını benimsemekteyim. Farklı iş tecrübelerimden edindiğime göre; en çok insan odaklı ve insanlarla iletişime girdiğim işlerin bana uygun olduğunu ve insanlarla sağlıklı iletişim kurduğumda; mutlu olduğumu; fark ettim. Öğretmenlik mesleğinin gerektirdiği; pedogojik uzmanlığa ek olarak; dijital yetkinlik için farklı eğitimler almaktayım. Aldığım eğitimleri; beceriye dönüştürerek; insanlık için faydalı ürünler ve hizmetler üretmeyi amaçlamaktayım.": "As an open-minded teacher candidate, I aim to specialize in the field of education thanks to my undergraduate degree in Turkish Language Teaching. Furthermore, through my volunteer teaching experience, my ability to integrate modern educational techniques and innovative approaches into the classroom environment continues to grow. By following opportunities in both online and physical learning environments, I embrace continuous self-improvement and lifelong learning. Based on my diverse work experiences, I have realized that human-centered roles involving direct interaction suit me best, and that establishing healthy communication with people brings me happiness. In addition to the pedagogical expertise required by the teaching profession, I pursue various training programs for digital competence. By transforming the training I receive into practical skills, I aim to produce beneficial products and services for humanity.",
  "Deneyim": "Experience",
  "8 Deneyim": "8 Experiences",
  "Oca 2026 - Devam ediyor · 11 ay": "Jan 2026 - Present · 11 mos",
  "Eğitim İçerik Üreticisi": "Educational Content Creator",
  "ALΣF · Kendi işim • İstanbul, Türkiye · Ofiste": "ALΣF · Self-employed • Istanbul, Türkiye · On-site",
  "Sunî zekâ destekli eğitim uygulamaları geliştirmekteyim. Bu projede PyCharm, Android Studio, Claude, Antigravity, Gemini, Codex, Termux, Github gibi araçlar kullanmaktayım. Soru üretimi, infografik vb. eğitim uygulamaları yaptım. Telegram botu, internet uygulamaları, editörlük uygulamaları, Android uygulamalar yaptım bu projede.": "I develop artificial intelligence-powered educational applications. In this project, I use tools such as PyCharm, Android Studio, Claude, Antigravity, Gemini, Codex, Termux, and GitHub. I have created educational applications for question generation, infographics, and more, including Telegram bots, web applications, editorial tools, and Android applications.",
  "Eyl 2024 - Tem 2026 · 1 yıl 11 ay": "Sep 2024 - Jul 2026 · 1 yr 11 mos",
  "Gönüllü Türkçe Öğretmeni": "Volunteer Turkish Teacher",
  "Okul Destek Derneği · Serbest çalışan • Türkiye · Uzaktan": "School Support Association (Okul Destek Derneği) · Freelance • Türkiye · Remote",
  "Ükemizdeki devlet okullarında okuyan öğrencilere uzaktan eğitim yoluyla haftada 2 saat Türkçe kod sistemini doğru kullanmalarını sağlamak için onlara yardımcı olmaktayım. Öğrencilerin yazma vazifelerine geribildirim vererek; onların üretim süreçlerine katkı sunmaktayım.": "I assist students attending public schools in our country for 2 hours a week via distance education to help them use the Turkish language code system accurately. By providing feedback on students' writing assignments, I contribute to their creative and productive processes.",
  "Nis 2023 - Ağu 2025 · 2 yıl 5 ay": "Apr 2023 - Aug 2025 · 2 yrs 5 mos",
  "Depo Vazifelisi-Dönemsel (Serbest-Günlük)": "Warehouse Associate - Seasonal (Freelance-Daily)",
  "Aygaz A.Ş. · Serbest çalışan • Avcılar, İstanbul, Türkiye · Ofiste": "Aygaz A.Ş. · Freelance • Avcılar, Istanbul, Türkiye · On-site",
  "Ara 2024 - Mar 2025 · 4 ay": "Dec 2024 - Mar 2025 · 4 mos",
  "Öğretmen Yetiştirme Programı": "Teacher Training Program",
  "Çınar Koleji · Stajyer • Başakşehir, İstanbul, Türkiye · Ofiste": "Çınar College · Intern • Başakşehir, Istanbul, Türkiye · On-site",
  "Eki 2023 - Haz 2024 · 9 ay": "Oct 2023 - Jun 2024 · 9 mos",
  "Öğretmenlik Uygulaması-Esenler Yunus Emre Ortaokulu": "Teaching Practicum - Esenler Yunus Emre Middle School",
  "Türkiye Cumhuriyeti Millî Eğitim Bakanlığı · Yarı zamanlı • Esenler, İstanbul, Türkiye": "Republic of Türkiye Ministry of National Education · Part-time • Esenler, Istanbul, Türkiye",
  "Üniversite mecburi dersi olarak aldığım; öğretmenlik uygulaması sayesinde okul ekosisteminin dinamiklerini tanıma fırsatı buldum. Öğrencileri gözlemleyerek; onların öğrenme stratejilerini fark etmeye çalıştım.": "Through the mandatory university teaching practicum course, I had the opportunity to experience the dynamics of the school ecosystem firsthand. By observing students, I worked on identifying and understanding their learning strategies.",
  "Şub 2020 - Ağu 2020 · 7 ay": "Feb 2020 - Aug 2020 · 7 mos",
  "Kargo Çalışanı": "Cargo Operations Staff",
  "MNG Kargo - a company of DHL · Tam zamanlı • Esenyurt, İstanbul, Türkiye": "MNG Kargo - a company of DHL · Full-time • Esenyurt, Istanbul, Türkiye",
  "May 2018 - Oca 2019 · 9 ay": "May 2018 - Jan 2019 · 9 mos",
  "Paketleme Elemanı": "Packaging Associate",
  "Tempo Şekerleme · Tam zamanlı • Arnavutköy, İstanbul, Türkiye": "Tempo Confectionery · Full-time • Arnavutköy, Istanbul, Türkiye",
  "Mar 2016 - Ağu 2016 · 6 ay": "Mar 2016 - Aug 2016 · 6 mos",
  "Kasiyer": "Cashier",
  "Şok Marketler · Tam zamanlı • Esenyurt, İstanbul, Türkiye": "Şok Markets · Full-time • Esenyurt, Istanbul, Türkiye",
  "Eğitim": "Education",
  "3 Eğitim": "3 Educations",
  "Eyl 2021 – Oca 2025": "Sep 2021 – Jan 2025",
  "Yıldız Teknik Üniversitesi": "Yıldız Technical University",
  "Lisans Derecesi, Türkçe Öğretmenliği": "Bachelor's Degree, Turkish Language Teaching",
  "Eki 2025 – Devam ediyor": "Oct 2025 – Present",
  "İstanbul Üniversitesi-Cerrahpaşa": "Istanbul University-Cerrahpaşa",
  "Spor İdareciliği": "Sports Management",
  "Eyl 2011 – Haz 2015": "Sep 2011 – Jun 2015",
  "Çakmaklı Cumhuriyet Anadolu Lisesi": "Çakmaklı Cumhuriyet Anatolian High School",
  "Lise, Eşit Ağırlık": "High School Diploma, Equal Weight Track",
  "Projeler & Yayınlar": "Projects & Publications",
  "1 Proje • 1 Yayın": "1 Project • 1 Publication",
  "Proje": "Project",
  "Sosyal Aidiyet ve Okuma Performansına İlişkisinde Aile Motivasyonunun Aracılığı: PISA Tabanlı İkincil Bir Analiz": "The Mediating Role of Family Motivation in the Relationship Between Social Belonging and Reading Performance: A PISA-Based Secondary Analysis",
  "2209-A - Üniversite Öğrencileri Araştırma Projeleri Destekleme Programı": "TÜBİTAK 2209-A - University Students Research Projects Support Program",
  "Rakuten Kobo · 13 May 2025": "Rakuten Kobo · May 13, 2025",
  "Utrucce-Fantastik Hikâye": "Utrucce - Fantasy Story",
  "📖 Yayını göster ↗": "📖 Show publication ↗",
  "Gönüllü Çalışma": "Volunteering",
  "8 Gönüllü Çalışma": "8 Volunteering Roles",
  "Ara 2021 - Devam ediyor · 5 yıl": "Dec 2021 - Present · 5 yrs",
  "Gönüllü Çalışan, Editör": "Volunteer Staff, Editor",
  "Dil Akademisi • Eğitim": "Language Academy • Education",
  "Haz 2017 - Devam ediyor · 9 yıl 6 ay": "Jun 2017 - Present · 9 yrs 6 mos",
  "Bağış Gönüllüsü": "Donation Volunteer",
  "Kızılay • Sağlık": "Turkish Red Crescent (Kızılay) • Health",
  "Kas 2025 - Devam ediyor · 1 yıl 1 ay": "Nov 2025 - Present · 1 yr 1 mo",
  "Metin Okuyucusu": "Text Reader for the Visually Impaired",
  "Ders Ortağım Projesi • Sosyal Hizmetler": "My Study Partner Project • Social Services",
  "Görme engelli kardeşlerimize ilgili metinleri okumaktayım.": "I read educational and literary texts aloud for our visually impaired brothers and sisters.",
  "Eyl 2025 - May 2026 · 9 ay": "Sep 2025 - May 2026 · 9 mos",
  "Okul Destek Derneği • Eğitim": "School Support Association (Okul Destek Derneği) • Education",
  "Eki 2025 - Devam ediyor · 1 yıl 2 ay": "Oct 2025 - Present · 1 yr 2 mos",
  "Destek Ekip Gönüllüsü": "Support Team Volunteer",
  "T.C. İçişleri Bakanlığı Afet ve Acil Durum Yönetimi Başkanlığı - AFAD • Felaket ve İnsani Yardım": "Republic of Türkiye Ministry of Interior Disaster and Emergency Management Presidency (AFAD) • Disaster and Humanitarian Relief",
  "Destek ekip gönüllüsü olarak çadır kurma, profesyonel ekiplerin verdiği talimatlar doğrultusunda arama-kurtarma faaliyetlerinde bulunma gibi vazifeler yapmaktayım. Bu süreçte arama ve kurtarma, sosyal yardım, yangın, ilkyardım gibi konularda, afet ve acil durum hallerinde profesyonel ekiplere destek olabilecek bilgi ve beceriye sahip olacak eğitimler almaktayım.": "As a support team volunteer, I perform duties such as setting up tents and participating in search and rescue operations under the guidance of professional teams. Throughout this process, I receive training in search and rescue, social aid, fire safety, and first aid to acquire the knowledge and skills needed to support professional teams during disasters and emergencies.",
  "Tem 2026 - Devam ediyor · 5 ay": "Jul 2026 - Present · 5 mos",
  "ALΣF • Eğitim": "ALΣF • Education",
  "Android uygulama geliştirme süreçlerinde çalışıyorum. Ayrıca içerikleri üretmekten sorumluyum. Soru hazırlamaktayım.": "I work on Android application development processes and am responsible for content production and question authoring.",
  "Etkinlik Görevlisi": "Event Coordinator",
  "İBB Spor İstanbul • Sosyal Hizmetler": "IMM Spor Istanbul • Social Services",
  "Şub 2018 - Devam ediyor · 8 yıl 10 ay": "Feb 2018 - Present · 8 yrs 10 mos",
  "Gönüllü Çalışan": "Volunteer Staff",
  "T.C. Gençlik ve Spor Bakanlığı • Kültür ve Sanat": "Republic of Türkiye Ministry of Youth and Sports • Culture and Arts",
  "Lisanslar ve sertifikalar (53)": "Licenses & Certifications (53)",
  "Her sertifikanın altındaki bağlantıya tıklayarak resmi yeterlilik belgesini görüntüleyebilirsiniz": "Click the link below each certificate to view the official credential document",
  "📄 Yeterlilik belgesini göster ↗": "📄 Show credential ↗",
  "Gönüllü Eğitmen Sertifikası": "Volunteer Instructor Certificate",
  "Okul Destek Derneği": "School Support Association (Okul Destek Derneği)",
  "YetGen Öğretmen Eğitim Programı TR": "YetGen Teacher Training Program TR",
  "Yetkin Gençler": "Yetkin Gençler (Competent Youth)",
  "Eğitimde Farklılaştırma Stratejileri": "Differentiation Strategies in Education",
  "Enstitü Sosyal": "Enstitü Sosyal (Social Institute)",
  "Nitelikli Eğitim, BM Kalkınma Hedefleri": "Quality Education, UN Sustainable Development Goals",
  "Eğitimde Oyunlaştırma ve İnternet 2.0 Araçları": "Gamification in Education and Web 2.0 Tools",
  "BTK Akademi": "BTK Academy",
  "Educast İnternational Confererence 2025": "Educast International Conference 2025",
  "Veri Bilimi İçin Temel İstatistik": "Fundamental Statistics for Data Science",
  "Oyun Terapisi Eğitimi": "Play Therapy Training",
  "İstanbul İşletme Enstitüsü": "Istanbul Institute of Business",
  "Microsoft Word Temelleri": "Microsoft Word Fundamentals",
  "Etkili Sunum Teknikleri": "Effective Presentation Techniques",
  "İGEDER İstanbul Gönüllü Eğitimciler Derneği": "İGEDER Istanbul Volunteer Educators Association",
  "Canva Dijital Öğretmenler Zirvesi": "Canva Digital Teachers Summit",
  "Etkin Kampüs": "Etkin Kampüs",
  "Zaman Yönetimi": "Time Management",
  "Öğretmenin Psikolojik Dayanıklılığı": "Psychological Resilience of the Teacher",
  "Geleceğin Öğretmen Zirvesi '24": "Teacher of the Future Summit '24",
  "Sıra Dışı Öğretim Teknikleri": "Extraordinary Teaching Techniques",
  "Bütünsel Gelişim Eğitimi": "Holistic Development Training",
  "YETEV Eğitim Teknolojileri Zirvesi '24": "YETEV Educational Technologies Summit '24",
  "B1 İngilizce": "B1 English Certificate",
  "Veri Bilimine Giriş": "Introduction to Data Science",
  "Etkili İletişim Stratejileri": "Effective Communication Strategies",
  "Dijital Hikâyeler-Hikâye Anlatma Tekniklerinde Akademik Başarı Uygulamalarını Artırarak Erken Okul Terkini Azaltma, Erasmus+ Projesi, Modüller": "Digital Stories - Reducing Early School Leaving by Increasing Academic Success Practices in Storytelling Techniques, Erasmus+ Project, Modules",
  "Türkiye Cumhuriyeti Millî Eğitim Bakanlığı": "Republic of Türkiye Ministry of National Education",
  "Kariyeri Tehdit Eden Yaklaşımlar": "Career-Threatening Approaches",
  "Etkili Geribildirim Eğitimi (Socrative, Plickers, Menti)": "Effective Feedback Training (Socrative, Plickers, Menti)",
  "TÜBİTAK 2209-A PROJESİ": "TÜBİTAK 2209-A PROJECT",
  "Dijital Hikâyeler-Hikâye Anlatma Tekniklerinde Akademik Başarı Uygulamalarını Artırarak Erken Okul Terkini Azaltma, Erasmus+ Projesi Kapanış Sunumu": "Digital Stories - Reducing Early School Leaving by Increasing Academic Success Practices in Storytelling Techniques, Erasmus+ Project Closing Presentation",
  "4. İstanbul '24 Eğitim Zirvesi": "4th Istanbul '24 Education Summit",
  "TÜRKİYE MAARİF VAKFI": "Turkish Maarif Foundation",
  "Çocuk ve Felsefe Bilgilendirme Semineri": "Children and Philosophy Information Seminar",
  "Arduino ile Robotiğe Giriş": "Introduction to Robotics with Arduino",
  "İş İngilizcesi": "Business English",
  "Sıkça Yapılan Yazım Yanlışları": "Frequently Made Spelling Mistakes",
  "TRT Akademi": "TRT Academy",
  "Farklı Bakışlarla Özel Eğitim Bilgilendirme Semineri": "Special Education Information Seminar from Different Perspectives",
  "Karatay Üniversitesi Sürekli Eğitim Merkezi - KARSEM": "Karatay University Continuing Education Center - KARSEM",
  "Zihin Haritaları Eğitimi": "Mind Mapping Training",
  "Mangala, Mas Güreşi ve Geleneksel Okçuluk Eğitmen Eğitimi": "Mangala, Mas-Wrestling, and Traditional Archery Instructor Training",
  "WORLD ETHNOSPORT UNİON": "World Ethnosport Union",
  "İş Hayatında Oryantasyon": "Workplace Orientation",
  "Esenyurt Belediyesi": "Esenyurt Municipality",
  "Liderlik": "Leadership",
  "T.C. İçişleri Bakanlığı Afet ve Acil Durum Yönetimi Başkanlığı - AFAD": "Republic of Türkiye Ministry of Interior Disaster and Emergency Management Presidency - AFAD",
  "Kişisel Stres Yönetimi": "Personal Stress Management",
  "Arama Faaliyetlerinde Kullanılan Düğümler": "Knots Used in Search and Rescue Operations",
  "Afet Risklerini Azaltma": "Disaster Risk Reduction",
  "Afet Risklerini Anlama": "Understanding Disaster Risks",
  "Birey ve Aileler İçin Afet Bilinci Eğitimi": "Disaster Awareness Training for Individuals and Families",
  "Ekranların Ötesinde Geleceğin Liderlerine İlham Vermek Semineri": "Inspiring Future Leaders Beyond Screens Seminar",
  "Zor Öğrencilerle İletişim": "Communicating with Challenging Students",
  "Eğitimde Oyunun Gücü": "The Power of Play in Education",
  "Dijital Yaşam Becerileri": "Digital Life Skills",
  "Atılganlık": "Assertiveness",
  "Türkçenin Doğru Kullanımı": "Proper Use of the Turkish Language",
  "Hızlı ve Etkili Okuma Teknikleri Bilgilendirme Semineri": "Fast and Effective Reading Techniques Information Seminar",
  "Topluluk Önünde Konuşma ve Etkili Sunum Teknikleri": "Public Speaking and Effective Presentation Techniques",
  "Problem Çözme Teknikleri": "Problem Solving Techniques",
  "72 Saatlik Bilgisayarsız Robotik Kodlama": "72-Hour Unplugged Robotics Coding",
  "Motivasyon 3.0 Eğitimi": "Motivation 3.0 Training",
  "Bionluk Uzman Hizmeti": "Bionluk Expert Service",
  "utrucce - Metin ve Video Editörü | Bionluk": "utrucce - Text & Video Editor | Bionluk",
  "Metin tahlili, soru kitapçığı redaksiyonu, kitap mizanpajı, video montajı ve profesyonel editörlük hizmetleri için Bionluk profilimizi ziyaret edebilirsiniz.": "Visit our Bionluk profile for text analysis, question booklet proofreading, book layout design, video editing, and professional editorial services.",
  "Metin tahlili, soru kitapçığı redaksiyonu, kitap mizanpajı ve profesyonel editörlük hizmetleri için Bionluk profilimizi ziyaret edebilirsiniz.": "Visit our Bionluk profile for text analysis, question booklet proofreading, book layout design, and professional editorial services.",
  "Bionluk Profiline Git →": "Visit Bionluk Profile →",
  "Yayın Mağazası & Google Play Kitapları": "Publishing Store & Google Play Books",
  "Sertan Çubukcu tarafından kaleme alınan lisanslı eğitim yayınları, soru bankaları ve dijital eserler:": "Licensed educational publications, question banks, and digital works authored by Sertan Çubukcu:",
  "Sertan Çubukcu tarafından kaleme alınan lisanslı eğitim yayınları ve dijital eserler:": "Licensed educational publications and digital works authored by Sertan Çubukcu:",
  "Resmî Satış & Dağıtım Mağazası": "Official Sales & Distribution Store",
  "Türkçe Öğretmenliği ÖABT ve Millî Eğitim Akademisi hazırlık soru bankaları ve özel deneme setleri güvenli satış portalı.": "Secure sales portal for Turkish Teaching (ÖABT) and National Education Academy preparation question banks and practice exam sets.",
  "EğitimYayın Mağazasına Git →": "Go to EğitimYayın Store →",
  "Google Play'de İncele": "View on Google Play",
  "Pırtıl Terakki-2, Türkçe ÖABT": "Pırtıl Terakki-2, Turkish ÖABT",
  "Türkçe ÖABT Denemesi, Pırtıl-Terakki": "Turkish ÖABT Practice Exam, Pırtıl-Terakki",
  "Halk Edebiyatı - Girizgâh": "Folk Literature - Introduction",
  "2024 Maarif Karikatürleştirilmiş Çıktılar": "2024 Maarif Illustrated Learning Outcomes",
  "Mihenk Zühre / Türkçe ÖABT": "Mihenk Zühre / Turkish ÖABT",
  "Türkçe ÖABT Denemesi / Pırtlak-1": "Turkish ÖABT Practice Exam / Pırtlak-1",
  "Canlı İnternet Platformları": "Live Web Platforms",
  "Geliştirici Sertan Çubukcu tarafından kurulan ve yayında olan çevrim içi internet servisleri:": "Online web services founded and maintained by developer Sertan Çubukcu:",
  "✓ Yayında • Dijital Kültür Portalı": "✓ Live • Digital Culture Portal",
  "📖 907 Sayfa Orijinal Eser": "📖 907-Page Original Work",
  "🔍 874 Mitolojik Kavram": "🔍 874 Mythological Concepts",
  "🏆 3.868 Soruluk Bilgi Yarışması": "🏆 3,868-Question Trivia Quiz",
  "Türk Söylenceler Sözlüğü | Dijital Mitoloji ve Kültür Portalı": "Dictionary of Turkic Myths | Digital Mythology & Culture Portal",
  "Yazar: Deniz Karakurt • Dijital Mimari & Site Tasarımı: Sertan Çubukcu • utrucce.github.io/Turk-Soylenceler-Sozlugu": "Author: Deniz Karakurt • Digital Architecture & Web Design: Sertan Çubukcu • utrucce.github.io/Turk-Soylenceler-Sozlugu",
  "Açıklamalı Ansiklopedik Mitoloji Sözlüğü'nün 907 sayfalık orijinal belgesini": "A comprehensive culture portal uniting the 907-page original Annotated Encyclopedic Mythology Dictionary with",
  "Üç Boyutlu Sayfa Kıvrılma": "3D Page-Curl Flipbook",
  "ve gerçek sayfa çevirme sesiyle okuma, Türkçe sesli okuma (TTS), 7 farklı okuma teması, 874 mitolojik kavram ve kökenbilim dizininde anlık arama ile 3.868 soruluk dört şıklı etkileşimli bilgi yarışmasını tek çatı altında buluşturan kapsamlı kültür portalı.": "and realistic page-flip audio, Turkish text-to-speech (TTS), 7 reading themes, instant search across 874 mythological concepts and etymology index, plus an interactive 3,868-question multiple-choice quiz.",
  "🐺 Portalı Ziyaret Et (Canlı Yayın) →": "🐺 Visit Live Portal →",
  "Dijital etiketleme, metin tahlili ve soru arşivleme için geliştirilen modern bulut tabanlı internet aracı.": "Modern cloud-based web tool developed for digital tagging, text analysis, and question archiving.",
  "Siteyi Ziyaret Et": "Visit Website",
  "Radyo Tiyatrosu": "Radio Drama Theater",
  "Klasik ve çağdaş radyo tiyatrosu kayıtlarını edebiyatseverlerle buluşturan çevrim içi sesli drama kütüphanesi.": "Online audio drama library bringing classic and contemporary radio theater recordings to literature enthusiasts.",
  "Dinlemeye Başla": "Start Listening",
  "ALΣF Psikoloji": "ALΣF Psychology",
  "Öğretmen adayları ve öğrenciler için motivasyon, sınav kaygısı yönetimi ve rehberlik içerikleri platformu.": "Motivation, exam anxiety management, and guidance content platform for teacher candidates and students.",
  "Platformu İncele": "Explore Platform",
  "AFED Dersleri": "AFED Disaster Courses",
  "Afet bilinci, acil durum yönetimi ve temel sivil savunma eğitim materyallerini içeren açık kaynaklı eğitim portalı.": "Open-source educational portal featuring disaster awareness, emergency management, and basic civil defense training materials.",
  "Eğitimi İncele": "Explore Training",
  "Telegram Eğitim Botları & Topluluklarımız": "Our Telegram Educational Bots & Communities",
  "Adaylarımıza anlık soru çözümü, edebiyat tahlili ve sınav desteği sunan Telegram servislerimiz:": "Our Telegram services offering instant question solving, literary analysis, and exam support to candidates:",
  "Türkçe ÖABT ve Soru Asistanı": "Turkish ÖABT & Question Assistant",
  "Yazarlık & Edebiyat Tahlili": "Creative Writing & Literary Analysis",
  "Süreli Deneme Sınavları": "Timed Practice Exams",
  "Zorlu Edebiyat Soruları": "Challenging Literature Questions",
  "Şiir & Edebi Sanatlar": "Poetry & Literary Arts",
  "Akıllı Dizin ve Etiketleme": "Smart Indexing & Tagging",
  "Manevi Kalkan ve Ahlak": "Spiritual Shield & Ethics",
  "Telegram Tartışma Grubu": "Telegram Discussion Group",
  "Sosyal Medya, Telegram Gruplarımız ve İletişim": "Social Media, Telegram Groups & Contact",
  "Sosyal Medya ve İletişim Kanallarımız": "Our Social Media & Contact Channels",
  "Doğrudan geliştiriciye ulaşabileceğiniz resmi iletişim adreslerimiz ve çalışma gruplarımız:": "Our official contact addresses and study groups where you can reach the developer directly:",
  "Resmî iletişim ve destek adreslerimiz:": "Our official contact and support channels:",
  "1 Dakikada Türkçe ÖABT": "Turkish ÖABT in 1 Minute",
  "F Telegram Çalışma ve Anket Gruplarımız": "F Telegram Study & Poll Groups",
  "ALΣF Türkçe ÖABT | Akademi Pırtılları 🐛🍊": "ALΣF Turkish ÖABT | Academy Pırtılları 🐛🍊",
  "📚 Türkçe ÖABT Anket Grubu": "📚 Turkish ÖABT Poll Group",
  "ALΣF Pırtılları YKS": "ALΣF Pırtılları YKS (University Exam)",
  "F Ekosistemi": "F Ecosystem",
  "Eğitim, Yayıncılık ve Dijital Yazılım Projeleri": "Education, Publishing & Digital Software Projects",
  "F Güvenlik Protokolü": "F Security Protocol",
  "KVKK & GDPR Kapsamlı Veri Bildirimi": "Comprehensive KVKK & GDPR Data Disclosure",
  "F • Yazar & Geliştirici: Sertan Çubukcu. Bütün hakları saklıdır.": "F • Author & Developer: Sertan Çubukcu. All rights reserved.",
  "F Türkçe ÖABT": "F Turkish ÖABT",
  "F Türkçe ÖABT, AL": "F Turkish ÖABT, AL"
};

const ALEF_MONTH_MAP = {
  "Oca": "Jan", "Şub": "Feb", "Mar": "Mar", "Nis": "Apr",
  "May": "May", "Haz": "Jun", "Tem": "Jul", "Ağu": "Aug",
  "Eyl": "Sep", "Eki": "Oct", "Kas": "Nov", "Ara": "Dec"
};

const ALEF_ATTR_MAP = {
  "Balinayı Zıplat": "Jump the Whale",
  "Mitolojik Balinayı Çağır": "Summon the Mythic Whale",
  "ALΣF Ana Sayfa": "ALΣF Home Page",
  "Dil Seçimi": "Language Selection",
  "Büyütmek için tıklayın": "Click to enlarge",
  "Önceki": "Previous",
  "Sonraki": "Next",
  "Görsel Büyütücü": "Image Lightbox",
  "Kapat": "Close",
  "Genişletilmiş Görüntü": "Enlarged Image"
};

function translateSingleString(norm) {
  if (!norm) return null;
  if (Object.prototype.hasOwnProperty.call(ALEF_I18N_MAP, norm)) {
    return ALEF_I18N_MAP[norm];
  }
  const mDate = norm.match(/^(Oca|Şub|Mar|Nis|May|Haz|Tem|Ağu|Eyl|Eki|Kas|Ara)\s+(\d{4})\s+tarihinde verildi$/);
  if (mDate) {
    return `Issued ${ALEF_MONTH_MAP[mDate[1]]} ${mDate[2]}`;
  }
  if (norm.startsWith("Yeterlilik Kimliği ")) {
    let rest = norm.slice("Yeterlilik Kimliği ".length);
    if (rest === "Motivasyon 3.0 Eğitimi") rest = "Motivation 3.0 Training";
    return `Credential ID ${rest}`;
  }
  const mRate = norm.match(/^★\s*(\d+),(\d+)\s*•\s*Ücretsiz$/);
  if (mRate) {
    return `★ ${mRate[1]}.${mRate[2]} • Free`;
  }
  return null;
}

let i18nInitialized = false;
let trackedTextNodes = [];
let trackedHtmlBlocks = [];
let trackedAttrs = [];
let origDocTitle = "";

function prepareI18nCatalog() {
  if (i18nInitialized) return;
  i18nInitialized = true;
  origDocTitle = document.title;

  // 1. Special mixed-HTML paragraphs where English word order differs
  document.querySelectorAll('.hero-subtitle, #internet-projeleri .store-banner p.text-justify').forEach(el => {
    const orig = el.innerHTML;
    let enHtml = null;
    if (orig.includes('Millî Eğitim Bakanlığı Akademi Giriş Sınavı')) {
      enHtml = 'A complete educational ecosystem meticulously developed for Republic of Türkiye Ministry of National Education Academy Entrance Exam (M<span class="sigma">Σ</span>B - AGS) and Turkish Teaching (ÖABT) candidates — featuring a comprehensive question pool, practice exams, topic summaries, the <strong>EğitimYayın Store</strong>, <strong>Google Play Books</strong>, the <strong>Dictionary of Turkic Myths</strong> digital culture portal, live web platforms, 8 interactive Telegram educational bots, and next-generation Android applications.';
    } else if (orig.includes('BÜTÜN mobil uygulamalar')) {
      enHtml = 'This Privacy Policy and Security Protocol is the complete and official security statement for <strong>ALL mobile applications</strong> developed and published by developer and author Sertan Çubukcu (AL<span class="sigma">Σ</span>F - M<span class="sigma">Σ</span>B - AGS, AL<span class="sigma">Σ</span>F Turkish ÖABT, AL<span class="sigma">Σ</span>F KPSS, AL<span class="sigma">Σ</span>F EKYS, Islamic Time: Shoulder to Shoulder, Qibla Finder, Karargâh, Mergen, Pırtıl, Asayiş Berko, and all future releases), the EğitimYayın Store, Google Play Books, online web services, and the Telegram educational bots ecosystem.';
    } else if (orig.includes('Üç Boyutlu Sayfa Kıvrılma')) {
      enHtml = 'A comprehensive culture portal uniting the 907-page original Annotated Encyclopedic Mythology Dictionary with <strong>3D Page-Curl Flipbook</strong> reading and realistic page-flip audio, Turkish text-to-speech (TTS), 7 reading themes, instant search across 874 mythological concepts and an etymology index, plus an interactive 3,868-question four-option trivia quiz under one roof.';
    }
    if (enHtml) {
      trackedHtmlBlocks.push({ el, tr: orig, en: enHtml });
      el.setAttribute('data-i18n-html-handled', 'true');
    }
  });

  // 2. Walk all text nodes outside .content-tr / .content-en / handled HTML blocks
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
  let node;
  while ((node = walker.nextNode())) {
    const parent = node.parentElement;
    if (!parent) continue;
    const tag = parent.tagName;
    if (tag === 'SCRIPT' || tag === 'STYLE') continue;
    if (parent.closest('.content-tr, .content-en, [data-i18n-html-handled="true"]')) continue;

    const raw = node.nodeValue;
    const norm = raw.trim().replace(/\s+/g, ' ');
    if (!norm) continue;

    const enVal = translateSingleString(norm);
    if (enVal) {
      const leadMatch = raw.match(/^\s*/);
      const trailMatch = raw.match(/\s*$/);
      const lead = leadMatch ? leadMatch[0] : '';
      const trail = trailMatch ? trailMatch[0] : '';
      trackedTextNodes.push({
        node,
        tr: raw,
        en: lead + enVal + trail
      });
    }
  }

  // 3. Track attributes (title, aria-label, alt)
  document.querySelectorAll('[title], [aria-label], [alt]').forEach(el => {
    ['title', 'aria-label', 'alt'].forEach(attr => {
      const val = el.getAttribute(attr);
      if (val && Object.prototype.hasOwnProperty.call(ALEF_ATTR_MAP, val)) {
        trackedAttrs.push({ el, attr, tr: val, en: ALEF_ATTR_MAP[val] });
      }
    });
  });
}

function initLanguage() {
  prepareI18nCatalog();
  const langButtons = document.querySelectorAll('.lang-btn');
  const dualContainers = document.querySelectorAll('.dual-lang-container');

  function setLanguage(lang) {
    if (lang !== 'en') lang = 'tr';
    document.documentElement.setAttribute('data-lang', lang);
    document.documentElement.lang = lang;

    langButtons.forEach(btn => {
      const isActive = btn.dataset.lang === lang;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });

    // Toggle dual-language privacy articles if present
    document.querySelectorAll('.content-tr').forEach(el => {
      el.hidden = (lang === 'en');
    });
    document.querySelectorAll('.content-en').forEach(el => {
      el.hidden = (lang === 'tr');
    });
    dualContainers.forEach(c => {
      c.style.gridTemplateColumns = '1fr';
    });

    // Translate all tracked HTML blocks, text nodes, and attributes across the whole page
    trackedHtmlBlocks.forEach(item => {
      item.el.innerHTML = (lang === 'en') ? item.en : item.tr;
    });
    trackedTextNodes.forEach(item => {
      item.node.nodeValue = (lang === 'en') ? item.en : item.tr;
    });
    trackedAttrs.forEach(item => {
      item.el.setAttribute(item.attr, (lang === 'en') ? item.en : item.tr);
    });

    if (lang === 'en') {
      if (origDocTitle.includes('Gizlilik Politikası')) {
        document.title = 'ALΣF | Privacy Policy and Security Protocol (GDPR & KVKK)';
      } else {
        document.title = 'ALΣF (ALEF) | Education, Publishing & Digital Projects Portal';
      }
    } else {
      document.title = origDocTitle;
    }

    try { localStorage.setItem('alef_site_lang', lang); } catch (e) {}
  }

  langButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      setLanguage(btn.dataset.lang);
    });
  });

  let savedLang = 'tr';
  try {
    const stored = localStorage.getItem('alef_site_lang');
    if (stored === 'en') savedLang = 'en';
  } catch (e) {}
  setLanguage(savedLang);
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
      const isEn = document.documentElement.getAttribute('data-lang') === 'en';
      copyText(
        'sertancubukcu@gmail.com',
        isEn ? 'Email address copied: sertancubukcu@gmail.com' : 'E-posta adresi kopyalandı: sertancubukcu@gmail.com'
      );
    });
  });
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
  // Balina zıplama sesi kullanıcı talebiyle kaldırıldı.
}

function playWaterCrash() {
  // Balina suya çarpma sesi kullanıcı talebiyle kaldırıldı.
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

function downloadHalTercumesiBelgesi() {
  const section = document.getElementById('hal-tercumesi');
  if (!section) return;
  const clone = section.cloneNode(true);
  const headBtns = clone.querySelector('.section-head');
  if (headBtns) headBtns.remove();

  // Remove decorative butterfly emoji in formal document if present
  clone.querySelectorAll('h3 span').forEach(sp => {
    if (sp.textContent && sp.textContent.includes('🦋')) sp.remove();
  });

  const printWin = window.open('', '_blank', 'width=980,height=860');
  if (!printWin) {
    window.print();
    return;
  }
  const htmlDoc = `<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Sertan Çubukcu — Hâl Tercümesi Belgesi</title>
  <style>
    @page {
      size: A4;
      margin: 20mm 18mm 20mm 18mm;
    }
    * {
      box-sizing: border-box;
      font-family: 'Times New Roman', Times, serif !important;
    }
    body {
      font-family: 'Times New Roman', Times, serif !important;
      font-size: 12pt !important;
      line-height: 1.55 !important;
      text-align: justify !important;
      color: #000000 !important;
      background: #f3f4f6;
      margin: 0;
      padding: 28px 16px 48px;
    }
    .doc-toolbar {
      max-width: 210mm;
      margin: 0 auto 20px auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      color: #ffffff !important;
      padding: 12px 22px;
      border-radius: 8px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
    }
    .doc-toolbar-title {
      color: #ffffff !important;
      font-size: 12pt !important;
      font-weight: bold !important;
    }
    .doc-toolbar button {
      background: #d97706;
      color: #ffffff !important;
      border: 1px solid #f59e0b;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: bold !important;
      font-size: 11pt !important;
      cursor: pointer;
    }
    .doc-toolbar button:hover {
      background: #b45309;
    }
    .doc-sheet {
      max-width: 210mm;
      margin: 0 auto;
      background: #ffffff;
      padding: 22mm 20mm;
      border: 1px solid #d1d5db;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    .doc-official-header {
      text-align: center !important;
      border-bottom: 2px double #000000;
      padding-bottom: 12px;
      margin-bottom: 18px;
    }
    .doc-official-header h1 {
      font-size: 14pt !important;
      font-weight: bold !important;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin: 0 0 4px 0;
      color: #000000 !important;
      text-align: center !important;
    }
    .doc-official-header .doc-sub {
      font-size: 12pt !important;
      font-weight: bold !important;
      color: #1f2937 !important;
      text-align: center !important;
    }
    .cv-hero-card, .cv-card {
      background: #ffffff !important;
      border: none !important;
      border-bottom: 1px solid #9ca3af !important;
      border-radius: 0 !important;
      padding: 12px 0 16px 0 !important;
      margin: 0 0 16px 0 !important;
    }
    .cv-grid {
      display: block !important;
    }
    .cv-card-header {
      display: flex !important;
      align-items: baseline !important;
      justify-content: space-between !important;
      border-bottom: 1.5px solid #000000 !important;
      padding-bottom: 4px !important;
      margin-bottom: 12px !important;
    }
    .cv-card-icon, .badge-dot {
      display: none !important;
    }
    h1, h2, h3, h4, .cv-role, strong {
      font-family: 'Times New Roman', Times, serif !important;
      font-size: 12pt !important;
      font-weight: bold !important;
      color: #000000 !important;
      margin: 0 0 4px 0 !important;
    }
    .cv-card-header h3 {
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }
    p, div, span, li, .cv-org {
      font-family: 'Times New Roman', Times, serif !important;
      font-size: 12pt !important;
      color: #000000 !important;
      text-align: justify !important;
      line-height: 1.55 !important;
    }
    .cv-timeline {
      display: block !important;
    }
    .cv-timeline-item {
      padding: 8px 0 10px 0 !important;
      margin-bottom: 8px !important;
      border-left: none !important;
      border-bottom: 1px dotted #d1d5db !important;
      page-break-inside: avoid;
    }
    .cv-timeline-item:last-child {
      border-bottom: none !important;
    }
    .cv-date-badge, .badge {
      background: transparent !important;
      color: #000000 !important;
      border: none !important;
      padding: 0 !important;
      font-size: 12pt !important;
      font-weight: bold !important;
      font-style: italic;
      display: block !important;
      margin-bottom: 2px !important;
    }
    .cv-org {
      font-style: italic;
      margin-bottom: 4px !important;
    }
    /* Sertifikalar ızgarasını belgede alt alta nizami liste görünümüne dönüştür */
    .cv-card > div[style*="grid-template-columns"] {
      display: block !important;
    }
    .cv-card > div[style*="grid-template-columns"] > div {
      background: #ffffff !important;
      border: none !important;
      border-bottom: 1px dotted #d1d5db !important;
      border-radius: 0 !important;
      padding: 8px 0 !important;
      margin-bottom: 4px !important;
      display: flex !important;
      flex-direction: row !important;
      justify-content: space-between !important;
      align-items: baseline !important;
      gap: 16px !important;
      page-break-inside: avoid;
    }
    .cv-card > div[style*="grid-template-columns"] > div > div:first-child > div:first-child {
      font-weight: bold !important;
    }
    a {
      color: #000000 !important;
      text-decoration: underline !important;
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      font-size: 12pt !important;
      font-weight: normal !important;
    }
    @media print {
      body {
        background: #ffffff !important;
        padding: 0 !important;
      }
      .doc-toolbar {
        display: none !important;
      }
      .doc-sheet {
        max-width: 100% !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
      }
    }
  </style>
</head>
<body>
  <div class="doc-toolbar">
    <div class="doc-toolbar-title">${document.documentElement.getAttribute('data-lang') === 'en' ? 'Sertan Çubukcu — Curriculum Vitae Document' : 'Sertan Çubukcu — Hâl Tercümesi Belgesi'}</div>
    <button onclick="window.print()">${document.documentElement.getAttribute('data-lang') === 'en' ? '🖨️ Save / Print Document' : '🖨️ Belgeyi Kaydet / Yazdır'}</button>
  </div>
  <div class="doc-sheet">
    <div class="doc-official-header">
      <h1>${document.documentElement.getAttribute('data-lang') === 'en' ? 'CURRICULUM VITAE' : 'HÂL TERCÜMESİ BELGESİ'}</h1>
      <div class="doc-sub">Sertan Çubukcu</div>
    </div>
    ${clone.innerHTML}
  </div>
  <script>setTimeout(function(){ window.print(); }, 450);<\/script>
</body>
</html>`;
  printWin.document.open();
  printWin.document.write(htmlDoc);
  printWin.document.close();
}

function startAllEngines() {
  initLanguage();
  initScreenshotsAndLightbox();
  initCopyActions();
  window.downloadHalTercumesiBelgesi = downloadHalTercumesiBelgesi;
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

  // Balinayı Çağır Butonu (Sessiz Zıplama)
  const summonBtn = document.getElementById('summonWhaleBtn');
  if (summonBtn) {
    summonBtn.addEventListener('click', (e) => {
      e.preventDefault();
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
