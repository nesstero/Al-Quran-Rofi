#! /usr/bin/env python
from os import path as p
from os import environ as env
from configparser import ConfigParser as conf

user = env["USER"]
cfg = conf()
config_file = f"/home/{user}/.config/quran-rofi.ini"

if not p.isfile(config_file):
    cfg.add_section("Font")
    cfg.set("Font", "font", "Al Qalam Quran Majeed 20")
    
    cfg.add_section("Tafsir")
    cfg.set("Tafsir", "tafsir", "true")
    
    with open(config_file, "w") as cfg_ini:
        cfg.write(cfg_ini)
else:
    cfg.read(config_file)

opt_tafsir = cfg["Tafsir"]["tafsir"]

f = p.dirname(p.abspath(__file__))
quran = p.join(f, "source/quran.xml")
if opt_tafsir == "true":
    terjemahan = p.join(f, "source/tafsir.xml")
else:
    terjemahan = p.join(f, "source/terjemahan.xml")

with open(quran, "r") as q:
    quran = q.read()

with open(terjemahan, "r") as t:
    terjemahan = t.read()

font_quran = cfg["Font"]["font"]
r_surat = 'listview {lines: 11; columns: 2;} window {width: 700px; border-radius: 6px;}'
r_ayat = 'listview {lines: 3; columns: 11;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
r_ayat_pendek = 'textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 5;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}' 
r_ayat_panjang = 'textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 5;} element-text {horizontal-align: 0.5;} window {width: 1000px; border-radius: 6px;}'
r_ter_pendek = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
r_ter_panjang = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
