import sqlite3

conn = sqlite3.connect("toko.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    harga INTEGER NOT NULL,
    stok INTEGER NOT NULL
)
""")

conn.commit()

def tambah_produk(nama, harga, stok):
    cursor.execute("""
        INSERT INTO produk (nama, harga, stok)
        VALUES (?, ?, ?)
    """, (nama, harga, stok))
    conn.commit()
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    cursor.execute("SELECT * FROM produk")
    data = cursor.fetchall()

    if not data:
        print("Tdak ada data produk.")
        return
    
    print("\nDaftar Produk:")
    print("-" * 40)
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Nama: {row[1]}")
        print(f"Harga: {row[2]}")
        print(f"Stok: {row[3]}")
        print("-" * 40)

def update_produk(id_produk, nama_baru, harga_baru, stok_baru):
    cursor.execute("""
        UPDATE produk
        SET nama = ?, harga = ?, stok = ?
        WHERE id = ?
    """, (nama_baru, harga_baru, stok_baru, id_produk))
    conn.commit()
    print("Produk berhasil diperbarui!")

def hapus_produk(id_produk):
    cursor.execute("DELETE FROM produk WHERE id = ?", (id_produk,))
    conn.commit()
    print("Produk berhasil dihapus!")

def menu():
    while True:
        print("\n=== Menu Manajemen Produk ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukan nama produk: ")
            harga = int(input("Masukan harga produk: "))
            stok = int(input("Masukan stok produk: "))
            tambah_produk(nama, harga, stok)
        elif pilihan == "2":
            tampilkan_produk()
        elif pilihan == "3":
            id_produk = int(input("Masukkan ID produk yang akan diupdate: "))
            nama_baru = str(input("Masukkan nama produk baru: "))
            harga_baru = int(input("Masukkan harga produk baru: "))
            stok_baru = int(input("Masukkan stok produk baru: "))
            update_produk(id_produk, nama_baru, harga_baru, stok_baru)
        elif pilihan == "4":
            id_produk = int(input("Masukkan ID produk yang akan dihapus: "))
            hapus_produk(id_produk)
        elif pilihan == "5":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

menu()
cursor.close()
conn.close()