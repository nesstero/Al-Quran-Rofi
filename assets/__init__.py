#! /usr/bin/env python
from os import path as p
from .surat import *

f = p.dirname(p.abspath(__file__))
quran = p.join(f, "quran.xml")
terjemahan = p.join(f, "terjemahan.xml")

with open(quran, "r") as q:
    quran = q.read()

with open(terjemahan, "r") as t:
    terjemahan = t.read()
