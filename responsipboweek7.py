class Tiket:
    def __init__(self, nama_event, harga, stok):
        self.nama_event = nama_event
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Event: {self.nama_event}, Harga: Rp{self.harga}, Stok: {self.stok}")

    def hitung_total(self, jumlah):
        return jumlah * self.harga

    def beli(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pembelian harus > 0")
        if jumlah > self.stok:
            raise ValueError("Stok tidak cukup")

        total = self.hitung_total(jumlah)
        self.stok -= jumlah
        return total


class TiketKonser(Tiket):
    def __init__(self, nama_event, harga, stok, kategori):
        super().__init__(nama_event, harga, stok)
        self.kategori = kategori

    def hitung_total(self, jumlah):
        total = super().hitung_total(jumlah)
        diskon = 0

        if self.kategori == "VIP" and total > 2000000:
            diskon = 0.15 * total
        elif self.kategori == "Reguler" and total > 1000000:
            diskon = 0.10 * total

        return total - diskon


class TiketBioskop(Tiket):
    def __init__(self, nama_event, harga, stok, studio):
        super().__init__(nama_event, harga, stok)
        self.studio = studio

    def hitung_total(self, jumlah):
        total = super().hitung_total(jumlah)
        if jumlah > 3:
            total -= total * 0.05
        return total


class TiketWisata(Tiket):
    def __init__(self, nama_event, harga, stok, lokasi):
        super().__init__(nama_event, harga, stok)
        self.lokasi = lokasi

    def hitung_total(self, jumlah):
        total = super().hitung_total(jumlah)
        if total > 500000:
            total -= total * 0.08
        return total
    
konser = TiketKonser("Dewa19", 1500000, 10, "VIP")
bioskop = TiketBioskop("Avengers", 80000, 20, "Studio 2")
wisata = TiketWisata("Jatim Park", 200000, 15, "Malang")

konser.tampilkan_info()
bioskop.tampilkan_info()
wisata.tampilkan_info()

print("\nSimulasi pembelian:")
print("Total bayar konser:", konser.hitung_total(2))
print("Total bayar bioskop:", bioskop.hitung_total(4))
print("Total bayar wisata :", wisata.hitung_total(3))
