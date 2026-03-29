# ==========================================
# Tugas 5 - Coding: Python Function and Class
# ==========================================

# --- FUNCTIONS ---

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Mengembalikan rata-rata (2 angka di belakang koma)."""
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)


# --- CLASS STUDENT ---

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float):
        """Menambah satu nilai ke list."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Rata-rata nilai menggunakan function rata_rata() di atas."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Menentukan status kelulusan berdasarkan threshold."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        """Representasi string dari objek Student."""
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


# --- DEMO ---

if __name__ == "__main__":
    # Demo Functions
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"Tambah (5 + 7): {tambah(5, 7)}")
    print(f"Tambah (10 + default): {tambah(10)}")
    print(f"Rata-rata [80, 90, 100]: {rata_rata([80, 90, 100])}")
    print(f"Rata-rata list kosong: {rata_rata([])}")
    print()

    # Demo Class Student
    print("=== CLASS STUDENT ===")
    
    # Mahasiswa 1
    mhs1 = Student("Jonathan", "B10-001")
    mhs1.tambah_nilai(85.0)
    mhs1.tambah_nilai(90.5)
    mhs1.tambah_nilai(78.0)
    print(mhs1) # Memanggil __str__
    print(f"Detail: Rata-rata {mhs1.rata_nilai()}, Status: {mhs1.status()}")
    print()

    # Mahasiswa 2
    mhs2 = Student("Budi", "B10-002")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)
    print(mhs2) # Memanggil __str__
    print(f"Detail: Rata-rata {mhs2.rata_nilai()}, Status: {mhs2.status()}")
