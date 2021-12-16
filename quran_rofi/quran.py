#! /usr/bin/env python

from .surat import *
from .data import *
from pyrof.rofi import Rofi
from bs4 import BeautifulSoup
import subprocess as sub

al_quran = BeautifulSoup(quran, "xml")
terjemahan_id = BeautifulSoup(terjemahan, "xml")

class AlQuran():
    def __init__(self, index_surat):
        self.index_surat = index_surat
        self.surat = al_quran.find("sura", {"index": self.index_surat})
        self.surat_terjemahan = terjemahan_id.find("sura", {"index": self.index_surat})

    def Ayat(self, index_ayat):
        ayat = self.surat.find("aya", {"index": index_ayat})
        ayat = ayat.get("text")
        return ayat

    def JumlahAyat(self):
        global list_ayat
        ayat = self.surat.find_all("aya")
        jml_ayat = len(ayat) + 1
        list_ayat = []
        for i in range (1, jml_ayat):
            i = str(i)
            list_ayat.append(i)
        return list_ayat

    def TerjemahanAyat(self, index_ayat):
        ayat_terjemahan = self.surat_terjemahan.find("aya", {"index": index_ayat})
        ayat_terjemahan = ayat_terjemahan.get("text")
        return ayat_terjemahan

def getSurat():
    t_str = 'listview {lines: 11; columns: 2;} window {width: 700px; border-radius: 6px;}'
    menu = Rofi(theme_str=t_str)
    menu.case_insensitive = True
    menu.prompt = "Al-Quran"
    menu = menu(id_surat)
    index_surat = menu.value
    nama_surat = menu.selected
    return index_surat, nama_surat
    
def getIdAyat():
    global quran
    surat = getSurat()
    quran = AlQuran(surat[0])
    jml_ayat = quran.JumlahAyat()
    t_str = 'listview {lines: 3; columns: 11;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
    menu = Rofi(theme_str=t_str)
    menu.prompt = surat[1]
    menu = menu(jml_ayat)
    index_ayat = menu.selected
    return index_ayat, surat[1]

def showAyat():
    index_ayat = getIdAyat()
    id_ayat = index_ayat[0]
    nama_surat = index_ayat[1]
    ayat = quran.Ayat(id_ayat)
    terjemahan = quran.TerjemahanAyat(id_ayat)
    
    def tampil(theme, ayat_terjemahan, prompt, opt):
        menu = Rofi(theme_str=theme)
        menu.prompt = prompt
        menu.mesg = ayat_terjemahan
        menu = menu(opt)
        menu_opt = menu.selected
        return menu_opt

    def tampilAyat():
        if len(ayat) >= 1000:
            t_ayat = ayat_panjang 
        else:
            t_ayat = ayat_pendek 
        menu_ayat = ("Next", "Prev", "Surat", "Terjemahan")
        m_ayat = tampil(t_ayat, f"\n {ayat} \n", f"{nama_surat} Ayat {id_ayat}", menu_ayat)
        if m_ayat == menu_ayat[0]:
            nextAyat()
        elif m_ayat == menu_ayat[1]:
            prevAyat()
        elif m_ayat == menu_ayat[2]:
            showAyat()
        elif m_ayat == menu_ayat[3]:
            tampilTerjemahan()

    def tampilTerjemahan():
        if len(terjemahan) >=1000:
            t_terjemahan = terjemahan_panjang 
        else:
            t_terjemahan = terjemahan_pendek 
        menu_terjemahan = ("Back to Ayat", "Copy")
        m_terjemahan = tampil(t_terjemahan, terjemahan, f"Terjemahan {nama_surat} ayat {id_ayat}", menu_terjemahan)
        if m_terjemahan == menu_terjemahan[0]:
            tampilAyat()
        elif m_terjemahan == menu_terjemahan[1]:
            copyAyat()

    def nextAyat():
        nonlocal id_ayat, ayat, terjemahan
        id_ayat = int(id_ayat) + 1
        jml_ayat = quran.JumlahAyat()
        jml_ayat = len(jml_ayat) + 1
        if id_ayat == jml_ayat:
            showAyat()
        else:
            ayat = quran.Ayat(id_ayat)
            terjemahan = quran.TerjemahanAyat(id_ayat)
            tampilAyat()
    
    def prevAyat():
        nonlocal id_ayat, ayat, terjemahan
        id_ayat = int(id_ayat) - 1
        if id_ayat == 0:
            showAyat()
        else:
            ayat = quran.Ayat(id_ayat)
            terjemahan = quran.TerjemahanAyat(id_ayat)
            tampilAyat()
    
    def copyAyat():
        if opt_tafsir == "true":
            ayat_dan_terjemahan = f"Ayat {id_ayat} Surat {nama_surat}: \n {ayat} \n Tafsir Jalalayn: \n {terjemahan}"
        else:    
            ayat_dan_terjemahan = f"Ayat {id_ayat} Surat {nama_surat}: \n {ayat} \n Terjemahan: \n {terjemahan}"
        copy_ayat = sub.Popen(['xclip', '-selection', 'clipboard'], stdin=sub.PIPE, close_fds=True)
        copy_ayat.communicate(input=ayat_dan_terjemahan.encode("utf-8"))

    tampilAyat()


showAyat()
