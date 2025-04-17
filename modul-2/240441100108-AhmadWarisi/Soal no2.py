
class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.validasi_sks(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print(f"[Peringatan] SKS tidak valid: {sks}")
            self.kode = kode
            self.nama = nama
            self.sks = None

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

    def __str__(self):
        return f"{self.nama} ({self.kode}, {self.sks} SKS)" if self.sks is not None else f"{self.nama} ({self.kode}, SKS tidak valid)"


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.mata_kuliah = []
            Mahasiswa.jumlah_mahasiswa += 1
        else:
            print(f"[Peringatan] NIM tidak valid: {nim}")
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.mata_kuliah = []
            Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Prodi   : {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.mata_kuliah:
            print(f"- {mk}")
        print("=" * 40)

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah mahasiswa yang telah dibuat: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10


# Buat 8 mata kuliah
matkul1 = MataKuliah("IF101", "Pemrograman Berbasis Web", 3)
matkul2 = MataKuliah("IF102", "Logika Engenering", 2)
matkul3 = MataKuliah("IF103", "Pengantar Basis Data", 3)
matkul4 = MataKuliah("IF104", "Analisa Proses Bisnis", 3)
matkul5 = MataKuliah("IF105", "Desain Manageman Jaringan", 2)
matkul6 = MataKuliah("IF106", "Pemrograman Berbasis Objek", 3)
matkul7 = MataKuliah("IF107", "Statistika", 2)
matkul8 = MataKuliah("IF108", "Pengantar Teknologi Informasi Komputer", 2)

# Buat 6 mahasiswa
m1 = Mahasiswa("Warisi", "2312345678", "Informatika")
m2 = Mahasiswa("Fadil", "2300000001", "Sistem Informasi")
m3 = Mahasiswa("Yuricho", "2311111122", "Teknik Komputer")
m4 = Mahasiswa("Dhani", "2301234567", "Informatika")
m5 = Mahasiswa("Razin", "2309876543", "Sistem Informasi")
m6 = Mahasiswa("Fajar", "2310000010", "Teknik Komputer")

# Tambahkan minimal 4 matkul ke masing-masing mahasiswa
m1.tambah_matkul(matkul1)
m1.tambah_matkul(matkul2)
m1.tambah_matkul(matkul3)
m1.tambah_matkul(matkul4)

m2.tambah_matkul(matkul2)
m2.tambah_matkul(matkul5)
m2.tambah_matkul(matkul6)
m2.tambah_matkul(matkul8)

m3.tambah_matkul(matkul1)
m3.tambah_matkul(matkul3)
m3.tambah_matkul(matkul6)
m3.tambah_matkul(matkul7)

m4.tambah_matkul(matkul2)
m4.tambah_matkul(matkul4)
m4.tambah_matkul(matkul7)
m4.tambah_matkul(matkul8)

m5.tambah_matkul(matkul1)
m5.tambah_matkul(matkul5)
m5.tambah_matkul(matkul6)
m5.tambah_matkul(matkul8)

m6.tambah_matkul(matkul3)
m6.tambah_matkul(matkul4)
m6.tambah_matkul(matkul6)
m6.tambah_matkul(matkul7)

# Tampilkan info semua mahasiswa
for m in [m1, m2, m3, m4, m5, m6]:
    m.tampilkan_info()

# Tampilkan jumlah mahasiswa
Mahasiswa.tampilkan_jumlah_mahasiswa()

# Contoh pembuatan objek dengan data tidak valid
matkul_invalid_sks = MataKuliah("IF999", "Mata Kuliah Aneh", 1)
mahasiswa_invalid_nim = Mahasiswa("Bambang", "2212345678", "Ilmu Komputer")
mahasiswa_invalid_nim.tampilkan_info()