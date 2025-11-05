class Nasabah:
    def __init__(self, nama, no_rek, saldo_awal):
        self._nama = nama
        self.no_rek = no_rek
        self.__saldo_awal = saldo_awal
        self.__poin_reward = 0
        self.__riwayat_transaksi = []
        self.__log(f"Open Account saldo awal: {saldo_awal}")

    def __log(self, text):
        self.__riwayat_transaksi(text)

    def menabung(self, tabungan):
        if tabungan <= 0:
            print("==Anda Belum Ada Saldo==")
            return self
        
        cashback = tabungan * 0.01
        self.__saldo_awal += tabungan + cashback
        print(f"Menabung Rp{tabungan:,.} berhasil. Anda mendapatkan Cashback sebesar Rp{cashback:,.}.")
        self.__log(f"Menabung Rp{tabungan:,} | cashback RP(cashback:,.)")
        self.cek_saldo()

    def belanja(self, belanjaan):
        if belanjaan <= 0:
            print("==Anda Belum Belanja==")
            return self
        
        if self.__saldo_awal >= belanjaan:
            self.__saldo_awal -= belanjaan
            poinreward = belanjaan // 10000
            self.__poin_reward += poinreward
            self.__log(f"Belanja Rp")

            # print(f"Belanja sebesar Rp{belanjaan:,.} berhasil.")
            # if poinreward > 0:
            #     print(f"Selamat! Anda mendapatkan {poinreward} Poin Reward.")
            # self.cek_saldo()
        else:
            print("Saldo Anda Tidak Mencukupi.")
            self.cek_saldo()

    def cek_saldo(self):
        print(f"Saldo anda saat ini sebesar: Rp{self.__saldo_awal}")

    def poin(self):
        print(f"Poin Reward Anda: {self.__poin_reward} poin")

    def poin_redeem(self, pilihan):
        list_hadiah = {
                1: {"nama": "Voucher Belanja Rp50.000", "poin": 100},
                2: {"nama": "Saldo Rp100.000", "poin": 200},
                3: {"nama": "Smartwatch BCN Edition", "poin": 500}
        }

        if pilihan not in list_hadiah:
            print("Pilihan Anda tidak valid")

        hadiah = list_hadiah[pilihan]
        poin_dibutuhkan = hadiah["poin"]
        if self._poin_reward >= poin_dibutuhkan:
            self._poin_reward -= poin_dibutuhkan
            print(f"Anda berhasil menukarkan {poin_dibutuhkan} poin denga {hadiah['nama']}!")
        else:
            print("Poin Anda Tidak cukup untuk menukarkan hadiah ini.")

    def tampilkan_info(self):
        print("==Informasi Nasabah==")
        print(f"Nama :{self.nama}")
        print(f"Nomor Rekening :{self.no_rek}")
        print(f"Saldo :Rp{self.__saldo_awal}")
        print(f"Poin Reward :{self._poin_reward}")
        print("="*21)
        return self        