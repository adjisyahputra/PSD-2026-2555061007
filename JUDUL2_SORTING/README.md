Tugas Akhir Praktikum Struktur Data 2
Mama: DIMAS ADJI SYAHPUTRA
NPM: 2555061007
KELAS: PSD C

Judul Program: Bagaimana Mengurutkan Absen Mahasiswa Sesuai Dengan Abjad?

Program sederhana ini membantu kita untuk mempermudah menemukan absen mahasiswa yang berantakan, ketika basen tidak terurut tentu kita kesulitan untuk menemukan nama kita kita terletak di posisi bagian mana. Ketika absen sudah terurut, tentu ini akan mempermudah kita menemukan nama kita tanpa harus mencari dan membaca nama dari awal hingga akhir, hanya perlu mencari letak abjad kita kemudian mencarinya. Fungsi yang digunakan adalah bubble short yang membandingkan dua nama yang berdekatan lalu apabila tidak sesuai dengan posisinya maka ditukar.

<img width="1264" height="1736" alt="psd 2" src="https://github.com/user-attachments/assets/26c71928-a6bd-4896-b4a9-63be82426b4e" />
1. Mendefinisikan fungsi bernama tukar yang digunakan untuk menukar posisi dua elemen dalam array berdasarkan indeks.
2. Menyimpan sementara nilai elemen pada indeks i ke dalam variabel temp agar tidak hilang saat proses penukaran.
3. Mengisi posisi indeks i dengan nilai dari indeks j.
4. Mengisi posisi indeks j dengan nilai yang sebelumnya disimpan di temp, sehingga kedua elemen berhasil ditukar.
5. -
6. -
7. Mendefinisikan fungsi bubble_sort yang bertugas mengurutkan isi array menggunakan metode Bubble Sort.
8. Melakukan perulangan luar sebanyak n - 1 kali, karena dalam Bubble Sort maksimal diperlukan n-1 tahap untuk memastikan semua data terurut.
9. Melakukan perulangan dalam untuk membandingkan elemen yang bersebelahan dari awal hingga bagian yang belum terurut.
10. Membandingkan dua elemen bertipe string dengan mengubah keduanya ke huruf kecil (lower()), agar pengurutan tidak terpengaruh huruf besar/kecil.
11. Memanggil fungsi tukar untuk menukar posisi kedua elemen agar urutan menjadi benar.
12. -
13. -
14. Mendefinisikan fungsi main sebagai fungsi utama yang mengatur alur program dari awal sampai akhir.
15. Memulai blok try untuk mengantisipasi kesalahan saat user memasukkan jumlah mahasiswa.
16. Meminta user memasukkan jumlah mahasiswa yang akan diinput, lalu mengubahnya menjadi tipe data integer.
17. Menangkap error ValueError jika user memasukkan input selain angka.
18. Menampilkan pesan bahwa input tidak valid agar user tahu kesalahannya.
19. -Menghentikan program menggunakan return jika terjadi kesalahan input.
20. -
21. Membuat list kosong bernama arr yang akan digunakan untuk menyimpan nama-nama mahasiswa.
22. -
23. Menampilkan pesan instruksi kepada user untuk mulai memasukkan nama mahasiswa.
24. Melakukan perulangan sebanyak jumlah mahasiswa (n) agar semua nama bisa diinput.
25. Meminta user memasukkan nama mahasiswa satu per satu sesuai urutan.
26. Menambahkan setiap nama yang diinput ke dalam list arr menggunakan method append().
27. -
28. Menampilkan isi list arr sebelum dilakukan proses pengurutan, agar bisa dibandingkan dengan hasil setelah sorting.
29. -
30. Memanggil fungsi bubble_sort dengan parameter array dan jumlah data untuk mengurutkan nama mahasiswa.
31. -
32. Menampilkan judul bahwa data berikut adalah hasil setelah diurutkan.
33. Melakukan perulangan untuk menampilkan semua isi array yang sudah diurutkan.
34. Menampilkan setiap nama mahasiswa satu per satu sesuai urutan alfabet.
35. -
36. -
37. Baris standar Python yang memastikan bahwa kode di dalam main() hanya dijalankan jika file ini dijalankan langsung, bukan diimpor.
38. Memanggil fungsi main() untuk menjalankan seluruh program dari awal.

    Output : <img width="783" height="212" alt="Screenshot 2026-05-05 230302" src="https://github.com/user-attachments/assets/3b46c2b8-6f5c-44dc-8394-53db4ec69238" />

    link youtube: https://youtu.be/LXa6kOcltDM?si=Rk6VwTGwELzm7JK7






