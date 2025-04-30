class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Seluruh Karyawan:")
        for karyawan in self.daftar_karyawan:
            karyawan.info()
            print('-------------------')

# Program utama
manajemen = ManajemenKaryawan()

while True:
    print("Tambah Karyawan")
    tipe = input("Jenis karyawan (Tetap/Harian)? (ketik 'selesai' untuk keluar): ")

    if tipe == "selesai":
        break

    nama = input("Masukkan nama: ")
    gaji = int(input("Masukkan gaji: "))
    departemen = input("Masukkan departemen: ")

    if tipe == "tetap":
        tunjangan = int(input("Masukkan tunjangan: "))
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif tipe == "harian":
        jam_kerja = int(input("Masukkan jam kerja per hari: "))
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
    else:
        print("Tipe karyawan tidak dikenali!")
        continue

    manajemen.tambah_karyawan(karyawan)

manajemen.tampilkan_semua_karyawan()