# Al-Quran Rofi
Al-Quran dengan Terjemahan / Tafsir Jalalayn

## Install
#### Requirements
- [Rofi](https://github.com/davatorium/rofi)
- [xclip](https://github.com/astrand/xclip)
- Al-Quran Rofi menggunakan font [Al Qalam Quran Majeed](https://gitlab.com/nesstero/Al-Quran-Rofi/-/blob/master/quran_rofi/assets/Al%20Qalam%20Quran%20Majeed.ttf)
#### Installasi
- `pip install quran-rofi`

## Configure
- Pengaturan font Quran dan Murotal ada di file `~/.config/quran-rofi.ini`, untuk contoh confignya ada **[disini](https://gitlab.com/nesstero/Al-Quran-Rofi/-/blob/master/quran_rofi/assets/contoh_confgi_quran-rofi.ini)**

- File Murotal ada di folder `~/.local/share/Quran/murotal/`, untuk contoh formatnya  ada **[disini](https://gitlab.com/nesstero/Al-Quran-Rofi/-/tree/master/quran_rofi/assets/murotal)**

## Font
Update cache font dengan :
```
$ fc-cache -fv
```

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


## Perubahan 
###[0.1.8](https://pypi.org/project/quran-rofi/0.1.8/)
- Menggunakan **[alquran-id](https://pypi.org/project/alquran-id/)**
