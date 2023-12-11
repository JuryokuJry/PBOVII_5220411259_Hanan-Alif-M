Nama      : Hanan Alif M
NPM       : 5220411259 
Kelompok  : 8

Anggota Lain  : 
Muhammad Jaohar Asbara (5220411241)
Febrian Aditiya        (5220411261)

Penjelasan Code:

Class Animal:
Merupakan class induk serta mewakili kelas dasar untuk semua hewan.
Memiliki atribut seperti nama, sifat, ukuran, dan jumlah kaki.
Memiliki metode tampil_info untuk menampilkan informasi umum tentang hewan.

Class Mamalia (Turunan dari Animal):
Mewakili hewan mamalia.
Menambahkan atribut seperti kemampuan jalan dan jenis mamalia.
Menggunakan metode tampil_info dari kelas Animal dan menambahkan informasi khusus mamalia.

Class Aves (Turunan dari Animal):
Mewakili hewan aves (burung).
Menambahkan atribut seperti kemampuan terbang dan jenis aves.
Menggunakan metode tampil_info dari kelas Animal dan menambahkan informasi khusus aves.

Class Ayam (Turunan dari Aves):
Mewakili jenis ayam yang merupakan turunan dari hewan aves.
Menambahkan atribut seperti jenis ayam dan kemampuan diadu.
Menggunakan metode tampil_info dari kelas Aves dan menambahkan informasi khusus ayam.

Class Merpati (Turunan dari Aves):
Mewakili jenis merpati yang merupakan turunan dari hewan aves.
Menggunakan metode tampil_info dari kelas Aves dan menambahkan informasi merpati

Objek:
Beberapa objek telah dibuat menggunakan kelas-kelas yang telah didefinisikan.
Setiap objek memiliki atribut dan metode sesuai dengan kelas induk dan turunannya.

Pemanggilan Metode tampil_info:
Setiap objek memanggil metode tampil_info untuk menampilkan informasi tentang hewan tersebut.
Pemanggilan metode ini menunjukkan konsep polimorfisme, di mana metode yang sama dipanggil dari objek-objek dengan tipe yang berbeda, dan masing-masing kelas turunan menyediakan implementasi sendiri.

Inheritance (Pewarisan):
Konsep pewarisan digunakan untuk mengorganisir dan mendefinisikan hubungan antara kelas-kelas.
Mamalia dan Aves mewarisi dari kelas Animal, dan Ayam serta Merpati mewarisi dari kelas Aves.
Pewarisan memungkinkan penggunaan kembali kode dan mengelompokkan sifat-sifat umum.
