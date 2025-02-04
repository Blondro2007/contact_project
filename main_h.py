"Program Manajemen Kontak"

import kontaks

def main():
    kontak_kantor = kontaks.Kontak()
    kontak_keluarga = kontaks.Kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Melihat semua kontak")
        print("2. Menambahkan kontak baru")
        print("3. Menghapus kontak")
        print("4. Keluar dari kontak")

        pilihan = input("masukan pilihan menu kontak (1,2,3 atau 4):  ")

        if pilihan == '1':
            kontak_kantor.melihat_kontak()

        elif  pilihan == '2':
            # menambahkan kontak
            kontak_kantor.menambah_kontak()

        elif pilihan == '3':
            # menghapus kontak
            kontak_kantor.menghapus_kontak()

        elif pilihan =='4':
            # keluar dari kontak
            kontak_kantor.keluar_kontak()
            break
        else:
            print("anda memasukkan pilihan yang salah")

if __name__ == "__main__":
    main()