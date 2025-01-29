"Program Manajemen Kontak"

class Kontak:
    def __init__(self):
        self.contact = []

    def melihat_kontak(self):
        if self.contact:
            for num, item in enumerate(self.contact, start=1):
                print(f'{num}. {item["nama"]}  ({item["HP"]},{item["email"]})')
        else:
            print("kontak masih kosong !")
            return 1

    def menambah_kontak(self):
        nama = input("Masukan nama kontak yang baru : ")
        HP = input("Masukan Nomor kontak yang baru : ")
        email = input("Masukan email yang baru :  ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.contact.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan!")


    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukan Nomor kontak yang akan di hapus : "))
            del self.contact[i_hapus - 1]
            print("kontak yang dimaksud sudah di hapus")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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
        #keluar dari kontak
        break
    else:
        print("anda memasaukkan pilihan yang salah")
