def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []

    print("Masukkan nama mahasiswa:")
    for i in range(n):
        nama = input(f"Nama mahasiswa ke-{i + 1}: ")
        arr.append(nama)

    print(f"\nDaftar nama mahasiswa sebelum diurutkan: {arr}")

    bubble_sort(arr, n)

    print("\nDaftar absen mahasiswa yang telah diurutkan:")
    for i in range(n):
        print(arr[i])


if __name__ == "__main__":
    main()