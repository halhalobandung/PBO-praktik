class Dosen:
    def __init__(self, nama, nidn, gaji):
        self.nama = nama
        self._nidn = nidn
        self.__gaji = gaji

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NIDN {self._nidn}, Gaji: {self.__gaji}"
    
    def get_gaji(self):
        print(f"Gaji {self.nama} sebesar {self.__gaji}")
        return self.__gaji
    
    def set_gaji(self, gaji):
        self.__gaji = gaji
        return f"Gaji telah diganti"
    
Slamet = Dosen("Slamet Riyadi", "99995555", 5000000)
Agus = Dosen("Agus Hariyanto", "88887777", 3000000)

print(Slamet.tampilkan_data())
print(Agus.tampilkan_data())

print(Slamet.nama)              #public
print(Slamet._nidn)             #protected
# print(Slamet.__gaji)          #private
print(Slamet._Dosen__gaji)      #illegal_private_access

print("="*50)

Slamet.get_gaji()
print(Slamet.set_gaji(1000000))
Slamet.get_gaji()