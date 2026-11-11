@echo off
chcp 65001 >nul
echo ====================================================
echo  ALΣF Portal - GitHub Pages Otomatik Yükleme Aracı
echo ====================================================
echo.

if not exist .git (
    echo [1/4] Git deposu baslatiliyor...
    git init
    git branch -M main
)

echo [2/4] Tum dosyalar (56 adet secilmis asset) hazirlaniyor...
git add .

echo [3/4] Degisiklikler paketleniyor...
git commit -m "ALΣF Portal V4: 3B Balina, Okyanus, Simsek ve Tum Resimler"

echo.
echo [4/4] GitHub baglantisi:
echo Eger GitHub depon henuz bagli degilse, asagidaki komutu calistir:
echo   git remote add origin https://github.com/KULLANICI_ADIN/REPO_ADIN.git
echo   git push -u origin main --force
echo.
echo Eger depon zaten bagliysa simdi gonderiliyor:
git push -u origin main
echo.
echo ====================================================
echo Islem tamamlandi! Tarayicini yenileyebilirsin.
echo ====================================================
pause
