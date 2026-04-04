data_laptop=[
    {"nama": "Asus Vivobook", "ram": 8, "harga": 7500000},
    {"nama": "Acer Swift", "ram": 16, "harga": 9500000},
    {"nama": "Lenovo Ideapad", "ram": 4, "harga": 5500000},
    {"nama": "Macbook Air", "ram": 8, "harga": 13500000},
    {"nama": "Advan Heritage", "ram": 16, "harga": 6500000},
    {"nama": "Lenovo Yoga Slim 7i", "ram": 16, "harga": 15000000}
    ]



def stok_laptop(daftar):
   for laptop in daftar:
     print(f"laptop: {laptop['nama']} | Ram {laptop['ram']} | harga: {laptop['harga']:,}")

#fungsi mencari laptop yang termurah dan termahal
def termurah_termahal(daftar_laptop):
  laptop_termurah=daftar_laptop[0]
  laptop_termahal=daftar_laptop[0]
  for laptop in daftar_laptop:
    if laptop['harga'] > laptop_termahal['harga']:
      laptop_termahal = laptop
    elif laptop['harga'] < laptop_termurah['harga']:
      laptop_termurah = laptop
  return laptop_termahal, laptop_termurah

#fungsi untuk memfilter berbasarkan budget dan ram
def filter_budget_ram(daftar_laptop, uang, ram):
  hasil_pencarian=[]

  for laptop in daftar_laptop:
    if laptop['harga'] < uang and laptop['ram'] >= ram:
      hasil_pencarian.append(laptop)
  return hasil_pencarian


print("-"*40)
print("=== SELAMAT DATANG DI LAPTOP STORE ===")
print("-"*40)
print("1. Lihat Laptop Termurah dan Laptop Termahal")
print("2. Cari Berdasarkan Budget dan Ram")
print("3. Stok Laptop Tersedia")

while True:
    pilihan=input("\nMasukan Pilihan Anda (ketik stop untuk berherti): ")

    if pilihan=="stop".lower():
       print("Terimakasih sudah mengunjungi Laptop Store")
       break

    if pilihan =="1":
        laptop_termahal, laptop_termurah = termurah_termahal(data_laptop)
        print(f"\nLaptop termahal: {laptop_termahal['nama']} dengan harga Rp {laptop_termahal['harga']:,}")
        print(f"Laptop termurah: {laptop_termurah['nama']} dengan harga Rp {laptop_termurah['harga']:,}")

    elif pilihan =="2":
        uang=int(input("Masukan minimal uang: "))
        ram=int(input("Masukan minimal ram: "))
        
        hasil=filter_budget_ram(data_laptop, uang, ram)
        if hasil:
            print(f"\n--- Ditemukan {len(hasil)} laptop sesuai budget ---")
            for lp in hasil:
                print(f"{lp['nama']} dengan harga Rp {lp['harga']:,}")
        else:
            print("Pilihan tidak tersedia")

    elif pilihan =="3":
       print(f"--- Stok Laptop Tersedia ---")
       stok_laptop(data_laptop)

    else:
        print("Pilihan tidak valid.")


