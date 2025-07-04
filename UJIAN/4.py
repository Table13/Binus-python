nilaiIcha = [80 ,70 ,70, 80]
nilaiBruno = [90,88,45,100]
dataMhs = {
    "Icha" : nilaiIcha,
    "Bruno" : nilaiBruno
}

def rerata_nilai_mhs(namaMhs, dataDict):
    totalNilai = 0
    try:
        data = dataDict[namaMhs]
        print(f"{"\n"}{namaMhs}")
        for nilai in data:
            totalNilai += int(nilai)
            print(f"{nilai}",end = " ")
        rata_rata = totalNilai / len(data)
        print(f"{"\n"}Nilai Rerata = {rata_rata}")
    except KeyError:
        print(f"{"\n"}tidak ada data nilai mahasiswa bernama {namaMhs}")

rerata_nilai_mhs("Icha", dataMhs)
rerata_nilai_mhs("Bruno", dataMhs)
rerata_nilai_mhs("Wahyu", dataMhs)