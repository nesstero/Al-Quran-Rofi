# Al-Quran Rofi
Al-Quran dengan Terjemahan / Tafsir Jalalayn

## Instalasi Al-Quran Rofi untuk Archlinux
untuk pengguna distro Archlinux dengan paket manager paru:
```
paru -S quran-rofi
```

## Instalasi Al-Quran Rofi untuk distro lain
- Install dependensi utama yang dibutuhkan yakni rofi, contoh untuk distro ubuntu/debian
```
sudo apt install rofi
```
- Pastikan library yang ada sudah terinstall semua denan menggunaka
```
pip install --user requirements.txt
```
- Jalankan Al-Quran Rofi dengan `python3 Quran.py` atau bisa juga dengan :
- `mv Quran.py Quran`, `chmod +x Quran` dan jalankan dengan `./Quran`


## Fonts
pengaturan font ada di variabel `font_quran`

## Preview Al-Quran Rofi
![Al-Quran Rofi](ss.png)
