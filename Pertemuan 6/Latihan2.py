#-_---pre program--__---
class siswa:
    def __init__(self, nama="siswa", umur=0, tempatTinggal="kota"):
        self.nama = nama
        self.umur = umur
        self.tempatTinggal = tempatTinggal
        
    @property
    def nama(self):
        return self._nama
    @nama.setter
    def nama(self, nama):
        self._nama = nama
    
    @property
    def umur(self):
        return self._umur
    @umur.setter
    def umur(self, umur):
        self._umur = umur
    
    @property
    def tempatTinggal(self):
        return self._tempatTinggal
    @tempatTinggal.setter
    def tempatTinggal(self,tempatTinggal):
        self._tempatTinggal = tempatTinggal
    
    def setData(self, nama, umur, tempatTinggal):
        self.nama = nama
        self.umur = umur
        self.tempatTinggal = tempatTinggal
    
    def showData(self):
        print(f'nama {self.nama} umur {self.umur} tahun tinggal di {self.tempatTinggal}')
Datasiswa = []
#end pre program

print("going to run program wait")

#utility
def Inputcek(Input):
    if not Input.strip():
        return False
    else:
        return True

def stopper(Input):
    if Input.lower() == 'stop':
        return True
    else:
        try:
            int(Input)
            return False
        except ValueError:
            print('////////////////')
            print(f'tidak ada pilihan {Input}')
            return False

def lanjut(keadaan):
    while True:
        lanjut = input(f"lanjut {keadaan}? Y/N: ")
        cek = Inputcek(lanjut)
        if cek:
            if lanjut.upper() == "Y":
                return True
            else:
                if lanjut.upper() == "N":
                    return False
                elif not stopper(lanjut):
                    continue
        else:
            print('pilihan tidak boleh kosong')
            continue

def noData():
    if len(Datasiswa) == 0:
        print('///////////////////')
        print('kamu belum memasukan data')
        print('///////////////////')
        if not lanjut(keadaan="memasukan data"):
            return True
        else:
            memasukanData()
    else:
        return False

def InputUtility():
    while True:
        print(f'''apa yang ingin anda lakukan?
            ketik 'stop' untuk berhenti
            1. memasukan data siswa
            2. menampilkan data siswa
            3. mengubah data siswa
            4. menghapus data siswa''')
        utility = input("pilihan: ")
        cek = Inputcek(utility)
        if cek:
            if not stopper(utility):
                try:
                    utility = int(utility)
                    if utility > 4 or utility < 1:
                        print(f'tidak ada pilihan ke {utility}')
                        print('/////////////////////')
                    else:
                        return utility
                except ValueError:
                    print("masukan pilihan utility dengan pilihan angka 1,2,3,4 bukan satu dua")
                    print()
                    continue
            else:
                return utility
        else:
            print('tidak boleh kosong')
            print('///////////')
            continue


def InputNama():
    while True:
        namaSiswa = input("nama siswa: ")
        cek = Inputcek(namaSiswa)
        if cek:
            number = 0
            for i in list(namaSiswa):
                try:
                    cek_angka = int(i)
                    number += 1
                except ValueError:
                    number += 0
            if number > 0:
                print("nama anda tidak valid, terdeteksi angka di nama anda")
                print()
            else:
                return namaSiswa
        else:
            print(f'Nama tidak boleh kosong')

def cariNama():
    while True:
        namaSiswa = input("data siapa yang ingin anda cari?(nama): ")
        cek = Inputcek(namaSiswa)
        if cek:
            ditemukan = False
            for v_Siswa in Datasiswa:
                if v_Siswa.nama.lower() == namaSiswa.lower():
                    ditemukan = True
                    return v_Siswa
            if not ditemukan:
                print(f"tidak memukan data siswa dengan nama {namaSiswa}")
                if not lanjut(keadaan=f'ubah nama'):
                    break
                else:
                    continue
        else:
            print("nama tidak boleh kosong")

def InputUmur():
    while True:
        umurSiswa = input("umur siswa: ")
        try:
            umurSiswa = int(umurSiswa)
            return umurSiswa
        except ValueError:
            cek = Inputcek(umurSiswa)
            if not cek:
                print('umur tidak boleh kosong')
            else:
                print("masukan umur dengan angka (1,13,25) bukan (satu, tiga)")

def InputTempatTinggal():
    while True:
        tempatTinggalSiswa = input("TempatTinggal: ")
        cek = Inputcek(tempatTinggalSiswa)
        if cek:
             return tempatTinggalSiswa
        else:
            print('tempat tinggal tidak boleh kosong')

def memasukanData():
    while True:
        nama1 = InputNama()
        umur1 = InputUmur()
        tempatTinggal1 = InputTempatTinggal()
        siswadata = siswa()
        siswadata.setData(nama1, umur1, tempatTinggal1)
        Datasiswa.append(siswadata)
        print('//////////////')
        siswadata.showData()
        print('berhasil tersimpan')
        print('//////////////')
        if not lanjut(keadaan="memasukan data siswa lain"):
            break
        else:
            print('//////////////')
            continue

def menampilkanData():
    def showSemuaData():
        while True:
            no = 1
            print('//////////////')
            print("ini semua data siswa: ")
            for data in Datasiswa:
                print(f'siswa {no}: nama {data.nama} berumur {data.umur} tahun tinggal di {data.tempatTinggal}')
                no+=1
            print('//////////////')
            if not lanjut(keadaan="menampilkan semua data siswa"):
                break
            else:
                continue
    def showDenganNama():
        while True:
            dataSiswa = cariNama()
            try:
                print('//////////////')
                dataSiswa.showData()
                print('//////////////')
            except AttributeError:
                break
            if not lanjut(keadaan="menampilkan data siswa dengan nama lain"):
                break
            else:
                continue
    while True:
            print("bersedia menampilkan data")
            cariSemua = input("apakah kamu ingin menampilkan SEMUA data siswa, ketik 'stop' untuk kembali? Y/N: ")
            cek = Inputcek(cariSemua)
            if cek:
                if not stopper(cariSemua):
                    if cariSemua.upper() == "Y" or cariSemua.upper() == 'N':
                        if cariSemua.upper() == "Y":
                            showSemuaData()
                        elif cariSemua.upper() == 'N':
                            showDenganNama()
                        if not lanjut(keadaan=f'menampilkan'):
                            break
                        else:
                            continue
                else:
                    break
            else:
                print('pilihan tidak boleh kosong')
                print("///////////////////")
                continue


def mengubahData():
    print("MENGUBAH DATA")
    while True:
        print(f'''apa yang ingin anda rubah?
                ketik 'stop' untuk keluar dari menu "mengubah data"
            1. nama
            2. umur
            3. tempat tinggal''')
        ubahdata = input("pilih yang mana?: ")
        cek = Inputcek(ubahdata)
        if cek:
            if not stopper(ubahdata):
                try:
                    ubahdata = int(ubahdata)
                    if ubahdata >= 1 and ubahdata <= 3:
                        try:
                            dataSiswa = cariNama()
                            dataSiswa.showData()
                        except AttributeError:
                            break
                        if ubahdata == 1:
                            namabaru = InputNama()
                            dataSiswa.nama = namabaru
                            dataSiswa.showData()
                        if ubahdata == 2:
                            umurbaru = InputUmur()
                            dataSiswa.umur = umurbaru
                            dataSiswa.showData()
                        if ubahdata == 3:
                            tempatTinggalBaru = InputTempatTinggal()
                            dataSiswa.tempatTinggal = tempatTinggalBaru
                            dataSiswa.showData()
                        if not lanjut(keadaan=f'mengubah data {dataSiswa.nama}'):
                            break
                        else:
                            continue
                    else:
                        print(f'tidak ada pilihan ke {ubahdata}')
                        print('//////////////')
                except ValueError:
                    continue
            else:
                break
        else:
            print('pilihan tidak boleh kosong')
            print('////////////////')
            continue

def menghapusData():
    print(f' Menu Menghapus Data Siswa')
    def menghapusSemuadata():
        Datasiswa.clear()
        print('semua data terhapus')
    def menghapusDataSesuaiNama():
        while True:
            datasiswa = cariNama()
            try:
                nama = datasiswa.nama
                datasiswa.showData()
            except AttributeError:
                break
            konfirmasi = input("apakah ini data yang ingin di hapus? Y/N: ")
            if konfirmasi.upper() == 'Y':
                Datasiswa.remove(datasiswa)
                print(f'siswa dengan nama {nama} telah di hapus')
            else:
                print(f'anda tidak jadi menghapus data siswa {nama}')
            if not lanjut(keadaan=f'? apakah kamu ingin menghapus data siswa lain'):
                break
            else:
                if noData():
                    break
    while True:
        print('''bagaimana cara kamu ingin hapus data siswa?
                ketik 'stop' untuk keluar menu "menghapus data"
            1. menghapus semua data sekaligus
            2. menghapus berdasarkan nama''')
        pilih = input("pilih: ")
        cek = Inputcek(pilih)
        if cek:
            try:
                pilih = int(pilih)
                if pilih > 0 and pilih < 3:
                    if pilih == 1:
                        menghapusSemuadata()
                        print('/////////////////////')
                        print('kamu tidak memiliki data siswa lagi')
                        print('//////////////////////')
                        break
                    if pilih == 2:
                        menghapusDataSesuaiNama()
                    if not lanjut(keadaan=f'? apakah tidak ada data yang ingin di hapus lagi'):
                        break
                    else:
                        continue
                else:
                    print(f"tidak ada pilihan {pilih} ")
            except ValueError:
                if stopper(pilih):
                    break
                else:
                    continue
        else:
            print(f'Pilihan tidak boleh kosong')
            print('/////////////////////')

#_---MAIN---_
while True:
    v_InputUtility = InputUtility()
    try:
        if v_InputUtility == 1:
            memasukanData()
        elif v_InputUtility > 1:
            if not noData():
                if v_InputUtility == 2:
                    menampilkanData()
                elif v_InputUtility == 3:
                    mengubahData()
                elif v_InputUtility == 4:
                    menghapusData()
    except TypeError:
        if stopper(v_InputUtility):
            break
    print()
