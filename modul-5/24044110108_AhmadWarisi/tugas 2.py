from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f"Tipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%\n")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        if self.energi_tersisa > 0:
            print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        if self.energi_tersisa == 0:
            print("Laptop tidak bisa digunakan karena energi 0.")
            return
        self.nyalakan()
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("Laptop digunakan. Baterai habis!")
        else:
            print(f"Laptop digunakan selama {jam} jam.")
        self.matikan()

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        if self.energi_tersisa == 0:
            print("Tidak bisa menyalakan kulkas. Energi habis!")
        else:
            print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        if self.energi_tersisa == 0:
            print("Kulkas tidak bisa digunakan karena energi 0.")
            return
        self.nyalakan()
        self.energi_tersisa -= 5 * jam
        print(f"Kulkas digunakan selama {jam} jam.")
        if self.energi_tersisa < 20 and self.energi_tersisa > 0:
            print("Energi rendah, kulkas butuh daya tambahan!")
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        self.matikan()


# Buat objek
laptop = Laptop()
kulkas = Kulkas()

while True:
    print("=== Menu Penggunaan Perangkat Elektronik ===")
    print("1. Gunakan Laptop")
    print("2. Gunakan Kulkas")
    print("3. Tampilkan Status")
    print("4. Keluar")
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        jam = int(input("Masukkan durasi penggunaan Laptop (jam): "))
        laptop.gunakan(jam)

    elif pilihan == "2":
        jam = int(input("Masukkan durasi penggunaan Kulkas (jam): "))
        kulkas.gunakan(jam)


    elif pilihan == "3":
        laptop.status()
        kulkas.status()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.\n")