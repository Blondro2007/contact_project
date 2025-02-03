"Program Manajemen Kontak"
def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        contact = file.readlines()
    return contact

def menyimpan_kontak(path='kontak.txt' , isi=[]):
    with open(path , mode='w') as file:
        file.writelines(isi)


class Kontak:
    def __init__(self):
        self.contact = membuka_kontak()

    def melihat_kontak(self):
        if self.contact:
            for num, item in enumerate(self.contact, start=1):
                # print(f'{num}. {item["nama"]}  ({item["HP"]},{item["email"]})')
                print(f'{num}. '+ item)
        else:
            print("kontak masih kosong !")
            return 1

    def menambah_kontak(self):
        nama = input("Masukan nama kontak yang baru : ")
        HP = input("Masukan Nomor kontak yang baru : ")
        email = input("Masukan email yang baru :  ")
        #kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        kontak_baru = f'{nama} ({HP} , {email})' + '\n'
        self.contact.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan!")


    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan Nomor kontak yang akan di hapus : "))
                del self.contact[i_hapus - 1]
                print("kontak yang dimaksud sudah di hapus")
            except:
                print("input yang anda masukkan salah !")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.contact)

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
        # keluar dari kontak
        kontak_kantor.keluar_kontak()
        break
    else:
        print("anda memasukkan pilihan yang salah")
