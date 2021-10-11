#! /usr/bin/env python

from dynmen.rofi import Rofi
from bs4 import BeautifulSoup
from assets import *
from configparser import ConfigParser as conf
import pyperclip as c

cfg = conf()
config_folder = p.abspath(".config")
config_file = p.join(config_folder, "quran-rofi.ini") 

if not p.isfile(config_file):
    cfg.add_section("Font")
    cfg.set("Font", "font", "Al Qalam Quran Majeed 20")
    
    with open(config_file, "w") as cfg_ini:
        cfg.write(cfg_ini)
else:
    cfg.read(config_file)

font_quran = cfg["Font"]["font"]

al_quran = BeautifulSoup(quran, "xml")
terjemahan_id = BeautifulSoup(terjemahan, "xml")

list_ayat = []

class AlQuran():
    def __init__(self, index_surat):
        self.index_surat = index_surat
        self.surat = al_quran.find("sura", {"index":self.index_surat})
        self.surat_terjemahan = terjemahan_id.find("sura", {"index":self.index_surat})
    
    def Ayat(self, index_ayat):
        ayat = self.surat.find("aya", {"index":index_ayat})
        ayat = ayat.get("text")
        return ayat

    def JumlahAyat(self):
        global list_ayat
        ayat = self.surat.find_all("aya")
        jml_ayat = len(ayat)
        jml_ayat = jml_ayat + 1
        list_ayat = []
        for i in range (1, jml_ayat):
            i = str(i)
            list_ayat.append(i)
        return list_ayat
    
    def TerjemahanAyat(self, index_ayat):
        ayat_terjemahan = self.surat_terjemahan.find("aya", {"index":index_ayat})
        ayat_terjemahan = ayat_terjemahan.get("text")
        return ayat_terjemahan

def Menu():
    while True:
        menu_surat = Rofi(lines=11, columns=2, width=700, hide_scrollbar=True)
        menu_surat.case_sensitive = True
        menu_surat.prompt = "Al-Quran"
        menu_surat = menu_surat(id_surat)
        index_surat = menu_surat.value
        nama_surat = menu_surat.selected
        
        quran = AlQuran(index_surat)
        
        def MenuAyat():
            global index_ayat
            menu_ayat = Rofi(lines=3, columns=9, width=700, hide_scrollbar=True)
            menu_ayat.prompt = nama_surat
            jml_ayat = quran.JumlahAyat()
            menu_ayat = menu_ayat(list_ayat)
            index_ayat = menu_ayat.selected
        MenuAyat()

        def AyatdanTerjemahan():
            global ayat, panjang_ayat, terjemahan_ayat, panjang_terjemahan
            ayat = quran.Ayat(index_ayat)
            panjang_ayat = len(ayat)
            terjemahan_ayat = quran.TerjemahanAyat(index_ayat)
            panjang_terjemahan = len(terjemahan_ayat)
        AyatdanTerjemahan()
        
        def CopyAyat():
            ayat_dan_terjemahan = f"Ayat {index_ayat} Surat {nama_surat}: \n {ayat} \n Tafsir Jalalayn: \n {terjemahan_ayat}"
            c.copy(ayat_dan_terjemahan)

        l_menu_tampil_ayat = {"Tafsir Jalalayn", "Ayat"}
        l_menu_tampil_ayat = sorted(l_menu_tampil_ayat)
        def TampilAyat():
            global p_tampil_ayat
            if panjang_ayat >= 500:
                menu_tampil_ayat = Rofi(lines=1, columns=2, width=1270, font=font_quran, hide_scrollbar=True)
            else:
                menu_tampil_ayat = Rofi(lines=1, columns=2, width=700, font=font_quran, hide_scrollbar=True)
            tampil_ayat = f"\n {ayat} \n"
            menu_tampil_ayat.prompt = f"Ayat {index_ayat} Surat {nama_surat}"
            menu_tampil_ayat.mesg = tampil_ayat
            menu_tampil_ayat = menu_tampil_ayat(l_menu_tampil_ayat)
            p_tampil_ayat = menu_tampil_ayat.selected
        TampilAyat()

        def TampilTerjemahan():
            if p_tampil_ayat == "Tafsir Jalalayn":
                l_menu_tampil_terjemahan = {"Ayat", "Surat", "Copy"}
                l_menu_tampil_terjemahan = sorted(l_menu_tampil_terjemahan)
                if panjang_terjemahan >= 1000:
                    menu_tampil_terjemahan = Rofi(lines=1, columns=3, width=1270, hide_scrollbar=True)
                else:
                    menu_tampil_terjemahan = Rofi(lines=1, columns=3, width=700, hide_scrollbar=True)
                menu_tampil_terjemahan.prompt = f"Tafsir Jalalayn Surat {nama_surat} Ayat {index_ayat}"
                menu_tampil_terjemahan.mesg = terjemahan_ayat
                menu_tampil_terjemahan = menu_tampil_terjemahan(l_menu_tampil_terjemahan)
                p_tampil_terjemahan = menu_tampil_terjemahan.selected
                if p_tampil_terjemahan == "Ayat":
                    AyatdanTerjemahan()
                    TampilAyat()
                    TampilTerjemahan()
                elif p_tampil_terjemahan == "Surat":
                    Menu()
                elif p_tampil_terjemahan == "Copy":
                    CopyAyat()
                    exit()
                else:
                    exit()
            elif p_tampil_ayat == "Ayat":
                MenuAyat()
                AyatdanTerjemahan()
                TampilAyat()
                TampilTerjemahan()
            else:
                exit()
        TampilTerjemahan()
Menu()
