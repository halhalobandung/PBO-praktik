import sqlite3

conn = sqlite3.connect("sewamotor.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS motor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    plat TEXT NOT NULL,
    harga_sewa INTEGER NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()

def tambah_motor(nama, plat, harga_sewa, status):
    cursor.execute("""
        INSERT INTO motor (nama, plat, harga_sewa, status)
        VALUES (?, ?, ?, ?)
    """, (nama, plat, harga_sewa, status))
    conn.commit()
    print("Motor berhasil ditambahkan!")

def tampilkan_motor():
    cursor.execute("SELECT * FROM motor")
    data = cursor.fetchall()

    if not data:
        print("Tdak ada data motor.")
        return
    
    print("\nDaftar Motor:")
    print("-" * 40)
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Nama: {row[1]}")
        print(f"Plat: {row[2]}")
        print(f"Harga Sewa: {row[3]}")
        print(f"Status: {row[4]}")
        print("-" * 40)

def update_motor(id_motor, nama_baru, plat_baru, harga_baru, status_baru):
    cursor.execute("""
        UPDATE motor
        SET nama = ?, plat = ?, harga_sewa = ?, status = ? 
        WHERE id = ?
    """, (nama_baru, plat_baru, harga_baru, status_baru, id_motor))
    conn.commit()
    print("Motor berhasil diperbarui!")

def hapus_motor(id_motor):
    cursor.execute("DELETE FROM motor WHERE id = ?", (id_motor,))
    conn.commit()
    print("Motor berhasil dihapus!")

def cari_motor(keyword):
    cursor.execute("SELECT * FROM motor WHERE nama LIKE ?", ("%" + keyword + "%",))
    data = cursor.fetchall()

    if not data:
        print("Motor tidak ditemukan.")
        return
    
    print("\nDaftar Motor:")
    print("-" * 40)
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Nama: {row[1]}")
        print(f"Plat: {row[2]}")
        print(f"Harga Sewa: {row[3]}")
        print(f"Status: {row[4]}")
        print("-" * 40)

def tampilkan_tersedia():
    cursor.execute("SELECT * FROM motor WHERE status = 'tersedia'")
    data = cursor.fetchall()

    if not data:
        print("Motor tidak ditemukan.")
        return
    
    print("\nDaftar Motor:")
    print("-" * 40)
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Nama: {row[1]}")
        print(f"Plat: {row[2]}")
        print(f"Harga Sewa: {row[3]}")
        print(f"Status: Tersedia")
        print("-" * 40)

def sewa_motor(id_motor):
    cursor.execute("SELECT * FROM motor WHERE id = ?", (id_motor,))
    data = cursor.fetchone()

    if not data:
        print("ID motor tidak ditemukan.")
        return

    if data[0] == "Dipinjam":
        print("Motor sedang dipinjam.")

    cursor.execute("UPDATE motor SET status = 'Dipinjam' WHERE id = ?", (id_motor,))
    conn.commit()
    print("Motor berhasil disewa!")

def kembalikan_motor(id_motor, hari):
    cursor.execute("SELECT harga_sewa FROM motor WHERE id = ?", (id_motor,))
    data = cursor.fetchone()

    if not data:
        print("ID motor tidak ditemukan.")
        return
    
    harga = data[0]
    total = harga * hari

    cursor.execute("UPDATE motor SET status = 'Tersedia' WHERE id = ?", (id_motor,))
    conn.commit()

    print("\n=== MOTOR DIKEMBALIKAN ===")
    print(f"Harga Sewa Perhari: {harga}")
    print(f"Lama Sewa: {hari} hari")
    print(f"Total biaya: Rp {total}")
    print("=" * 26)

def menu():
    while True:
        print("\n=== RENTAL MOTOR JOGJA ===")
        print("1. Tambah Motor")
        print("2. Tampilkan Semua Motor")
        print("3. Update Motor")
        print("4. Hapus Motor")
        print("5. Cari Motor")
        print("6. Tampilkan Motor Tersedia")
        print("7. Sewa Motor")
        print("8. Transaksi Sewa Motor")
        print("9. Keluar")

        pilihan = input("Pilih menu (1-9): ")

        if pilihan == "1":
            nama = input("Masukan nama motor: ")
            plat = input("Masukan plat motor: ")
            harga_sewa = int(input("Masukan harga sewa motor: "))
            status = input("Masukan status : ")
            tambah_motor(nama, plat, harga_sewa, status)
        elif pilihan == "2":
            tampilkan_motor()
        elif pilihan == "3":
            id_motor = int(input("Masukkan ID motor yang akan diupdate: "))
            plat_baru = str(input("Masukkan plat motor baru: "))
            nama_baru = str(input("Masukkan nama motor baru: "))
            harga_baru = int(input("Masukkan harga motor baru: "))
            status_baru = input("Masukkan status motor baru: ")
            update_motor(id_motor, plat_baru, nama_baru, harga_baru, status_baru)
        elif pilihan == "4":
            id_motor = int(input("Masukkan ID motor yang akan dihapus: "))
            hapus_motor(id_motor)
        elif pilihan == "5":
            keyword = input("\nMasukkan kata kunci nama motor: ")
            cari_motor(keyword)
        elif pilihan == "6":
            tampilkan_tersedia()
        elif pilihan == "7":
            id_motor = int(input("Masukkan ID motor yang akan disewa: "))
            sewa_motor(id_motor)
        elif pilihan == "8":
            id_motor = int(input("Masukkan ID motor yang akan dikembalikan: "))
            hari = int(input("Berapa hari disewa: "))
            kembalikan_motor(id_motor, hari)
        elif pilihan == "9":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

menu()
cursor.close()
conn.close()