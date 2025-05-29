from abc import ABC, abstractmethod

# Abstract class
class Manusia(ABC):

    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

# Subclass Joko
class Joko(Manusia):
    def berbicara(self):
        print("Joko berbicara dengan logat Jawa.")

    def bekerja(self):
        print("Joko bekerja sebagai petani.")

    def makan(self):
        print("Joko makan nasi pecel.")

# Subclass Beni
class Beni(Manusia):
    def berbicara(self):
        print("Beni berbicara dengan penuh semangat.")

    def bekerja(self):
        print("Beni bekerja sebagai programmer.")

    def makan(self):
        print("Beni makan mie instan.")

# Subclass Fani
class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara dengan suara lembut.")

    def bekerja(self):
        print("Fani bekerja sebagai guru.")

    def makan(self):
        print("Fani makan salad buah.")

# Subclass Jani
class Jani(Manusia):
    def berbicara(self):
        print("Jani berbicara dengan nada tegas.")

    def bekerja(self):
        print("Jani bekerja sebagai polisi.")

    def makan(self):
        print("Jani makan rendang.")

karakter_dict = {
    "joko": Joko(),
    "beni": Beni(),
    "fani": Fani(),
    "jani": Jani()
}

# Program utama
def main():
    while True:
        print("=== Program Interaksi Karakter ===")
        print("Pilih karakter (joko, beni, fani, jani) atau ketik 'keluar' untuk berhenti.")
        nama = input("Masukkan nama karakter: ").strip().lower()

        if nama == "keluar":
            print("Program dihentikan. Terima kasih!")
            break
        elif nama in karakter_dict:
            karakter = karakter_dict[nama]
            karakter.berbicara()
            karakter.bekerja()
            karakter.makan()
        else:
            print("Karakter tidak ditemukan. Coba lagi.")
main()