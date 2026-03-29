# Tugas 3 - Coding: Python Basics

# 1. Deklarasi Variabel dan Tipe Data
nama_program = "Belajar Python AI"          # String
batch_ke = 10                               # Integer
rating_kesulitan = 4.5                      # Float
apakah_seru = True                          # Boolean
daftar_bahasa = ["Python", "C++", "Java"]   # List

print("--- 1. Variabel & Tipe Data ---")
print(f"Program: {nama_program}, Tipe: {type(nama_program)}")
print(f"Batch: {batch_ke}, Tipe: {type(batch_ke)}")
print(f"Rating: {rating_kesulitan}, Tipe: {type(rating_kesulitan)}")
print(f"Seru: {apakah_seru}, Tipe: {type(apakah_seru)}")
print(f"Daftar: {daftar_bahasa}, Tipe: {type(daftar_bahasa)}\n")

# 2. Manipulasi String
print("--- 2. Manipulasi String ---")
teks_sambutan = "Selamat Datang di Infinite Learning"
print("Teks Asli:", teks_sambutan)
print("Huruf Besar:", teks_sambutan.upper())
print("Huruf Kecil:", teks_sambutan.lower())
print("Panjang Karakter:", len(teks_sambutan))
print("Gabung String:", teks_sambutan + " Batch " + str(batch_ke) + "!")
print()

# 3. Operasi Matematika Sederhana
print("--- 3. Operasi Matematika ---")
a = 15
b = 4
print(f"Angka: a={a}, b={b}")
print("Penjumlahan (a + b):", a + b)
print("Pengurangan (a - b):", a - b)
print("Perkalian (a * b):", a * b)
print("Pembagian (a / b):", a / b)
print("Pembagian Bulat (a // b):", a // b)
print("Sisa Bagi/Modulo (a % b):", a % b)
print()

# 4. List dan Akses Elemen
print("--- 4. List & Manipulasi List ---")
hero_valorant = ["Jett", "Sage", "Omen", "Phoenix", "Reyna"]
print("List Awal:", hero_valorant)
print("Akses Elemen Kedua (Index 1):", hero_valorant[1])

# Tambah item
hero_valorant.append("Cypher")
print("Setelah Append (Tambah Cypher):", hero_valorant)

# Hapus item
hero_valorant.remove("Phoenix")
print("Setelah Remove (Hapus Phoenix):", hero_valorant)
print()

# 5. Penggunaan Input dari User
print("--- 5. Input User ---")
input_nama = input("Masukkan nama Anda: ")
input_umur = input("Masukkan umur Anda: ")

print(f"Halo, nama saya {input_nama} dan umur saya {input_umur} tahun.")
