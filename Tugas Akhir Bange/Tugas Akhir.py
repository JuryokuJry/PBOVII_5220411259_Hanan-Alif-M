import mysql.connector
"""
Hanan Alif M
5220411259
"""
# koneksi database
def create_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="5220411259"
    )
    return connection

def create_cursor(connection):
    return connection.cursor()

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

class PengawasRuangAngkasa:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def mendapatkan_nama(self):
        return self._nama

    def mendapatkan_umur(self):
        return self._umur

    def menjelajahi_ruang_angkasa(self):
        print(f"{self._nama} sedang menjelajahi ruang angkasa!")

    def menghitung_tahun_hingga_pensiun(self):
        tahun_tersisa = 65 - self._umur
        return max(0, tahun_tersisa)

class Astronot(PengawasRuangAngkasa):
    def __init__(self, nama, umur, warna_baju_luar):
        super().__init__(nama, umur)
        self.__warna_baju_luar = warna_baju_luar

    def mengatur_warna_baju_luar(self, warna):
        self.__warna_baju_luar = warna

    def menjelajahi_ruang_angkasa(self):
        print(f"{self.mendapatkan_nama()} sedang melakukan spacewalk dengan baju luar berwarna {self.__warna_baju_luar}.")

    def melakukan_spacewalk(self):
        print(f"{self.mendapatkan_nama()} sedang melakukan spacewalk.")

    def menghitung_tahun_hingga_pensiun(self):
        tahun_tersisa = 60 - self.mendapatkan_umur()
        return max(0, tahun_tersisa)

# Main
def buat_pengawas():
    nama_pengawas = input("Masukkan nama Pengawas Ruang Angkasa: ")
    umur_pengawas = int(input("Masukkan umur Pengawas Ruang Angkasa: "))
    return PengawasRuangAngkasa(nama_pengawas, umur_pengawas)

def buat_astronot():
    nama_astronot = input("Masukkan nama Astronot: ")
    umur_astronot = int(input("Masukkan umur Astronot: "))
    warna_baju_astronot = input("Masukkan warna baju luar Astronot: ")
    return Astronot(nama_astronot, umur_astronot, warna_baju_astronot)

def isi_data():
    jenis_data = input("Pilih jenis data (1. Pengawas, 2. Astronot): ")
    connection = create_db_connection()
    cursor = create_cursor(connection)

    if jenis_data == "1":
        pengawas = buat_pengawas()
        pengawas.menjelajahi_ruang_angkasa()

        insert_query = "INSERT INTO pengawas (nama, umur) VALUES (%s, %s)"
        cursor.execute(insert_query, (
            pengawas.mendapatkan_nama(),
            pengawas.mendapatkan_umur()
        ))

    elif jenis_data == "2":
        astronot = buat_astronot()
        astronot.menjelajahi_ruang_angkasa()
        astronot.melakukan_spacewalk()

        insert_query = "INSERT INTO astronot (nama, umur, warna_baju_luar) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (
            astronot.mendapatkan_nama(),
            astronot.mendapatkan_umur(),
            astronot._Astronot__warna_baju_luar
        ))

    else:
        print("Jenis data tidak valid.")

    connection.commit()
    print("Data berhasil disimpan ke database")

    close_connection(connection, cursor)

def ubah_data():
    jenis_data = input("Pilih jenis data yang ingin diubah (1. Pengawas, 2. Astronot): ")
    connection = create_db_connection()
    cursor = create_cursor(connection)

    if jenis_data == "1":
        display_data("pengawas")
        nama_pengawas = input("Masukkan Nama Pengawas yang ingin diubah: ")
        umur_baru = int(input("Masukkan umur baru: "))
        update_query = "UPDATE pengawas SET umur=%s WHERE nama=%s"
        cursor.execute(update_query, (umur_baru, nama_pengawas))

    elif jenis_data == "2":
        display_data("astronot")
        nama_astronot = input("Masukkan Nama Astronot yang ingin diubah: ")
        warna_baju_baru = input("Masukkan warna baju luar baru: ")
        update_query = "UPDATE astronot SET warna_baju_luar=%s WHERE nama=%s"
        cursor.execute(update_query, (warna_baju_baru, nama_astronot))

    else:
        print("Jenis data tidak valid.")

    connection.commit()
    print("Data berhasil diubah")

    close_connection(connection, cursor)

def hapus_data():
    jenis_data = input("Pilih jenis data yang ingin dihapus (1. Pengawas, 2. Astronot): ")
    connection = create_db_connection()
    cursor = create_cursor(connection)

    if jenis_data == "1":
        display_data("pengawas")
        nama_pengawas = input("Masukkan Nama Pengawas yang ingin dihapus: ")
        delete_query = "DELETE FROM pengawas WHERE nama=%s"
        cursor.execute(delete_query, (nama_pengawas,))

    elif jenis_data == "2":
        display_data("astronot")
        nama_astronot = input("Masukkan Nama Astronot yang ingin dihapus: ")
        delete_query = "DELETE FROM astronot WHERE nama=%s"
        cursor.execute(delete_query, (nama_astronot,))

    else:
        print("Jenis data tidak valid.")

    connection.commit()
    print("Data berhasil dihapus")

    close_connection(connection, cursor)

def display_data(table_name):
    connection = create_db_connection()
    cursor = create_cursor(connection)

    select_query = f"SELECT * FROM {table_name}"
    cursor.execute(select_query)
    results = cursor.fetchall()

    print(f"Data pada tabel {table_name}:")
    for row in results:
        print(row)

    close_connection(connection, cursor)

def tampilkan_menu():
    print("Menu:")
    print("1. Isi Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Pengawas")
    print("5. Tampilkan Astronot")
    print("6. Keluar")
    return int(input("Pilih menu (1-6): "))

while True:
    pilihan = tampilkan_menu()

    if pilihan == 1:
        isi_data()

    elif pilihan == 2:
        ubah_data()

    elif pilihan == 3:
        hapus_data()

    elif pilihan == 4:
        display_data("pengawas")

    elif pilihan == 5:
        display_data("astronot")

    elif pilihan == 6:
        print("Terima kasih! Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-6.")
