#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as des:
    l_desc = des.read()

setup(
    name='quran_rofi',
    packages=find_packages(),
    version='0.1.4',
    entry_points={'console_scripts': ['quran-rofi = quran_rofi.quran:Menu']},
    include_package_data=True,
    package_data={'': ['source/*.xml']},
    description='Al-Quran dengan Terjemahan / Tafsir Jalalayn',
    url='https://github.com/nesstero/Al-Quran-Rofi',
    license='MIT',
    author='nesstero',
    author_email='nestero@tuta.io',
    install_requires=['pyrof', 'beautifulsoup4', 'lxml'],
    long_description=l_desc,
    long_description_content_type='text/markdown',
)
