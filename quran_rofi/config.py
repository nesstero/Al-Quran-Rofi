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
    
    with open(config_file, "w") as cfg_ini:
        cfg.write(cfg_ini)
else:
    cfg.read(config_file)

font_quran = cfg["Font"]["font"]

ayat_panjang = 'textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 5;} element-text {horizontal-align: 0.5;} window {width: 1000px; border-radius: 6px;}'
ayat_pendek = 'textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 5;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}' 
terjemahan_panjang = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 1000px; border-radius: 6px;}'
terjemahan_pendek = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
tafsir_panjang = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 1300px;}'
tafsir_pendek = 'listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 700px; border-radius: 6px;}'
