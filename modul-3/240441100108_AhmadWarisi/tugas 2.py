class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  # estimasi default


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan.lower() == 'motor':
            return 6
        elif self.jenis_kendaraan.lower() == 'mobil':
            return 4
        else:
            return 5


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == 'garuda':
            return 2
        elif self.maskapai.lower() == 'lion':
            return 3
        else:
            return 4


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        waktu = min(waktu_darat, waktu_udara)
        if self.tujuan.lower() != 'indonesia':
            waktu += 3
        return waktu


while True:
    print("--- Kalkulator Estimasi Waktu Pengiriman ---")
    asal = input("Masukkan kota/negara asal: ")
    tujuan = input("Masukkan kota/negara tujuan: ")
    jenis_pengiriman = input("Jenis pengiriman (darat/udara/internasional): ").lower()

    if jenis_pengiriman == 'darat':
        jenis_kendaraan = input("Jenis kendaraan (motor/mobil): ")
        pengiriman = PengirimanDarat(asal, tujuan, jenis_kendaraan)
        print("Estimasi waktu pengiriman darat:", pengiriman.estimasi_waktu(), "hari")
    elif jenis_pengiriman == 'udara':
        maskapai = input("Nama maskapai: ")
        pengiriman = PengirimanUdara(asal, tujuan, maskapai)
        print("Estimasi waktu pengiriman udara:", pengiriman.estimasi_waktu(), "hari")
    elif jenis_pengiriman == 'internasional':
        jenis_kendaraan = input("Jenis kendaraan untuk pengiriman darat (motor/mobil): ")
        maskapai = input("Nama maskapai untuk pengiriman udara: ")
        pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)
        print("Estimasi waktu pengiriman internasional:", pengiriman.estimasi_waktu(), "hari")
    else:
        print("Jenis pengiriman tidak valid.")

    ulangi = input("Hitung estimasi lagi? (ya/tidak): ").lower()
    if ulangi != 'ya':
        break

print("Terima kasih!")