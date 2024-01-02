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
        return max(0, tahun_tersisa)  # fungsi max untuk memastikan hasil tidak negatif

class Operator(PengawasRuangAngkasa):
    def __init__(self, nama, umur, job):
        super().__init__(nama, umur)
        self._job = job  

    def job(self):
        return self._job

    def mengatur_job(self, job):
        self._job = job

    def memantau_ruang_angkasa(self):
        print(f"{self.mendapatkan_nama()} sedang melakukan {self.job()}")

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

class AnakAstronot(Astronot):
    def __init__(self, nama, umur, warna_baju_luar, alat_ruang_angkasa):
        super().__init__(nama, umur, warna_baju_luar)
        self._alat_ruang_angkasa = alat_ruang_angkasa

    def get_alat_ruang_angkasa(self):
        return self._alat_ruang_angkasa

    def set_alat_ruang_angkasa(self, alat):
        self._alat_ruang_angkasa = alat

    def menghitung_tahun_hingga_pensiun(self):
        tahun_tersisa = 60 - self.mendapatkan_umur()
        return max(0, tahun_tersisa)

# Main
def buat_pengawas():
    nama_pengawas = input("Masukkan nama Pengawas Ruang Angkasa: ")
    umur_pengawas = int(input("Masukkan umur Pengawas Ruang Angkasa: "))
    return PengawasRuangAngkasa(nama_pengawas, umur_pengawas)

def buat_operator():
    nama_operator = input("Masukkan nama Operator: ")
    umur_operator = int(input("Masukkan umur Operator: "))
    job_operator = input("Masukkan pekerjaan Operator: ")
    return Operator(nama_operator, umur_operator, job_operator)

def buat_astronot():
    nama_astronot = input("Masukkan nama Astronot: ")
    umur_astronot = int(input("Masukkan umur Astronot: "))
    warna_baju_astronot = input("Masukkan warna baju luar Astronot: ")
    return Astronot(nama_astronot, umur_astronot, warna_baju_astronot)

def buat_anak_astronot():
    nama_anak_astronot = input("Masukkan nama Anak Astronot: ")
    umur_anak_astronot = int(input("Masukkan umur Anak Astronot: "))
    warna_baju_anak_astronot = input("Masukkan warna baju luar Anak Astronot: ")
    alat_ruang_anak_astronot = input("Masukkan alat ruang angkasa Anak Astronot: ")
    return AnakAstronot(nama_anak_astronot, umur_anak_astronot, warna_baju_anak_astronot, alat_ruang_anak_astronot)

def tampilkan_menu():
    print("Menu:")
    print("1. Buat Pengawas")
    print("2. Buat Operator")
    print("3. Buat Astronot")
    print("4. Buat Anak Astronot")
    print("5. Keluar")
    return int(input("Pilih menu (1-5): "))

# Perulangan menggunakan loop while
while True:
    pilihan = tampilkan_menu()

    if pilihan == 1:
        pengawas = buat_pengawas()
        pengawas.menjelajahi_ruang_angkasa()


    elif pilihan == 2:
        operator = buat_operator()
        operator.menjelajahi_ruang_angkasa()
        operator.mengatur_job('Pemantauan')
        operator.memantau_ruang_angkasa()

    elif pilihan == 3:
        astronot = buat_astronot()
        astronot.menjelajahi_ruang_angkasa()
        astronot.melakukan_spacewalk()

    elif pilihan == 4:
        anak_astronot = buat_anak_astronot()
        anak_astronot.menjelajahi_ruang_angkasa()
        print('Alat :', anak_astronot.get_alat_ruang_angkasa())
        anak_astronot.set_alat_ruang_angkasa("Sedang Memakai AeroPress")
        print(anak_astronot.get_alat_ruang_angkasa())

    elif pilihan == 5:
        print("Terima kasih! Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-5.")
