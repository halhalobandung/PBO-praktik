class Mahasiswa:
    def __init__(self, nama, npm, nilai):
        self.nama = nama
        self._npm = npm
        self.__nilai = nilai

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NPM: {self._npm}, Nilai: {self.__nilai}"