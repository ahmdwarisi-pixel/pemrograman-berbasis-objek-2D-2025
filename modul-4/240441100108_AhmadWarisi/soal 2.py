class Buku:
    def __init__(self, judul, penulis, halaman):
        self.judul = judul
        self._penulis = penulis
        self.__halaman = halaman

    def get_penulis(self):
        return self._penulis

    def set_penulis(self, penulis):
        self._penulis = penulis

    def get_halaman(self):
        return self.__halaman

    def set_halaman(self, jumlah):
        self.__halaman = jumlah

    def info(self):
        print(f"Judul: {self.judul}, Penulis: {self._penulis}, Halaman: {self.__halaman}")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self):
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Nama Penulis: ")
        halaman = int(input("Masukkan Jumlah Halaman: "))
        self.daftar_buku.append(Buku(judul, penulis, halaman))

    def tampilkan_buku(self):
        print("\nDaftar Buku di Perpustakaan:")
        for buku in self.daftar_buku:
            buku.info()


def main_perpustakaan():
    perpus = Perpustakaan()
    while True:
        print("\n1. Tambah Buku\n2. Tampilkan Semua Buku\n3. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            perpus.tambah_buku()
        elif pilih == "2":
            perpus.tampilkan_buku()
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid.")

main_perpustakaan()