**DETEKSI DATA ANOMALI STREAMING🎶**

langkah langkah dalam menyelesaikan Studi kasus ini sangat sederhana disini saya menggunakan 3 langkah diantaranya:
1. Mendekteksi Akun Bot
2. Filter data Bersih
3. Kesimpulan

1. Mendeteksi Akun Bot ini menggunakan fungtion (detekksi_bot) yang didalamnya menggunakan operasi logika or untuk menangkap kecurangan. Ciri cirinya
   "Jika Durasi putar <=0.1 menit atau menggunakan device emulator" => Jika salah satu syarat terpenuhi maka akun ditandai sebagai Bot

2. Filtering data bersih menggunakan fungtion juga (filter_clean), disini menggunakan logika AND dengan ciri ciri:
   "Jika menit putar harus >=0.1 dan device bukan emulator => Data yang minus maka otomatis terbuang karena syarat durasinya positif

3. Kesimpulan nya total pendengar valid ada 7 akun, total menit putar bersih 26.3 menit dan ang terakhir akun bot yang berasil diblokir ada 8 akun.
