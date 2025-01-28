"Program Manajemen Kontak"

def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]}  ({item["HP"]},{item["email"]})')
    else:
        print("kontak masih kosong !")
        return 1

def menambah_kontak():
    nama = input("Masukan nama kontak yang baru : ")
    HP = input("Masukan Nomor kontak yang baru : ")
    email = input("Masukan email yang baru :  ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil di tambahkan!")

def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan Nomor kontak yang akan di hapus : "))
        del kontak[i_hapus - 1]
        print("kontak yang dimaksud sudah di hapus")

kontak1 = {'nama' : "Andi", 'HP' :'081348099888' , 'email' : 'andi@python.com'}
kontak2 = {'nama' : "Nia", 'HP' :'081525099888' , 'email' : 'nia@python.com'}
kontak = [kontak1 , kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("masukan pilihan menu kontak (1,2,3 atau 4):  ")

    if pilihan == '1':
        melihat_kontak()

    elif  pilihan == '2':
        # menambahkan kontak
        menambah_kontak()

    elif pilihan == '3':
        # menghapus kontak
        menghapus_kontak()

    elif pilihan =='4':
        #keluar dari kontak
        break
    else:
        print("anda memasaukkan pilihan yang salah")
