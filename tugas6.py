# ==========================================
# Tugas 6 - Python Modules, File I/O, & OOP
# ==========================================

import numpy as np
import pandas as pd
import os

# Set seed agar output konsisten (Opsional)
np.random.seed(42)

# --- NUMPY: DATA & STATISTIK ---
# Membuat 10 data nilai ujian acak antara 50 - 100
nilai_ujian = np.random.randint(50, 101, size=10)

def hitung_statistik(arr):
    stats = {
        "Rata-rata": np.mean(arr),
        "Median": np.median(arr),
        "Standar Deviasi": np.std(arr),
        "Min": np.min(arr),
        "Max": np.max(arr)
    }
    return stats

# --- PANDAS: DATAFRAME ---
data_mhs = {
    "nama": ["Jonathan", "Budi", "Sari", "Andi", "Lia"],
    "nim": ["B10-01", "B10-02", "B10-03", "B10-04", "B10-05"],
    "nilai": nilai_ujian[:5] # Mengambil 5 data pertama dari NumPy
}

df_mhs = pd.DataFrame(data_mhs)

# Menambahkan kolom status
df_mhs["status"] = df_mhs["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# --- OOP: GRADEBOOK ---
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Menghitung rata-rata kolom nilai."""
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase kelulusan."""
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return (lulus / len(self.df)) * 100

    def save_summary(self, path: str):
        """Menulis ringkasan ke file .txt."""
        stats = hitung_statistik(self.df["nilai"].values)
        jml_lulus = len(self.df[self.df["status"] == "LULUS"])
        jml_tidak = len(self.df[self.df["status"] == "TIDAK LULUS"])

        with open(path, "w") as f:
            f.write("=== RINGKASAN TUGAS 6 ===\n")
            f.write(f"Jumlah Data: {len(self.df)}\n")
            for k, v in stats.items():
                f.write(f"{k}: {v:.2 f}\n")
            f.write("-" * 25 + "\n")
            f.write(f"LULUS: {jml_lulus}\n")
            f.write(f"TIDAK LULUS: {jml_tidak}\n")
            f.write(f"Pass Rate: {self.pass_rate():.2 f}%\n")

    def __str__(self) -> str:
        return f"GradeBook(Data={len(self.df)}, Rata-rata={self.average():.2 f})"


# --- DEMO ---
if __name__ == "__main__":
    # 1. NumPy Section
    print("=== NUMPY ===")
    s = hitung_statistik(nilai_ujian)
    for k, v in s.items():
        print(f"{k}: {v:.2 f}")
    print()

    # 2. Pandas Section
    print("=== PANDAS ===")
    print(df_mhs.head())
    print()

    # 3. OOP Section
    print("=== OOP: GRADEBOOK ===")
    book = GradeBook(df_mhs)
    print(book)
    print(f"Rata-rata Kelas: {book.average():.2 f}")
    print(f"Tingkat Kelulusan: {book.pass_rate()}%")
    
    # Simpan ke File
    filename = "ringkasan_tugas6.txt"
    book.save_summary(filename)
    print(f"\nRingkasan telah disimpan ke {filename}")
