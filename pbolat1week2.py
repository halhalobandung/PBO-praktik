class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkaninfo(self):
        return f"Nama saya adalah {self.nama}, NPM saya adalah {self.nim}"


mahasiswa1 = Mahasiswa("Anta Rizqi Maulana", "5240411104")
print(mahasiswa1.nama)
print(mahasiswa1.nim)
print(mahasiswa1.tampilkaninfo()) 