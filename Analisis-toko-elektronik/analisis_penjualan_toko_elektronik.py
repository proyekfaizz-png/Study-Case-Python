import pandas as pd

data = [
    {"Produk": "Laptop", "Kota": "Bandung", "Kategori": "Elektronik", "Harga": 8000000, "Jumlah": 2, "Bulan": "Januari"},
    {"Produk": "Mouse", "Kota": "Bandung", "Kategori": "Aksesoris", "Harga": 150000, "Jumlah": 10, "Bulan": "Januari"},
    {"Produk": "Keyboard", "Kota": "Jakarta", "Kategori": "Aksesoris", "Harga": 300000, "Jumlah": 8, "Bulan": "Februari"},
    {"Produk": "Laptop", "Kota": "Jakarta", "Kategori": "Elektronik", "Harga": 8000000, "Jumlah": 1, "Bulan": "Februari"},
    {"Produk": "Monitor", "Kota": "Bandung", "Kategori": "Elektronik", "Harga": 2500000, "Jumlah": 4, "Bulan": "Maret"},
    {"Produk": "Mouse", "Kota": "Surabaya", "Kategori": "Aksesoris", "Harga": 150000, "Jumlah": 15, "Bulan": "Maret"},
    {"Produk": "Laptop", "Kota": "Surabaya", "Kategori": "Elektronik", "Harga": 8000000, "Jumlah": 3, "Bulan": "April"},
    {"Produk": "Keyboard", "Kota": "Bandung", "Kategori": "Aksesoris", "Harga": 300000, "Jumlah": 7, "Bulan": "April"},
    {"Produk": "Monitor", "Kota": "Jakarta", "Kategori": "Elektronik", "Harga": 2500000, "Jumlah": 2, "Bulan": "Mei"},
    {"Produk": "Mouse", "Kota": "Jakarta", "Kategori": "Aksesoris", "Harga": 150000, "Jumlah": 20, "Bulan": "Mei"}
]

df = pd.DataFrame(data)

# Menambah kolom Total Omzet
df["Total"] = df["Harga"] * df["Jumlah"]

print("=" * 50)
print("DATA PENJUALAN")
print("=" * 50)
print(df)

# ==========================
# Total Omzet Perusahaan
total_omzet = df["Total"].sum()

print("\nTotal Omzet Perusahaan")
print(f"Rp {total_omzet:,}")

# ==========================
# Omzet per Produk
omzet_produk = df.groupby("Produk")["Total"].sum().sort_values(ascending=False)

print("\nOmzet per Produk")
print(omzet_produk)

# ==========================
# Omzet per Kota
omzet_kota = df.groupby("Kota")["Total"].sum().sort_values(ascending=False)

print("\nOmzet per Kota")
print(omzet_kota)

# ==========================
# Omzet per Kategori
omzet_kategori = (df.groupby("Kategori")["Total"].sum().sort_values(ascending=False)
)

print("\nOmzet per Kategori")
print(omzet_kategori)

# ==========================
# Rata-rata Harga Produk
rata_harga = (df.groupby("Produk")["Harga"].mean().sort_values(ascending=False))

print("\nRata-rata Harga Produk")
print(rata_harga)

# ==========================
# Produk Terlaris Berdasarkan Omzet
produk_terbaik = omzet_produk.idxmax()
nilai_produk = omzet_produk.max()

print("\nProduk dengan Omzet Terbesar")
print(f"{produk_terbaik} : Rp {nilai_produk:,}")

# ==========================
# Kota Terbaik
kota_terbaik = omzet_kota.idxmax()
nilai_kota = omzet_kota.max()

print("\nKota dengan Omzet Terbesar")
print(f"{kota_terbaik} : Rp {nilai_kota:,}")

print("========================================")
print("           LAPORAN PENJUALAN    ")
print("========================================")

print("\nRingkasan")
print(f"Total Omzet {total_omzet:,}")
print(f"Produk Terbaik {produk_terbaik} : Rp {nilai_produk:,}")
print(f"Kota Terbaik {kota_terbaik} : Rp {nilai_kota:,}")

print("\n---------------------------------------")
print("Insight")
print(f"Total omzet perusahaan mencapai {total_omzet}")
print(f"Produk dengan omzet tertinggi adalah {produk_terbaik}")
print(f"Kategori dengan omzet tertinggi adalah {omzet_kategori.idxmax()}")
print(f"Kota dengan omzet tertinggi adalah {kota_terbaik}")

"""**LAPORAN HASIL ANALISIS**
1. Sebuah perusahaan mendapatkan omzet penjualan: Rp 74,250,000
2. Omzset Penjualan per produk tertinggi: Laptop Rp 48.000.000
3. Omzet Penjualan kota terlaris: Kota bandung
4. Kategori terlaris: Elektronik
5. rata rata harga produk: laptop 8000000

Rekomendasi Bisnis
1. Menambah stok laptop karena menyumbang omzet terbesar
2. Melakukan promosi pada keyboard karena  omzetnya paling rendah
3. memfokuskan pemasaran di kota bandung karena memberikan kontribusi omzet terbesar
"""