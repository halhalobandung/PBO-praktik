class Akun:
    def __init__(self, saldo):
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor sebesar {jumlah}. Saldo sekarang: {self.saldo}.")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            self.saldo -= jumlah
            print(f"Tarik sebesar {jumlah}. Saldo sekarang: {self.saldo}.")

class AkunReward(Akun):
    def __init__(self, saldo, poin=0):
        super().__init__(saldo)
        self.poin = poin

    def setor(self, jumlah):
        if jumlah <= 1000:
            self.poin += 1
        elif 1001 <= jumlah <= 5000:
            self.poin += 5
        elif jumlah > 5000:
            self.poin += 10
        else:
            self.poin += 0
        self.saldo += jumlah
        print(f"Setor sebesar {jumlah}. Saldo sekarang: {self.saldo}. Poin sekarang: {self.poin}.")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            if jumlah <= 1000:
                self.poin += 1
            elif jumlah > 1000:
                self.poin += 5
            else:
                self.poin += 0
            self.saldo -= jumlah
            print(f"Tarik sebesar {jumlah}. Saldo sekarang: {self.saldo}. Poin sekarang {self.poin}.")

Slamet = Akun(1000)
Agus = AkunReward(2000)

# Slamet.setor(500)
# print(Slamet.saldo)

# Slamet.tarik(500)
# print(Slamet.saldo)

# print(Agus.saldo)
# Agus.setor(5000)

# Agus.tarik(1500)
# print(Agus.saldo)

def setor_overrideing(Akun):
    Akun.setor(5000)

setor_overrideing(Akun(3000))
setor_overrideing(AkunReward(5000))