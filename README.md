**Laptop Inventory & Recommendation System (Python CLI)**

**Deskripsi Project**

Aplikasi berbasis Command Line Interface (CLI) yang dirancang untuk membantu manajemen inventaris toko laptop sekaligus memberikan rekomendasi kepada pembeli berdasarkan budget dan kebutuhan spesifikasi (RAM). Project ini mendemonstrasikan penerapan struktur data List of Dictionaries serta algoritma Searching dan Filtering di Python.

**Fitur Utama**
1. Market Analytics: Mencari laptop dengan harga termurah dan termahal secara otomatis dalam satu kali iterasi.
2. Smart Filter: Membantu pelanggan mencari laptop yang sesuai dengan budget harga tertentu dan syarat minimal RAM.
3. Data Management: Menyimpan atribut produk (Nama, RAM, Harga) secara terstruktur.

**Konsep Struktur Data & Algoritma**

Dalam project ini, saya menerapkan beberapa konsep dasar Computer Science:
1. List of Dictionaries: Digunakan untuk menyimpan database laptop karena memudahkan akses atribut menggunakan key yang deskriptif.
2. Linear Search: Melakukan iterasi pada seluruh data untuk membandingkan nilai harga.
3. Conditional Logic: Menggunakan operator logika "and" untuk penyaringan ganda (Harga & RAM).
4. Modular Programming: Memisahkan logika bisnis ke dalam Functions agar kode dapat digunakan kembali.

**Cuplikan Kode (Highlight)**

1. Sistem Rekomendasi Lptop:

    <img width="370" height="140" alt="filter budget dan ram" src="https://github.com/user-attachments/assets/c18a66d0-c4b7-49f0-8dd2-96efb1426fc9" />

fungtion ini berfungsi untuk menyaring berbasarkan dua parameter (Uang/Budget dan RAM), Menggunakan condifional logic "and"  untuk menyaring data yang paling relevan bagi calon pembeli.

2. Analisis Harga
   
   <img width="351" height="163" alt="termahal dan termurah" src="https://github.com/user-attachments/assets/8700599b-821e-4263-b8d0-86ad200226e5" />

Fungsi ini membandingkan setiap elemen untuk menemukan nilai minimum dan maksimum dalam satu kali putaran loop.

3. Daftar Stok Laptop
   
   <img width="539" height="69" alt="image" src="https://github.com/user-attachments/assets/4ebd52f4-d118-4c2a-9816-dc7c0e49bd82" />

Menampilkan seluurh data laptop yang tersimpan dalam sistem. Menggunakan perulangan for untuk melakukan iterasi pada list of dictionaries dan menyajikannya secara rapi.

4. Loop Interaktif (While True)
   
   <img width="708" height="451" alt="image" src="https://github.com/user-attachments/assets/4a3b0251-1c21-45d7-baac-c9368ef58814" />

Seluruh sistem dibungkus dalam perulangan while true untuk menjaga aplikasi tetap berjalan. Program hanya akan berhenti jika penggunakan mengetik "Stop", yang memicu perintah break.

Kenapa harus menggunakan while true?
1. User Experience: Pengguna tidak perlu menjalankan ulang skrip setiap kali ingin mencoba menu yang berbeda.
2. State Manajement: Memungkinkan pengguna untuk melakukan pengecetak berkali kali dalam satu sesi yang sama.

**Demonstrasi Output:**

1. Menu Utama
   
   <img width="274" height="100" alt="image" src="https://github.com/user-attachments/assets/67260ae2-559c-4e75-82e4-f17edc331e75" />

3. Analisis Harga (termurah & Termahal)

   <img width="409" height="69" alt="image" src="https://github.com/user-attachments/assets/3ffd83b9-513e-4d63-af4b-b0b555e7a2cd" />

4. Rekomendasi Berdasarkan Budget & RAM

   <img width="386" height="127" alt="image" src="https://github.com/user-attachments/assets/df455680-819b-4104-81bf-1f01234cd30d" />

5. Menampilkan Seluruh Stok

   <img width="382" height="106" alt="image" src="https://github.com/user-attachments/assets/366285e0-edc3-46e7-b109-e77d44469b51" />





