class Node:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        self.left = None
        self.right = None


class LeaderboardMahasiswa:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nama, nilai):
        if root is None:
            return Node(nama, nilai)
        
        if nilai < root.nilai:
            root.left = self.insert_node(root.left, nama, nilai)
        elif nilai > root.nilai:
            root.right = self.insert_node(root.right, nama, nilai)
        return root

    def insert(self, nama, nilai):
        self.root = self.insert_node(self.root, nama, nilai)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.right)  
        print(f"{root.nama} - {root.nilai}")
        self.inorder(root.left)

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.nama, current.nilai

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.nama, current.nilai

    def sum_nilai(self, root):
        if root is None:
            return 0
        return root.nilai + self.sum_nilai(root.left) + self.sum_nilai(root.right)

    def count_mahasiswa(self, root):
        if root is None:
            return 0
        return 1 + self.count_mahasiswa(root.left) + self.count_mahasiswa(root.right)


def main():
    lb = LeaderboardMahasiswa()
    pilih = 0
    while pilih != 6:
        print("\n=== Leaderboard Mahasiswa ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Leaderboard")
        print("3. Nilai Tertinggi & Terendah")
        print("4. Jumlah Mahasiswa")
        print("5. Rata-rata Nilai")
        print("6. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama mahasiswa: ")
            try:
                nilai = int(input("Masukkan nilai: "))
                lb.insert(nama, nilai)
                print(f"{nama} dengan nilai {nilai} berhasil ditambahkan.")
            except ValueError:
                print("Nilai harus berupa angka!")
        elif pilih == 2:
            print("\n=== Leaderboard (Nilai Tertinggi ke Terendah) ===")
            lb.inorder(lb.root)
        elif pilih == 3:
            max_mhs = lb.find_max(lb.root)
            min_mhs = lb.find_min(lb.root)
            print(f"Nilai Tertinggi: {max_mhs[0]} - {max_mhs[1]}")
            print(f"Nilai Terendah: {min_mhs[0]} - {min_mhs[1]}")
        elif pilih == 4:
            print(f"Jumlah Mahasiswa: {lb.count_mahasiswa(lb.root)}")
        elif pilih == 5:
            total = lb.sum_nilai(lb.root)
            jumlah = lb.count_mahasiswa(lb.root)
            rata = total / jumlah if jumlah > 0 else 0
            print(f"Rata-rata Nilai: {rata:.2f}")
        elif pilih == 6:
            print("Program selesai, Terimakasih telah menggunakan program ini guys.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
