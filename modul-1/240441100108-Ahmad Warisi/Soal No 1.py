#Tugas No 1
class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

# Membuat 5 objek dari class Manusia
manusia1 = Manusia("Andi", 20, "Jakarta")
manusia2 = Manusia("Budi", 25, "Bandung")
manusia3 = Manusia("Citra", 22, "Surabaya")
manusia4 = Manusia("Dewi", 24, "Yogyakarta")
manusia5 = Manusia("Eko", 21, "Malang")

# Memanggil method berjalan dan berlari
manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()