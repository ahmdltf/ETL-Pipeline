# ETL Pipeline - Fashion Product Data Scraping

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-Unit%20Testing-yellow.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Google%20Sheets](https://img.shields.io/badge/Google%20Sheets-Storage-success.svg)

## Overview

ETL Pipeline merupakan proyek **Extract, Transform, Load (ETL)** yang dikembangkan sebagai bagian dari submission kelas **Belajar Fundamental Pemrosesan Data** di Dicoding.

Pipeline ini melakukan proses otomatis mulai dari mengambil data produk fashion melalui web scraping, membersihkan data sesuai kebutuhan analisis, hingga menyimpan hasil akhirnya ke beberapa media penyimpanan.

Implementasi proyek menerapkan konsep **modular programming**, sehingga setiap tahapan ETL dipisahkan ke dalam modul yang berbeda agar mudah dipelihara, diuji, dan dikembangkan.

---

# Background

Data merupakan aset penting dalam proses pengambilan keputusan. Namun, data yang diperoleh dari internet sering kali masih mengandung informasi yang tidak konsisten, duplikat, maupun data yang tidak valid.

Melalui proyek ini dibangun sebuah ETL Pipeline sederhana yang mampu:

* mengambil data dari website secara otomatis,
* membersihkan kualitas data,
* mengubah format data agar siap digunakan,
* menyimpan hasil transformasi ke beberapa repositori data,
* memastikan setiap tahapan dapat diuji menggunakan unit testing.

---

# Objectives

Proyek ini bertujuan untuk:

* Melakukan web scraping pada seluruh halaman website target.
* Membersihkan data hasil scraping.
* Mengubah format data agar sesuai kebutuhan analisis.
* Menyimpan data ke berbagai media penyimpanan.
* Menerapkan struktur kode yang modular.
* Mengimplementasikan unit testing terhadap setiap tahapan ETL.

---

# ETL Workflow

```
Website
    │
    ▼
Extract
(utils/extract.py)
    │
    ▼
Transform
(utils/transform.py)
    │
    ▼
Load
(utils/load.py)
    │
    ├── CSV
    ├── Google Sheets
    └── PostgreSQL
```

---

# Technologies

Beberapa teknologi utama yang digunakan pada proyek ini antara lain:

| Technology            | Purpose                          |
| --------------------- | -------------------------------- |
| Python                | Bahasa pemrograman utama         |
| Requests              | Mengambil halaman website        |
| BeautifulSoup4        | Parsing HTML                     |
| Pandas                | Manipulasi dan transformasi data |
| SQLAlchemy            | Koneksi ke PostgreSQL            |
| psycopg2              | PostgreSQL Driver                |
| Google Sheets API     | Penyimpanan ke Google Sheets     |
| gspread               | Integrasi Google Sheets          |
| pytest                | Unit Testing                     |
| coverage / pytest-cov | Test Coverage                    |

---

# Project Structure

```text
ETL-Pipeline
│
├── tests
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── utils
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── products.csv
├── google-sheets-api.json
├── requirements.txt
└── submission.txt
```

---

# Pipeline Description

## 1. Extract

Tahapan ekstraksi dilakukan pada modul:

```
utils/extract.py
```

Fitur utama:

* scraping data dari website target
* mengambil seluruh halaman (1–50)
* mengambil atribut produk:

  * Title
  * Price
  * Rating
  * Colors
  * Size
  * Gender
* menambahkan timestamp proses ekstraksi
* menerapkan error handling pada proses scraping

---

## 2. Transform

Tahapan transformasi dilakukan pada:

```
utils/transform.py
```

Proses transformasi meliputi:

* menghapus data invalid
* menghapus nilai null
* menghapus data duplikat
* konversi harga Dollar ke Rupiah
* konversi Rating menjadi float
* konversi Colors menjadi integer
* membersihkan kolom Size
* membersihkan kolom Gender
* menghasilkan DataFrame yang siap digunakan

---

## 3. Load

Tahapan loading dilakukan pada:

```
utils/load.py
```

Hasil transformasi dapat disimpan ke:

* CSV
* Google Sheets
* PostgreSQL

Setiap metode penyimpanan memiliki mekanisme error handling sehingga kegagalan penyimpanan dapat ditangani tanpa menghentikan keseluruhan pipeline.

---

# Data Output

Dataset hasil transformasi memiliki atribut berikut:

| Column    | Description            |
| --------- | ---------------------- |
| Title     | Nama produk            |
| Price     | Harga dalam Rupiah     |
| Rating    | Rating produk          |
| Colors    | Jumlah variasi warna   |
| Size      | Ukuran produk          |
| Gender    | Target pengguna        |
| timestamp | Waktu proses ekstraksi |

---

# Installation

Clone repository:

```bash
git clone <repository-url>
cd ETL-Pipeline
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

# Configuration

Sebelum menjalankan pipeline, pastikan:

* PostgreSQL telah aktif.
* Database `etl_db` telah dibuat.
* File `google-sheets-api.json` tersedia pada root project.
* Google Sheets telah dibagikan kepada Service Account yang digunakan.

---

# Running the Project

Jalankan pipeline menggunakan:

```bash
python main.py
```

Pipeline akan menjalankan proses berikut secara otomatis:

1. Extract data dari website.
2. Transform data.
3. Menyimpan hasil ke:

   * CSV
   * Google Sheets
   * PostgreSQL

---

# Unit Testing

Seluruh pengujian disimpan pada folder:

```text
tests/
```

Modul yang diuji:

* Extract
* Transform
* Load

Menjalankan seluruh pengujian:

```bash
pytest
```

Menampilkan test coverage:

```bash
pytest --cov=utils tests/
```

---

# Error Handling

Pipeline menerapkan mekanisme penanganan kesalahan pada setiap tahapan utama.

Contoh penanganan meliputi:

* kegagalan koneksi website
* kesalahan parsing HTML
* kesalahan transformasi data
* kegagalan penyimpanan CSV
* kegagalan koneksi Google Sheets
* kegagalan penyimpanan PostgreSQL

Pendekatan ini membuat pipeline tetap lebih stabil ketika terjadi kondisi yang tidak diharapkan.

---

# Key Features

* Modular ETL Pipeline
* Web Scraping Automation
* Data Cleaning
* Currency Conversion (USD → IDR)
* Multi Repository Storage
* Timestamp Recording
* Unit Testing
* Error Handling
* Clean Project Structure

---

# Future Improvements

Beberapa pengembangan yang dapat dilakukan di masa mendatang:

* menggunakan logging dibandingkan `print()`
* menambahkan konfigurasi melalui file `.env`
* meningkatkan test coverage dengan mocking
* otomatisasi pipeline menggunakan scheduler
* integrasi dengan cloud storage atau data warehouse

---

# Author

**Ahmad Latif**

Industrial Engineering Student

Universitas Islam Negeri Sunan Kalijaga

---

# License

Repository ini dibuat untuk tujuan pembelajaran dan penyelesaian submission Dicoding. Seluruh data yang digunakan tetap mengikuti ketentuan dan sumber penyedia dataset.
