# Wi-Fi Passwords Viewer

## Deskripsi
Wi-Fi Passwords Viewer adalah program Python yang memungkinkan Anda untuk menampilkan dan menyimpan semua password Wi-Fi yang tersimpan di laptop Anda. Program ini menggunakan modul `subprocess` untuk berinteraksi dengan perintah sistem operasi dan menghasilkan output yang rapi baik di konsol maupun dalam file teks.

## Fitur Utama
- Menampilkan nama jaringan Wi-Fi dan password mereka.
- Menyimpan hasil ke dalam file `wifi_passwords.txt`.
- Tampilan yang menarik dengan teks ASCII menggunakan modul `pyfiglet`.
- Warna yang menyenangkan berkat `colorama`.

## Prasyarat
Sebelum menjalankan program, pastikan Anda telah menginstal Python di sistem Anda. Anda juga perlu menginstal beberapa pustaka Python yang diperlukan. Berikut adalah langkah-langkah yang perlu diikuti:

### 1. Instal Python
- **Windows**: Unduh dan instal Python dari [python.org](https://www.python.org/downloads/).
- **Pastikan** untuk menambahkan Python ke PATH selama instalasi.

### 2. Instal Pustaka yang Diperlukan
Setelah Python terinstal, buka terminal atau command prompt dan jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

```bash
pip install pyfiglet colorama subprocess
