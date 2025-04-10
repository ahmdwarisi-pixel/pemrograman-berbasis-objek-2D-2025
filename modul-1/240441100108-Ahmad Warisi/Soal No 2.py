#Tugas No 2
class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}, Alamat: {self.alamat}")

# Input data mahasiswa dan membuat objek
mahasiswa_list = []
for i in range(3):
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    prodi = input("Masukkan Prodi: ")
    alamat = input("Masukkan Alamat: ")
    mahasiswa = Mahasiswa(nama, nim, prodi, alamat)
    mahasiswa_list.append(mahasiswa)

# Menampilkan informasi mahasiswa
for mhs in mahasiswa_list:
    mhs.tampilkan_info()