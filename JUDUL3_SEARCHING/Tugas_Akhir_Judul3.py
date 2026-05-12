def sequential_search_all(data, target):
    """Mencari semua posisi target dalam data"""
    positions = [i for i, x in enumerate(data) if x == target]
    return positions


def main():
    inventaris = []  
    while True:
        print("\n=== Menu Inventaris Gudang ===")
        print("1. Input ID Barang")
        print("2. Cari ID Barang")
        print("3. Cek Daftar ID Barang")
        print("4. Keluar")
        
        pilihan = input("Pilih menu berikut, (1/2/3/4): ")
        
        if pilihan == "1":
            try:
                id_barang = int(input("Masukkan ID barang: "))
                inventaris.append(id_barang)
                print(f"Barang dengan ID {id_barang} berhasil ditambahkan ke dalam stock.")
            except ValueError:
                print("Input harus berupa kode barang, bukan nama barang!")
        
        elif pilihan == "2":
            if not inventaris:
                print("Inventaris masih kosong, silakan input id barang dulu.")
                continue
            try:
                target = int(input("Masukkan ID barang yang ingin dicari: "))
                positions = sequential_search_all(inventaris, target)
                if positions:
                    print(f"Barang dengan ID {target} ditemukan sebanyak {len(positions)} kali.")
                    print(f"Dengan posisi indeks: {positions}")
                else:
                    print(f"Barang dengan ID {target} tidak ditemukan.")
            except ValueError:
                print("Input harus berupa kode barang, bukan nama barang!")
        
        elif pilihan == "3":
            if not inventaris:
                print("Inventaris masih kosong.")
            else:
                print("Daftar ID Barang di Gudang:")
                for i, id_barang in enumerate(inventaris):
                    print(f"Indeks {i}: ID {id_barang}")
        
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()

