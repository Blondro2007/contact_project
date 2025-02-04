'berisi fungsi membuka dan menyimpan kontak'

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        contact = file.readlines()
    return contact

def menyimpan_kontak(path='kontak.txt' , isi=[]):
    with open(path , mode='w') as file:
        file.writelines(isi)