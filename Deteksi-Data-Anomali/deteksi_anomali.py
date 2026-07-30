
# Data mentah putar lagu yang diperbanyak (Sekarang 15 Data)
data_streaming = [
    {"user": "Faiz", "judul_lagu": "Sial - Mahalini", "menit_putar": 3.5, "device": "Mobile"},
    {"user": "Akun_Bot99", "judul_lagu": "Komang - Raim Laode", "menit_putar": 0.05, "device": "Emulator"},
    {"user": "Yazid", "judul_lagu": "Kopi Dangdut", "menit_putar": 4.2, "device": "Desktop"},
    {"user": "Akun_Z", "judul_lagu": "Glimpse of Us", "menit_putar": -2.0, "device": "Mobile"},
    {"user": "Diki", "judul_lagu": "Janji Setia", "menit_putar": 3.8, "device": "Mobile"},
    {"user": "Bot_Music_V2", "judul_lagu": "Tak Ingin Usai", "menit_putar": 0.01, "device": "Desktop"},
    {"user": "Rafif", "judul_lagu": "Penjaga Hati", "menit_putar": 4.0, "device": "Desktop"},
    {"user": "Spam_Account", "judul_lagu": "Rayuan Perempuan Gila", "menit_putar": 2.5, "device": "Emulator"},
    {"user": "Selpanaw", "judul_lagu": "Jiwa Yang Bersedih", "menit_putar": 3.2, "device": "Mobile"},
    {"user": "Error_User", "judul_lagu": "Bad Liar", "menit_putar": -0.5, "device": "Desktop"},
    {"user": "Naufal", "judul_lagu": "Secukupnya - Hindia", "menit_putar": 3.1, "device": "Mobile"},
    {"user": "Bot_Flex", "judul_lagu": "Sial - Mahalini", "menit_putar": 0.02, "device": "SmartTV"},
    {"user": "Fajar", "judul_lagu": "Evaluasi - Hindia", "menit_putar": 4.5, "device": "Desktop"},
    {"user": "Spam_Bot_v3", "judul_lagu": "Komang - Raim Laode", "menit_putar": 1.2, "device": "Emulator"},
    {"user": "Unknown_Device", "judul_lagu": "Lantas", "menit_putar": -1.5, "device": "Tablet"}
]

# --1. buat fungsi untuk mendeteksi akun robot
def deteksi_bot(data):
  akun_bot = []
  for item in data:
    if item['menit_putar'] <=0.1 or item['device'] == "Emulator":
      akun_bot.append(item)
  return akun_bot

# --2. buat fungsi unttuk filter data yang clean
def filter_clean(data):
  data_clean =[]
  for item in data:
    if item['menit_putar'] >=0.1 and item['device'] !="Emulator":
      data_clean.append(item)
  return data_clean


print("==================================================================")
print("         LAPORAN ANALISIS DETEKSI BOT MUSIC STREAMING SPAM                  ")
print("==================================================================\n")


hasil_deteksi = deteksi_bot(data_streaming)
print("⚠️ [DETEKSI AKUN BOT] Menemukan akun mencurigakan:")
for akun in hasil_deteksi:
    print(f"User : {akun['user']} | Judul Lagu: {akun['judul_lagu']} | Menit Putar: {akun['menit_putar']} | Device: {akun['device']}")
    print("-"*30)


data_clean = filter_clean(data_streaming)
print("\n✅ [CLEAN DATA] Data Sukses & Valid:")
for akun in data_clean:
    print(f"User : {akun['user']} | Judul Lagu: {akun['judul_lagu']} | Menit Putar: {akun['menit_putar']} | Device: {akun['device']}")
    print("-"*30)


#-- 3. kesimpulan
total_menit = sum(akun['menit_putar'] for akun in data_clean)
jumlah_pendengar = len(data_clean)

print("\n================ KESIMPULAN ==============")
print(f"🎵 Total Pendengar Valid: {jumlah_pendengar} Akun")
print(f"⏳ Total Menit Putar Bersih: {total_menit} Menit")
print(f"🤖 Akun Robot Berhasil Diblokir: {len(hasil_deteksi)} Akun")
print("===========================================")



