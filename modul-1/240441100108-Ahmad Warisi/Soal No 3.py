#Tugas No 3
# Class pertama: Kucing
class Kucing:
    def __init__(self, nama, umur, ras):
        self.nama = nama
        self.umur = umur
        self.ras = warna

    def bersuara(self):
        print(f"{self.nama} mengeong: Meong!")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan dengan lincah.")

# Class kedua: Burung
class Burung:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def bersuara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

# Class ketiga: Kambing
class Kambing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.jenis = warna

    def bersuara(self):
        print(f"{self.nama} mengembik: Mbeeekk!")

    def memakan_rumput(self):
        print(f"{self.nama} sedang memakan rumput di padang.")
# Data untuk masing-masing hewan
data_kucing = [("Mimi", 2, "putih"), ("Tom", 3, "kuning"), ("Leo", 1, "hitam")]
data_burung = [("Rio", 1, "Merah"), ("Kiki", 2, "Biru"), ("Lulu", 3, "Hijau")]
data_kambing = [("Mbek", 2, "putih"), ("Bleki", 3, "hitam"), ("kambing", 1, "hitam-putih")]

hewan_list = []
# Buat objek Kucing
for nama, umur, warna in data_kucing:
    kucing = Kucing(nama, umur, warna)
    hewan_list.append(kucing)

# Buat objek Burung
for nama, umur, warna in data_burung:
    burung = Burung(nama, umur, warna)
    hewan_list.append(burung)

# Buat objek Kambing
for nama, umur, warna in data_kambing:
    kambing = Kambing(nama, umur, warna)
    hewan_list.append(kambing)

# Panggil method dari semua objek
for hewan in hewan_list:
    hewan.bersuara()
