# class Hewan:
#     def suara(self):
#         print("Ini suara hewam")
# class Anjing(Hewan):
#     def suara(self):
#         print("Guk Guk")
# class Kucing(Hewan):
#     def suara(self):
#         print("Rawrr")
# class Sapi(Hewan):
#     def suara(self):
#         print("Moo Moo")

# def buat_suara(hewan):
#     hewan.suara()

# buat_suara(Anjing())
# buat_suara(Kucing())
# buat_suara(Sapi())

# for hewan in (Anjing(), Kucing(), Sapi()):
#     hewan.suara()

# class Math:
#     def tambah(self, *args):
#         total = 0
#         for i in args:
#             total += i
#         return total

# m = Math()
# print(m.tambah(1, 2, 3, 4, 5))
# print(m.tambah(10, 20))
# print(m.tambah(7, 14, 21))

class Kendaraan:
    def suara(self):
        print("Ini suara kendaraan")
class Motor(Kendaraan):
    def suara(self):
        print("Brum Brum")
class Mobil(Kendaraan):
    def suara(self):
        print("Broom Broom")

suara = [Motor(), Mobil()]
for k in suara:
    k.suara()

def jalan(kendaraan):
    kendaraan.suara()

jalan(Motor())
jalan(Mobil())