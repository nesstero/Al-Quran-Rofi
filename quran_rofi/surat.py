#! /usr/bin/env python
id_surat = {
        "Al-Fatihah (Pembukaan)":"1",
        "Al-Baqarah (Sapi Betina)":"2",
        "Ali Imran (Keluarga Imran)":"3",
        "An-Nisaa (Wanita)":"4",
        "Al-Ma'idah (Hidangan / Jamuan Makanan)":"5",
        "Al-An'am (Binatang Ternakan)":"6",
        "Al-A'raf (Tempat Yang Tertinggi)":"7",
        "Al-Anfal (Harta Rampasan Perang)":"8",
        "At-Taubah (Pengampunan)":"9",
        "Yunus (Nabi Yunus)":"10",
        "Hud (Nabi Hud)":"11",
        "Yusuf (Nabi Yusuf)":"12",
        "Ar-Ra’d (Guruh / Petir)":"13",
        "Ibrahim (Nabi Ibrahim)":"14",
        "Al-Hijr (Gunung Al Hijr)":"15",
        "An-Nahl (Lebah)":"16",
        "Al-Isra (Perjalanan Malam)":"17",
        "Al-Kahf (Penghuni-Penghuni Gua)":"18",
        "Maryam":"19",
        "Ta Ha":"20",
        "Al-Anbiya (Nabi-Nabi)":"21",
        "Al-Hajj (Haji)":"22",
        "Al-Mu’minun (Orang-Orang Mukmin)":"23",
        "An-Nur (Cahaya)":"24",
        "Al-Furqan (Pembeda)":"25",
        "Asy-Syu’ara (Penyair)":"26",
        "An-Naml (Semut)":"27",
        "Al-Qasas (Kisah)":"28",
        "Al-‘Ankabut (Laba-Laba)":"29",
        "Ar-Rum (Bangsa Romawi)":"30",
        "Luqman (Keluarga Luqman)":"31",
        "As-Sajdah (Sajdah)":"32",
        "Al-Ahzab (Golongan-Golongan Yang Bersekutu)":"33",
        "Saba (Kaum Saba)":"34",
        "Fatir (Pencipta)":"35",
        "Ya Sin (Yaasiin)":"36",
        "As-Saffat (Barisan-Barisan)":"37",
        "Sad (Shaad)":"38",
        "Az-Zumar (Rombongan-Rombongan)":"39",
        "Al-Mu’min/Ghafir (Orang Beriman, Pengampun)":"40",
        "Fussilat (Yang Dijelaskan)":"41",
        "Asy-Syuraa (Musyawarah)":"42",
        "Az-Zukhruf (Perhiasan)":"43",
        "Ad-Dukhan (Kabut)":"44",
        "Al-Jasiyah (Yang Bertekuk Lutut)":"45",
        "Al-Ahqaf (Bukit-Bukit Pasir)":"46",
        "Muhammad (Nabi Muhammad)":"47",
        "Al-Fath (Kemenangan)":"48",
        "Al-Hujurat (Kamar-Kamar)":"49",
        "Qaf":"50",
        "Az-Zariyat (Angin Yang Menerbangkan)":"51",
        "At-Tur (Bukit)":"52",
        "An-Najm (Binatang)":"53",
        "Al-Qamar (Bulan)":"54",
        "Ar-Rahman (Yang Maha Pemurah)":"55",
        "Al-Waqi’ah (Hari Kiamat)":"56",
        "Al-Hadid (Besi)":"57",
        "Al-Mujadilah (Wanita Yang Mengajukan Gugatan)":"58",
        "Al-Hasyr (Pengusiran)":"59",
        "Al-Mumtahanah (Wanita Yang Diuji)":"60",
        "As-Saff (Satu Barisan)":"61",
        "Al-Jumu’ah (Hari Jum’at)":"62",
        "Al-Munafiqun (Orang-Orang Yang Munafik)":"63",
        "At-Tagabun (Hari Dinampakkan Kesalahan-Kesalahan)":"64",
        "At-Talaq (Talak)":"65",
        "At-Tahrim (Mengharamkan)":"66",
        "Al-Mulk (Kerajaan)":"67",
        "Al-Qalam (Pena)":"68",
        "Al-Haqqah (Hari Kiamat)":"69",
        "Al-Ma’arij (Tempat Naik)":"70",
        "Nuh (Nabi Nuh)":"71",
        "Al-Jinn (Jin)":"72",
        "Al-Muzzammil (Orang Yang Berselimut)":"73",
        "Al-Muddassir (Orang Yang Berselubung)":"74",
        "Al-Qiyamah (Hari Kebangkitan / Kiamat)":"75",
        "Al-Insan (Manusia)":"76",
        "Al-Mursalat (Malaikat-Malaikat Yang Diutus)":"77",
        "An-Naba (Berita Besar)":"78",
        "An-Nazi’at (Malaikat-Malaikat Yang Mencabut)":"79",
        "Abasa (Ia Bermuka Masam)":"80",
        "At-Takwir (Menggulung)":"81",
        "Al-Infitar (Terbelah)":"82",
        "Al-Tatfif (Orang-Orang Yang Curang)":"83",
        "Al-Insyiqaq (Terbelah)":"84",
        "Al-Buruj (Gugus Bintang)":"85",
        "At-Tariq (Yang Datang di Malam Hari)":"86",
        "Al-A’la (Yang Paling Tinggi)":"87",
        "Al-Gasyiyah (Hari Pembalasan)":"88",
        "Al-Fajr (Fajar)":"89",
        "Al-Balad (Negeri)":"90",
        "Asy-Syams (Matahari)":"91",
        "Al-Lail (Malam)":"92",
        "Ad-Duha (Waktu Dhuha)":"93",
        "Al-Insyirah (Melapangkan)":"94",
        "At-Tin (Buah Tin)":"95",
        "Al-‘Alaq (Segumpal Darah)":"96",
        "Al-Qadr (Kemuliaan)":"97",
        "Al-Bayyinah (Pembuktian)":"98",
        "Az-Zalzalah (Kegoncangan)":"99",
        "Al-‘Adiyat (Berlari Kencang)":"100",
        "Al-Qari’ah (Hari Kiamat)":"101",
        "At-Takasur (Bermegah-Megahan)":"102",
        "Al-‘Asr (Masa/Waktu)":"103",
        "Al-Humazah (Pengumpat)":"104",
        "Al-Fil (Gajah)":"105",
        "Quraisy":"106",
        "Al-Ma’un (Barang-Barang Yang Berguna)":"107",
        "Al-Kausar (Nikmat Yang Berlimpah)":"108",
        "Al-Kafirun (Orang-Orang Kafir)":"109",
        "An-Nasr (Pertolongan)":"110",
        "Al-Lahab (Gejolak Api)":"111",
        "Al-Ikhlas (Ikhlas)":"112",
        "Al-Falaq (Waktu Subuh)":"113",
        "An-Nas (Umat Manusia)":"114"
        }