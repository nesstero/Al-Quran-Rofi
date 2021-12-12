# Al-Quran Rofi
Al-Quran dengan Terjemahan / Tafsir Jalalayn

## Install
#### Requirements
- [Rofi](https://github.com/davatorium/rofi)
- [xclip](https://github.com/astrand/xclip)
- Al-Quran Rofi menggunakan font [Al Qalam Quran Majeed](https://github.com/nesstero/Al-Quran-Rofi/raw/master/quran_rofi/Font/Al%20Qalam%20Quran%20Majeed.ttf)
#### Installasi
- `pip install quran-rofi`

## Configure
untuk pengaturan font Quran dan opsi terjemahan atau tafsir ada di file `~/.config/quran-rofi.ini`

## Icon Desktop
File `.desktop` Al-Quran Rofi ada di `~/.local/share/applications/quran.desktop`, jika icon desktop pada `rofi drun` tidak muncul bisa di ubah file `quran.desktop` pada bagian Icon:
```
[Desktop Entry]
Type=Application
Name=Al'Quran Rofi
Icon=~/.local/share/icons/quran.png
TryExec=quran-rofi
Exec=quran-rofi
Terminal=false
```

## Preview Al-Quran Rofi
![Al-Quran Rofi](https://github.com/nesstero/Al-Quran-Rofi/raw/master/ss.png)
