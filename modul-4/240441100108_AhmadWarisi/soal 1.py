class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self._no_rek = no_rek
        self.nama = nama
        self.__saldo = saldo

    def get_no_rek(self):
        return self._no_rek

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, jumlah):
        self.__saldo = jumlah

    def setor(self, jumlah):
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup!")

    def tampil(self):
        print(f"Rekening: {self._no_rek} | Nama: {self.nama} | Saldo: Rp{self.__saldo}")


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self):
        no_rek = input("Masukkan No Rekening: ")
        nama = input("Masukkan Nama Pemilik: ")
        saldo = float(input("Masukkan Saldo Awal: "))
        self.rekening_list.append(RekeningBank(no_rek, nama, saldo))

    def setor_uang(self):
        no_rek = input("Masukkan No Rekening: ")
        jumlah = float(input("Jumlah Setoran: "))
        for rek in self.rekening_list:
            if rek.get_no_rek() == no_rek:
                rek.setor(jumlah)
                print("Setoran berhasil.")
                return
        print("Rekening tidak ditemukan.")

    def tarik_uang(self):
        no_rek = input("Masukkan No Rekening: ")
        jumlah = float(input("Jumlah Penarikan: "))
        for rek in self.rekening_list:
            if rek.get_no_rek() == no_rek:
                rek.tarik(jumlah)
                return
        print("Rekening tidak ditemukan.")

    def tampil_semua(self):
        for rek in self.rekening_list:
            rek.tampil()

def main_bank():
    bank = Bank()
    while True:
        print("\n1. Tambah Rekening\n2. Setor\n3. Tarik\n4. Tampilkan Semua\n5. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            bank.tambah_rekening()
        elif pilih == "2":
            bank.setor_uang()
        elif pilih == "3":
            bank.tarik_uang()
        elif pilih == "4":
            bank.tampil_semua()
        elif pilih == "5":
            break
        else:
            print("Menu tidak valid.")
            
main_bank()