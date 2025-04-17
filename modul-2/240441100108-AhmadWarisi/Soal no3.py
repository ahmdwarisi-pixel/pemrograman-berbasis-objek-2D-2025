class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if Kampus.validasi_nama_kampus(nama):
            self.nama = nama
            self.alamat = alamat
            Kampus.jumlah_mahasiswa = 0
        else:
            print(f"[Peringatan] Nama kampus tidak valid: {nama}")
            self.nama = "NAMA INVALID"
            self.alamat = alamat

    @classmethod
    def info_kampus(cls, kampus_obj):
        print(f"Nama Kampus     : {kampus_obj.nama}")
        print(f"Alamat Kampus   : {kampus_obj.alamat}")
        print(f"Total Mahasiswa : {cls.jumlah_mahasiswa}")
        print("=" * 40)

    @staticmethod
    def validasi_nama_kampus(nama):
        for char in nama:
            if char.isdigit():
                return False
        return True
    
#Membuat objek Kampus  
kampus1 = Kampus("Universitas Trunojoyo Madura", "Jl. Telang no. 1, Kamal, Bangkalan")
Kampus.jumlah_mahasiswa = 1000
Kampus.info_kampus(kampus1)

# Membuat objek Kampus dengan nama tidak valid
kampus2 = Kampus("Kampus 123", "Jl. Salah Nama Kampus")
Kampus.info_kampus(kampus2)
