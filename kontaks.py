'Berisi kelas kontak untuk menjalankan Program kontak'

import dokumen

class Kontak:
    def __init__(self):
        self.contact = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.contact)