#! /usr/bin/env python

from alquran_id import AlQuran as Quran
from .surat import *
from .config import *
from pyrof.rofi import Rofi
import subprocess as sub
from threading import Thread as thr

class quranRofi():
    
    def __init__(self):
        self.quran = Quran()

    def surat(self):
        th = 'listview {lines: 11; columns: 2;} window {width: 700px; border-radius: 6px;}'
        menu = Rofi(theme_str=th)
        menu.case_insensitive = True
        menu.prompt = "Al Quran"
        menu = menu(idSurat)
        id_surat = menu.value
        nama_surat = menu.selected
        return id_surat, nama_surat

    def idAyat(self):
        surat = self.surat()
        id_surat = surat[0]
        nama_surat = surat[1]
        jml_ayat = self.quran.JumlahAyat(id_surat)
        list_ayat = []
        for i in range(1, jml_ayat + 1):
            i = str(i)
            list_ayat.append(i)
        th = 'listview {lines: 3; columns: 11;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
        menu = Rofi(theme_str=th)
        menu.prompt = nama_surat
        menu = menu(list_ayat)
        id_ayat = menu.selected
        return nama_surat, id_surat, id_ayat, jml_ayat

    def getayat(self):
        quran = self.idAyat()
        nama_surat = quran[0]
        id_surat = quran[1]
        id_ayat = quran[2]
        jml_ayat = quran[3]
        ayat = self.quran.Ayat(id_surat, id_ayat)
        terjemahan = self.quran.Terjemahan(id_surat, id_ayat)
        tafsir = self.quran.Tafsir(id_surat, id_ayat)
        return nama_surat, id_surat, jml_ayat, id_ayat, ayat, terjemahan, tafsir

def showSurat():
    quran_rofi = quranRofi()
    Ayat = quran_rofi.getayat()
    nama_surat = Ayat[0]
    id_surat = Ayat[1]
    jml_ayat = Ayat[2]
    id_ayat = Ayat[3]
    terjemahan = Ayat[5]
    tafsir = Ayat[6]
    ayat = Ayat[4]
    
    def showRofi(theme, text, prompt, opt):
        menu = Rofi(theme_str=theme)
        menu.prompt = prompt
        menu.mesg = text
        menu = menu(opt)
        menu = menu.selected
        return menu
        
    def playMurotal():
        Murotal(id_surat, id_ayat)
    
    def showAyat():
        if len(ayat) >= 1000:
            th = ayat_panjang
        else:
            th = ayat_pendek
        if murotal == "on":
            opt_ayat = ("Next", "Prev", "Terjemahan",  "Tafsir", "Surat", "Play")
        else:
            opt_ayat = ("Next", "Prev", "Terjemahan",  "Tafsir", "Surat")
        show = showRofi(th, f"\n{ayat}\n", f"{nama_surat} ayat {id_ayat}:", opt_ayat)
        if show == opt_ayat[0]:
            nextAyat()
        elif show == opt_ayat[1]:
            prevAyat()
        elif show == opt_ayat[2]:
            showTerjemahan()
        elif show == opt_ayat[3]:
            showTafsir()
        elif show == opt_ayat[4]:
            showSurat()
        elif show == opt_ayat[5]:
            thr(target=playMurotal).start()
            thr(target=showAyat).start()
    
    def showTerjemahan():
        if len(terjemahan) >= 1000:
            th = terjemahan_panjang
        else:
            th = terjemahan_pendek
        opt_terjemahan = ("Back", "Copy")
        show = showRofi(th, f"{terjemahan}", f"Terjemahan {nama_surat} ayat {id_ayat}:", opt_terjemahan)
        if show == opt_terjemahan[0]:
            showAyat()
        elif show == opt_terjemahan[1]:
            copy()
    
    def showTafsir():
        if len(tafsir) >= 1850:
            th = tafsir_panjang
        else:
            th = tafsir_pendek
        opt_tafsir = ("Back", "Copy")
        show = showRofi(th, f"{tafsir}", f"Tafsir {nama_surat} ayat {id_ayat}:", opt_tafsir)
        if show == opt_tafsir[0]:
            showAyat()
        elif show == opt_tafsir[1]:
            copy()

    def nextAyat():
        nonlocal nama_surat, id_surat, id_ayat, ayat, terjemahan, tafsir
        quran = Quran()
        id_ayat = int(id_ayat) + 1
        jml_ayt = quran.JumlahAyat(id_surat)
        if id_surat == "114" and id_ayat == jml_ayt + 1:
            showSurat()
        elif id_ayat == jml_ayt + 1:
            id_surat = int(id_surat) + 1
            id_ayat = 1
            nama_surat = list(idSurat).index(nama_surat)
            nama_surat = nama_surat + 1
            nama_surat = list(idSurat)[nama_surat]
            ayat = quran.Ayat(id_surat, id_ayat)
            terjemahan = quran.Terjemahan(id_surat, id_ayat)
            tafsir = quran.Tafsir(id_surat, 1)
            if autoplay == "on":
                thr(target=playMurotal).start()
                thr(target=showAyat).start()
            else:
                showAyat()
        else:
            ayat = quran.Ayat(id_surat, id_ayat)
            terjemahan = quran.Terjemahan(id_surat, id_ayat)
            tafsir = quran.Tafsir(id_surat, id_ayat)
            if autoplay == "on":
                thr(target=playMurotal).start()
                thr(target=showAyat).start()
            else:
                showAyat()

    def prevAyat():
        nonlocal nama_surat, id_surat, id_ayat, ayat, terjemahan, tafsir
        quran = Quran()
        id_ayat = int(id_ayat) - 1
        id_surat = int(id_surat)
        if id_surat == 1 and id_ayat == 0:
            showSurat()
        elif id_ayat == 0:
            id_surat = int(id_surat) - 1
            id_ayat = quran.JumlahAyat(id_surat)
            nama_surat = list(idSurat).index(nama_surat)
            nama_surat = nama_surat - 1
            nama_surat = list(idSurat)[nama_surat]
            ayat = quran.Ayat(id_surat, id_ayat)
            terjemahan = quran.Terjemahan(id_surat, id_ayat)
            tafsir = quran.Tafsir(id_surat, id_ayat)
            if autoplay == "on":
                thr(target=playMurotal).start()
                thr(target=showAyat).start()
            else:
                showAyat()
        else:
            ayat = quran.Ayat(id_surat, id_ayat)
            terjemahan = quran.Terjemahan(id_surat, id_ayat)
            tafsir = quran.Tafsir(id_surat, id_ayat)
            if autoplay == "on":
                thr(target=playMurotal).start()
                thr(target=showAyat).start()
            else:
                showAyat()

    def copy():
        quran_text = f"Surat {nama_surat} Ayat {id_ayat} : \n {ayat} \n Terjemahan: \n {terjemahan} \n Tafsir: \n {tafsir}"
        copy_quran = sub.Popen(['xclip', '-selection', 'clipboard'], stdin=sub.PIPE, close_fds=True)
        copy_quran.communicate(input=quran_text.encode("utf-8"))

    if autoplay == "on":
        thr(target=playMurotal).start()
        thr(target=showAyat).start()
    else:
        showAyat()

showSurat()
