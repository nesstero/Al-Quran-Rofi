#! /usr/bin/env python
from os import path as p
from os import environ as env
from configparser import ConfigParser as conf
from .surat import *

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
quran = p.join(f, "quran.xml")
if opt_tafsir == "true":
    terjemahan = p.join(f, "tafsir.xml")
else:
    terjemahan = p.join(f, "terjemahan.xml")

with open(quran, "r") as q:
    quran = q.read()

with open(terjemahan, "r") as t:
    terjemahan = t.read()

font_quran = cfg["Font"]["font"]
