#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as des:
    l_desc = des.read()

data_files = [('share/applications', ['quran_rofi/assets/quran.desktop']),
              ('share/icons', ['quran_rofi/assets/quran.png']),
            ]

setup(
    name='quran_rofi',
    packages=find_packages(),
    version='0.1.7',
    entry_points={'console_scripts': ['quran-rofi = quran_rofi.quran:showAyat']},
    include_package_data=True,
    package_data={'': ['source/*.xml']},
    data_files=data_files,
    description='Al-Quran dengan Terjemahan / Tafsir Jalalayn',
    url='https://gitlab.com/nesstero/Al-Quran-Rofi',
    license='MIT',
    author='nestero',
    author_email='nestero@mail.com',
    install_requires=['pyrof', 'beautifulsoup4', 'lxml'],
    long_description=l_desc,
    long_description_content_type='text/markdown',
)
