class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.nama = nama
        self._umur = umur
        self.__keluhan = keluhan

    def get_umur(self):
        return self._umur

    def set_umur(self, umur):
        self._umur = umur

    def get_keluhan(self):
        return self.__keluhan

    def set_keluhan(self, keluhan):
        self.__keluhan = keluhan

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self._umur}, Keluhan: {self.__keluhan}")


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self):
        nama = input("Masukkan Nama Pasien: ")
        umur = int(input("Masukkan Umur: "))
        keluhan = input("Masukkan Keluhan: ")
        self.daftar_pasien.append(Pasien(nama, umur, keluhan))

    def tampilkan_pasien(self):
        print("\nDaftar Pasien:")
        for pasien in self.daftar_pasien:
            pasien.tampilkan_info()


def main_klinik():
    klinik = Klinik()
    while True:
        print("\n1. Tambah Pasien\n2. Tampilkan Pasien\n3. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            klinik.tambah_pasien()
        elif pilih == "2":
            klinik.tampilkan_pasien()
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid.")
            
main_klinik()