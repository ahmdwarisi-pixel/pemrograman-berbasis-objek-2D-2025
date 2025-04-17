class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            print(f"[Peringatan] NIM tidak valid: {nim}")
            self.nim = nim
        else:
            self.nim = nim
        self.nama = nama
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
        if self.mata_kuliah:
            for matkul in self.mata_kuliah:
                print(f"- {matkul}")
        else:
            print("  Belum ada mata kuliah yang diambil.")
        print("=" * 30)

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah mahasiswa yang telah dibuat: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10

# Membuat minimal 6 object
m1 = Mahasiswa("Warisi", "2312345678", "Informatika")
m2 = Mahasiswa("Fadil", "2300000001", "Sistem Informasi")
m3 = Mahasiswa("Richo", "2311111122", "Teknik Komputer")
m4 = Mahasiswa("Razin", "2301234567", "Informatika")
m5 = Mahasiswa("Udin", "2309876543", "Sistem Informasi")
m6 = Mahasiswa("Fajar", "2310000010", "Teknik Komputer")

# Menambahkan mata kuliah
m1.tambah_matkul("Pemrograman Dasar")
m1.tambah_matkul("Matematika Diskrit")
m1.tambah_matkul("Algoritma")
m1.tambah_matkul("Struktur Data")

m2.tambah_matkul("Sistem Basis Data")
m2.tambah_matkul("Analisis dan Desain Sistem")
m2.tambah_matkul("Jaringan Komputer")
m2.tambah_matkul("Kalkulus")

m3.tambah_matkul("Jaringan Komputer")
m3.tambah_matkul("Sistem Operasi")
m3.tambah_matkul("Rekayasa Perangkat Lunak")
m3.tambah_matkul("Kalkulus")

m4.tambah_matkul("Kalkulus")
m4.tambah_matkul("Logika Informatika")
m4.tambah_matkul("Pemrograman Berbasis Web")
m4.tambah_matkul("Basis Data")

m5.tambah_matkul("Etika Profesi")
m5.tambah_matkul("Manajemen Proyek TI")
m5.tambah_matkul("Analisis dan Desain Sistem")
m5.tambah_matkul("Kalkulus")

m6.tambah_matkul("Algoritma dan Struktur Data")
m6.tambah_matkul("Statistika")
m6.tambah_matkul("Rekayasa Perangkat Lunak")
m6.tambah_matkul("Sistem Operasi")

# Tampilkan info masing-masing mahasiswa
for m in [m1, m2, m3, m4, m5, m6]:
    m.tampilkan_info()

# Tampilkan jumlah total mahasiswa
Mahasiswa.tampilkan_jumlah_mahasiswa()

# Contoh pembuatan objek dengan NIM tidak valid
m7 = Mahasiswa("Galih", "22123456", "Manajemen")
m7.tampilkan_info()