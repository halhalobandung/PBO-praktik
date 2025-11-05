from datetime import datetime

class Nasabah:

    no_rek = ""

    def __init__(self, nama, no_rek, saldo_awal):
        self._nama = nama
        self.no_rek = no_rek
        self.__saldo_awal = saldo_awal
        self.__poin_reward = 0
        self.__riwayat_transaksi = []

        self.__log(f"Buka Rekening | saldo awal Rp {saldo_awal}")

    def get_saldo(self):
        #print(f"Saldo anda saat ini sebesar: Rp{self.__saldo_awal}")
        return self.__saldo_awal
    
    def set_saldo(self, value):
        self.__saldo_awal = value

    def get_poin(self):
        #print(f"Poin Reward Anda: {self.__poin_reward} poin")
        return self.__poin_reward
    
    def set_poin(self, value):
        self.__poin_reward = value

    def __log(self, teks):
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.__riwayat_transaksi.append(f"[{waktu}] {teks}")

    def menabung(self, tabungan):
        if tabungan <= 0:
            print("==Anda Belum Ada Saldo==")
            return self
        
        cashback = tabungan * 0.01
        saldo_baru = self.get_saldo() + tabungan + cashback
        self.set_saldo(saldo_baru)
        print(f"Menabung Rp{tabungan:,} berhasil. Anda mendapatkan Cashback sebesar Rp{cashback:,}.")
        self.__log(f"Menabung Rp{tabungan:,} | cashback RP{cashback:,}")
        #self.cek_saldo()

    def belanja(self, belanjaan):
        if belanjaan <= 0:
            print("==Anda Belum Belanja==")
            return self
        
        if self.get_saldo() >= belanjaan:
            saldo_baru = self.get_saldo() - belanjaan
            self.set_saldo(saldo_baru)

            poinreward = belanjaan // 10000
            self.__poin_reward += poinreward
            self.__log(f"Belanja Rp{belanjaan:,} | Mendapatkan {poinreward} poin")

            # print(f"Belanja sebesar Rp{belanjaan:,.} berhasil.")
            # if poinreward > 0:
            #     print(f"Selamat! Anda mendapatkan {poinreward} Poin Reward.")
            # self.cek_saldo()
        else:
            print("Saldo Anda Tidak Mencukupi.")
            self.cek_saldo()

    def poin_redeem(self, jumlah_poin):
        list_hadiah = {
                100: "Voucher Belanja Rp50.000",
                200: "Saldo Rp100.000",
                500: "Smartwatch BCN Edition"
        }

        if jumlah_poin not in list_hadiah:
            print("Pilihan hadiah tidak tersedia!")
            return
        
        if self.get_poin() < jumlah_poin:
            print("Poin anda tidak mencukupi untuk redeem!")
            return
        
        self.set_poin(self.get_poin() - jumlah_poin)

        if jumlah_poin == 200:
            self.set_saldo(self.get_saldo() + 100000)

        self.__log(f"REDEEM {list_hadiah[jumlah_poin]} | Potong poin {jumlah_poin}")

    def tampilkan_info(self):
        print("="*50)
        print("Informasi Nasabah")
        print("="*50)
        print(f"Nama            :{self._nama}")
        print(f"Nomor Rekening  :{self.no_rek}")
        print(f"Saldo           :Rp {self.get_saldo():,}")
        print(f"Poin Reward     :{self.get_poin()}")
        print("="*50)

    def generate_riwayat_transaksi(self):
        print("\n== DETAIL TRANSAKSI BANK CERDAS NUSANTARA ==")
        print(f"Nasabah : {self._nama}")
        print("-"*50)
        for i, r in enumerate(self.__riwayat_transaksi, start=1):
            print(f"{i}. {r}")
        print("="*50)
        print(f"Saldo Akhir : Rp {self.get_saldo():,}")
        print(f"Poin Akhir : {self.get_poin()}")
        print("="*50)

nasabah1 = Nasabah("Anta Rizqi Maulana", "1234567890", 0)

nasabah1.menabung(10_000_000)

nasabah1.belanja(2_500_000)
nasabah1.belanja(3_200_000)
nasabah1.belanja(1_300_000)

nasabah1.menabung(3_000_000)

nasabah1.poin_redeem(200)

nasabah1.tampilkan_info()
nasabah1.generate_riwayat_transaksi()