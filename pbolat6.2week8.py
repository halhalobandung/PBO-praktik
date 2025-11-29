class Employee:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    def bonus(self):
        # bonus = ()
        # print("Gaji pokok" (gaji_pokok))
        # for gaji_pokok in kali:
        return self.gaji_pokok * 0.05

class Programmer(Employee):
    def __init__(self, nama, jumlah_project):
        super().__init__(nama, 8000000)
        self.jumlah_project = jumlah_project
    def bonus(self):
        # bonus = ()
        # jum_proj = ()
        # print("Gaji pokok" (gaji_pokok))
        # for gaji_pokok in kali:
        return (0.1 * self.gaji_pokok) + (self.jumlah_project * 50000)
    
class Designer(Employee):
    def __init__(self, nama, jumlah_desain):
        super().__init__(nama, 7000000)
        self.jumlah_desain = jumlah_desain
    def bonus(self):
        # bonus = ()
        # jum_des = ()
        # print("Gaji pokok" (gaji_pokok))
        # for gaji_pokok in kali:
        return (0.08 * self.gaji_pokok) + (self.jumlah_desain * 30000)
    
class Intern(Employee):
    def __init__(self, nama, jumlah_tugas):
        super().__init__(nama, 2000000)
        self.jumlah_tugas = jumlah_tugas
    def bonus(self):
        # bonus = ()
        # jum_tgs = ()
        # print("Gaji pokok" (gaji_pokok))
        # for gaji_pokok in kali:
        return (0.02 * self.gaji_pokok) + (self.jumlah_tugas * 10000)

def hitung_bonus_semua(karyawan_list):
    for k in karyawan_list:
        print(f"{k.nama} | Jabatan: {k.__class__.__name__}")
        print(f"Gaji Pokok : Rp {k.gaji_pokok:,}".replace(",", ","))
        print(f"Bonus : Rp {int(k.bonus()):,}".replace(",", ","))
        print("-" * 45)

karyawan = [
    Employee ("Andi", 5000000),
    Programmer ("Budi", 2),
    Designer ("Cici", 3),
    Intern ("Dana", 4)
]

hitung_bonus_semua(karyawan)

# def buat_gaji(Employee):
#     Employee.bonus()

# buat_gaji(Employee(5000000))
