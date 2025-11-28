class Hewan:
    def suara(self):
        print("Ini suara hewam")
class Anjing(Hewan):
    def suara(self):
        print("Guk Guk")
class Kucing(Hewan):
    def suara(self):
        print("Rawrr")
class Sapi(Hewan):
    def suara(self):
        print("Moo Moo")

for hewan in (Anjing(), Kucing(), Sapi()):
    hewan.suara()