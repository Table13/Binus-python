#-_---pre program--__---
class siswa:
    def __init__(self, name="siswa", umur=int, tempatTinggal="jakarta"):
        self.name = name
        self.umur = umur
        self.tempatTinggal = tempatTinggal
    
    def setdata(self, nama, umur, tempatTinggal):
        self.name = nama
        self.umur = umur
        self.tempatTinggal = tempatTinggal
    
    def showData(self):
        print(f'nama siswa: {self.name} umur {self.umur} tinggal di {self.tempatTinggal}')
    
Datasiswa = []
#end pre program

print("going to run program wait")

#utility

def lanjut():
    lanjut = input("lanjut? Y/N: ")
    if lanjut.upper() == "Y":
        return True
    else:
        return False

def InputNama():
    namaSiswa = input("nama siswa: ")
    number = 0
    for i in list(namaSiswa):
        try:
            cek = int(i)
            number += 1
        except ValueError:
            number += 0
    if number > 0:
        print("nama anda tidak valid, terdeteksi angka di nama anda")
        print()
        InputNama()
    else:
        return namaSiswa

def InputUmur():
    try:
        umurSiswa = int(input("umur siswa: "))
        return umurSiswa
    except ValueError:
        print("masukan umur dengan angka (1,13,25) bukan (satu, tiga)")
        print()
        InputUmur()

def InputTempatTinggal():
    tempatTinggalSiswa = input("TempatTinggal: ")
    number = 0
    for i in list(tempatTinggalSiswa):
        try:
            cek = int(i)
            number += 1
        except ValueError:
            number += 0
    if number > 0:
        print("nama anda tidak valid, terdeteksi angka di nama anda")
        print()
        InputNama()
    else:
        return tempatTinggalSiswa

#_---MAIN---_
while True:
    nama1 = InputNama()
    umur1 = InputUmur()
    tempatTinggal1 = InputTempatTinggal()
    siswadata = siswa(nama1,umur1,tempatTinggal1)
    Datasiswa.append(siswadata)
    cek = siswadata.showData()
    print('berhasil tersimpan')
    if not lanjut():
        if len(Datasiswa) > 0:
            no = 1
            print()
            print("ini semua data siswa anda: ")
            for data in Datasiswa:
                print(f'nama siswa{no}: {data.name} berumur {data.umur} tinggal di {data.tempatTinggal}')
                no+=1
            break
        else:
            print('kamu belum memasukan data')
            break
    print()
