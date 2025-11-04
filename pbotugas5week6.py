class Nasabah:
    def __init__(self, nama, no_rek, saldo_awal, poin_reward):
        self.nama = nama
        self.no_rek = no_rek
        self.__saldo_awal = saldo_awal
        self._poin_reward = poin_reward

    def tampilkan_info(self):
        print("==Informasi Nasabah==")
        print(f"Nama :{self.nama}")
        print(f"Nomor Rekening :{self.no_rek}")
        print(f"Saldo :Rp{self.__saldo_awal}")
        print(f"Poin Reward :{self._poin_reward}")
        print("="*21)
        return self
    
    def cek_saldo(self):
        print(f"Saldo anda saat ini sebesar: Rp{self.__saldo_awal}")

    def menabung(self, tabungan):
        if tabungan <= 0:
            print("==Anda Belum Ada Saldo==")
            return self
        
        cashback = tabungan * 0.01
        self.__saldo_awal += (tabungan + cashback)

        waktu_transaksi = datetime.datetime.now()
        self._histori_transaksi("Menabung", tabungan, waktu_transaksi)
        self._histori_transaksi("cashback", cashback, waktu_transaksi)

        print(f"Menabung Rp{tabungan:,.} berhasil. Anda mendapatkan Cashback sebesar Rp{cashback:,.}.")
        self.cek_saldo()

    def 

    def belanja(self, belanjaan):
        if belanjaan <= 0:
            print("==Anda Belum Belanja==")