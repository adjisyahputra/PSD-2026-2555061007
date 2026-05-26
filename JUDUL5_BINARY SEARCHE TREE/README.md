
TUGAS AKHIR JUDUL 5

NAMA: DIMAS ADJI SYAHPUTRA

NPM: 2555061007

JUDUL: PROGRAM LEADERBOARD UNTUK DATA NILAI MAHASISWA

Program ini merupakan penggunaan impelementasi sistem Leaderboard kelas mata kuliah yang menggunakan struktur data Binary Search Tree untuk menyimpan dan mengurutkan data mahasiswa berdasarkan nilai.
Setiap mahasiswa direpresentasikan sebagai node yang berisi nama dan nilai. Node dengan nilai lebih kecil ditempatkan di subtree kiri, sedangkan nilai lebih besar di subtree kanan.
Dengan cara ini, data tersusun secara terstruktur sehingga proses pencarian, penambahan, dan pengurutan nilai menjadi efisien.


<img width="1632" height="4396" alt="JUDUL 5 CODE EE" src="https://github.com/user-attachments/assets/119d550a-3337-43c7-9531-9cc6c9e8f317" />


Mendefinisikan class Node sebagai struktur dasar simpul BST.

Konstruktor __init__ untuk inisialisasi node baru.

Menyimpan nama mahasiswa ke atribut nama.

Menyimpan nilai mahasiswa ke atribut nilai.

Inisialisasi anak kiri node dengan None (kosong).

Inisialisasi anak kanan node dengan None (kosong).

Mendefinisikan class LeaderboardMahasiswa untuk mengelola BST.

Konstruktor class BST.

Inisialisasi root tree dengan None (pohon kosong).

Mendefinisikan fungsi insert_node untuk menambahkan node baru.

Mengecek apakah posisi root kosong.

Jika kosong, buat node baru.

Mengecek apakah nilai lebih kecil dari root.

Jika lebih kecil, masukkan ke subtree kiri.

Mengecek apakah nilai lebih besar dari root.

Jika lebih besar, masukkan ke subtree kanan.

Mengembalikan node root setelah update.

Baris kosong pemisah fungsi.

Mendefinisikan fungsi insert sebagai pembungkus.

Memanggil insert_node mulai dari root.

Mendefinisikan fungsi inorder untuk traversal.

Mengecek apakah node kosong.

Jika kosong, hentikan rekursi.

Rekursi ke subtree kanan (nilai besar dulu).

Menampilkan nama dan nilai mahasiswa.

Rekursi ke subtree kiri (nilai kecil).

Mendefinisikan fungsi find_max.

Mengecek apakah tree kosong.

Jika kosong, return None.

Mulai pencarian dari root.

Bergerak ke kanan selama masih ada node kanan.

Pindah ke node kanan berikutnya.

Mengembalikan nama dan nilai mahasiswa tertinggi.

Mendefinisikan fungsi find_min.

Mengecek apakah tree kosong.

Jika kosong, return None.

Mulai pencarian dari root.

Bergerak ke kiri selama masih ada node kiri.

Pindah ke node kiri berikutnya.

Mengembalikan nama dan nilai mahasiswa terendah.

Mendefinisikan fungsi sum_nilai.

Mengecek apakah node kosong.

Jika kosong, return 0.

Menjumlahkan nilai root + subtree kiri + subtree kanan.

Baris kosong pemisah fungsi.

Mendefinisikan fungsi count_mahasiswa.

Mengecek apakah node kosong.

Jika kosong, return 0.

Menghitung jumlah node: 1 + anak kiri + anak kanan.

Mendefinisikan fungsi main.

Membuat objek leaderboard mahasiswa.

Inisialisasi variabel pilih dengan 0.

Loop menu utama selama pilih != 6.

Menampilkan judul menu.

Menampilkan pilihan menu 1.

Menampilkan pilihan menu 2.

Menampilkan pilihan menu 3.

Menampilkan pilihan menu 4.

Menampilkan pilihan menu 5.

Menampilkan pilihan menu 6.

Memulai blok try untuk validasi input.

Meminta input angka dari pengguna.

Menangkap error jika input bukan angka.

Menampilkan pesan error input tidak valid.

Mengulang loop jika input salah.

Lanjut ke iterasi berikutnya.

Mengecek apakah pilihan = 1.

Meminta input nama mahasiswa.

Memulai blok try untuk nilai.

Meminta input nilai mahasiswa.

Memasukkan data mahasiswa ke BST.

Menampilkan pesan konfirmasi data berhasil ditambahkan.

Menangkap error jika nilai bukan angka.

Mengecek apakah pilihan = 2.

Menampilkan judul leaderboard.

Menampilkan leaderboard dengan traversal inorder.

Mengecek apakah pilihan = 3.

Mencari mahasiswa dengan nilai tertinggi.

Mencari mahasiswa dengan nilai terendah.

Menampilkan mahasiswa dengan nilai tertinggi.

Menampilkan mahasiswa dengan nilai terendah.

Mengecek apakah pilihan = 4.

Menampilkan jumlah mahasiswa.

Mengecek apakah pilihan = 5.

Menghitung total nilai mahasiswa.

Menghitung jumlah mahasiswa.

Menghitung rata-rata nilai.

Menampilkan rata-rata nilai.

Mengecek apakah pilihan = 6.

Menampilkan pesan keluar program.

Jika input tidak sesuai menu.

Menampilkan pesan pilihan tidak valid.

Mengecek apakah file dijalankan langsung.

Jika iya, jalankan fungsi main().

output:

<img width="274" height="499" alt="Screenshot 2026-05-26 224759" src="https://github.com/user-attachments/assets/2d9e10e5-a5bc-4460-9fc7-3cbecf1723a9" />

<img width="435" height="812" alt="Screenshot 2026-05-26 224805" src="https://github.com/user-attachments/assets/0771d5f0-60e3-474b-bf3a-765bcf79ed3e" />

<img width="483" height="796" alt="Screenshot 2026-05-26 224817" src="https://github.com/user-attachments/assets/68166644-e831-459c-a2c3-b790c9b7607a" />

<img width="1828" height="570" alt="Screenshot 2026-05-26 224832" src="https://github.com/user-attachments/assets/748d566e-37c1-4f8c-a123-0d1b856e11a9" />

<img width="347" height="425" alt="Screenshot 2026-05-26 224838" src="https://github.com/user-attachments/assets/514409bc-f1a5-4e52-b3ae-a38308499432" />

Link youtube: https://www.youtube.com/watch?v=Ozic_ZX96Pk&t=3s




