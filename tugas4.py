# ==========================================
# Tugas 4 - Coding: Python Data Structures
# Nama File: tugas4.py
# ==========================================

# 1. List – Akses & Manipulasi
print("--- 1. List: Akses & Manipulasi ---")
campuran = ["Python", 2026, "AI", 3.14, True, "Infinite"]
print(f"List Awal: {campuran}")
print(f"Elemen Pertama: {campuran[0]}, Terakhir: {campuran[-1]}")
print(f"Slicing [1:5:2]: {campuran[1:5:2]}")

# Manipulasi
campuran.append("Batam")
campuran.insert(2, "Learning")
campuran.extend([100, 200])
print(f"Setelah Append, Insert, Extend: {campuran}")

campuran.pop()
campuran.remove(3.14)
print(f"Setelah Pop & Remove (3.14): {campuran}\n")


# 2. Tuple – Immutability & Unpacking
print("--- 2. Tuple: Unpacking ---")
data_tuple = ("Valorant", "CSGO", "Dota2", "Apex", "Roblox")
print(f"Panjang Tuple: {len(data_tuple)}")
print(f"Indeks ke-2: {data_tuple[2]}")

# Unpacking
game1, game2, *sisanya = data_tuple
print(f"Unpacked -> g1: {game1}, g2: {game2}, rest: {sisanya}\n")


# 3. Set – Keunikan & Operasi Himpunan
print("--- 3. Set: Operasi Himpunan ---")
set_a = {1, 2, 3, 4, 5, 5, 5} # Cek duplikat otomatis hilang
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a} (Duplikat 5 hilang)")
print(f"Set B: {set_b}")

print(f"Union (|): {set_a | set_b}")
print(f"Intersection (&): {set_a & set_b}")
print(f"Difference (-): {set_a - set_b}")
print(f"Symmetric Difference (^): {set_a ^ set_b}\n")


# 4. Dictionary – Key/Value Dasar
print("--- 4. Dictionary: Data Mahasiswa ---")
mhs = {
    "nama": "Jonathan",
    "nim": "123456",
    "angkatan": 2024,
    "kota": "Batam"
}
mhs["prodi"] = "AI Development" # Tambah key
mhs["angkatan"] = 2025          # Ubah nilai
del mhs["kota"]                 # Hapus key

print(f"Keys: {list(mhs.keys())}")
print(f"Values: {list(mhs.values())}")
print("Iterasi Key: Value ->")
for k, v in mhs.items():
    print(f"  {k}: {v}")
print()


# 5. Nested Structures
print("--- 5. Nested Structures: Daftar Buku ---")
perpustakaan = [
    {"judul": "Python Crash Course", "penulis": "Eric Matthes", "tahun": 2019},
    {"judul": "Clean Code", "penulis": "Robert Cecil", "tahun": 2008},
    {"judul": "Automate Boring Stuff", "penulis": "Al Sweigart", "tahun": 2020},
    {"judul": "Deep Learning", "penulis": "Ian Goodfellow", "tahun": 2016}
]

print("Semua Judul Buku:")
for buku in perpustakaan:
    print(f"- {buku['judul']}")

# Filter buku >= 2018 menggunakan List Comprehension
buku_baru = [b['judul'] for b in perpustakaan if b['tahun'] >= 2018]
print(f"Buku Terbit >= 2018: {buku_baru}\n")


# 6. Comprehension & Utilitas
print("--- 6. Comprehension ---")
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]
print(f"List Genap: {genap}")
print(f"List Kuadrat (1-20): {kuadrat[:5]}...") # Tampilkan 5 saja

# Dict Comprehension 1-10
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print(f"Mapping Genap/Ganjil: {mapping}")

# Set Comprehension: Huruf unik lowercase
kalimat = "Infinite Learning AI"
huruf_unik = {h.lower() for h in kalimat if h.isalpha()}
print(f"Huruf Unik dari kalimat: {huruf_unik}\n")


# 7. Keanggotaan & Pencarian Sederhana
print("--- 7. Membership & Search ---")
cari = "AI"
if cari in campuran:
    print(f"'{cari}' ditemukan di list 'campuran' pada indeks ke-{campuran.index(cari)}")

cari_angka = 10
status = "ada" if cari_angka in set_a else "tidak ada"
print(f"Angka {cari_angka} {status} di dalam set_a.")
