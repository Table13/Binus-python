"""
JUDUL
CEK SISWA LULUS ATAU TIDAK
///////
Deklarasi:
nilai siswa, kkm : integer lulus, tidak lulus
////////
Deksripsi:
START
masukan(nilai siswa)

kkm=75
cekNilai= kkm - nilai siswa

if cekNilai > 0
    Print(LULUS)
else
    Print(TIDAK LULUS)
END
"""
int_nilaiSiswa = int(input("masukan nilai anda: "))
print("kkm anda adalah 75")
kkm = 75 
cekNilai = int_nilaiSiswa - kkm
if cekNilai > 0:
    print("LULUS")
else:
    print("TIDAK LULUS")
