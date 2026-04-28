def menu():
    print("\nPENGINPUTAN NILAI MAHASISWA")
    print("1. Tampilkan Semua Nilai Mahasiswa")
    print("2. Input/Update Nilai Mahasisiswa")
    print("3. Lihat Rata-rata Nilai Setiap Mahasiswa")
    print("4. Keluar")

def main():
    mata_kuliah = ["STRUKTUR DATA", "REKAYASA PERANGKAT LUNAK", "MATEMATIKA DISKRIT", "ALGORITMA MATRIKS", "KALKULUS"]
    jumlah_matkul = len(mata_kuliah)
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    nilai_mahasiswa = [[0 for _ in range(jumlah_matkul)] for _ in range(jumlah_mahasiswa)]
    
    running = True
    while running:
        menu()
        choice = int(input("Pilih menu : "))

        if choice == 1:
            print("\nTabel Nilai Mahasiswa")
            for i in range(jumlah_mahasiswa):
                print(f"Mahasiswa {i+1}: {nilai_mahasiswa[i]}")

        elif choice == 2:
            print("\nInput Nilai")
            for i in range(jumlah_mahasiswa):
                print(f"> Mahasiswa {i+1}:")
                for j in range(jumlah_matkul):
                    nilai_mahasiswa[i][j] = int(input(f"  {mata_kuliah[j]}: "))

        elif choice == 3:
            print("\nRata-rata Nilai")
            for i in range(jumlah_mahasiswa):
                rata_rata = sum(nilai_mahasiswa[i]) / jumlah_matkul
                print(f"Mahasiswa {i+1}: {rata_rata:.2f}")

        elif choice == 4:
            running = False
            print("Keluar...")

if __name__ == "__main__":
    main()
