#! /usr/bin/env python
from os import path as p
from appdirs import user_data_dir, user_config_dir
from configparser import ConfigParser as conf
from pydub import AudioSegment as audio
from pydub.playback import play

data_dir = user_data_dir("Quran")
cfg_dir = user_config_dir()
cfg = conf()
config_file = f"{cfg_dir}/quran-rofi.ini"

if not p.isfile(config_file):
    cfg.add_section("Font")
    cfg.set("Font", "font", "Al Qalam Quran Majeed 20")

    cfg.add_section("Murotal")
    cfg.set("Murotal", "qori", "Saad Al-Gamdi")
    cfg.set("Murotal", "murotal", "off")
    cfg.set("Murotal", "autoplay", "off")
    
    with open(config_file, "w") as cfg_ini:
        cfg.write(cfg_ini)
else:
    cfg.read(config_file)

murotal = cfg["Murotal"]["murotal"]
autoplay = cfg["Murotal"]["autoplay"]

def Murotal(id_surat, id_ayat):
    qori = cfg["Murotal"]["qori"] 
    murotal = f"{data_dir}/murotal/{qori}/{id_surat}/{id_ayat}.mp3"
    murotal = audio.from_mp3(murotal)
    play(murotal)

font_quran = cfg["Font"]["font"]
ayat_panjang = 'inputbar {children: [prompt];} textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 6;} element-text {horizontal-align: 0.5;} window {width: 900px; border-radius: 6px;}'
ayat_pendek = 'inputbar {children: [prompt];} textbox {font : ' '"' + font_quran + '"' ';} listview {lines: 1; columns: 6;} element-text {horizontal-align: 0.5;} window {width: 650px; border-radius: 6px;}' 
terjemahan_panjang = 'inputbar {children: [prompt];} listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 900px; border-radius: 6px;}'
terjemahan_pendek = 'inputbar {children: [prompt];} listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 650px; border-radius: 6px;}'
tafsir_panjang = 'inputbar {children: [prompt];} listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 1300px;}'
tafsir_pendek = 'inputbar {children: [prompt];} listview {lines: 1; columns: 3;} element-text {horizontal-align: 0.5;} window {width: 650px; border-radius: 6px;}'
