#! /usr/bin/env python

from os import path as p
from playsound import playsound as ply
from os import path as p
import asyncio

dir_audio = p.dirname(p.abspath(__file__))
def PlayAudio(index_surat, index_ayat):
    f_audio = f"{index_surat}/{index_ayat}.mp3"
    audio = p.join(dir_audio, "audio/", f_audio)
    ply(audio)

