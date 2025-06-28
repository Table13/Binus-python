def onlyAngka():
    while True:
        try:
            Age = int(input("Age: "))
            return Age
        except ValueError:
            print("masukan umur dengan angka")

def UserNama():
    Nama = input("Nama: ")
    return Nama

def memintaUserData():
    Age = onlyAngka()
    Address = input("Address: ")
    email = input("Email: ")
    userdata = f"nama: {Nama} \numur: {Age} \ntempat tinggal: {Address} \nemail: {email}"
    return userdata

def mencariFile(NamaFile):
    while True:
        try:
            file = open(f"biodata{NamaFile}.txt", "r")
            file.close()
            print("file sudah ada")
            print("menambahakan biodata ke file")
            return True
        except FileNotFoundError:
            print("file tidak di temukan")
            file = open(f"biodata{NamaFile}.txt", "w")
            file.write("")
            file.close()

def menamaiFile(namaFile):
    while True:
      print(f"apakah kamu ingin menamai filenya dengan 'biodata{namaFile}.txt' mu? ")
      Y = input("Y/N: ")
      if Y.upper() == "Y":
        return namaFile
      elif Y.upper() == "N":
        Nama = input("masukan nama file mu: ")
        return Nama
      else:
        print("tidak ada pilihan itu")

def menambahkanDatakeFile(userData, namaFile):
  file = open(f"biodata{namaFile}.txt", "a")
  file.write(userData)
  file.write(f"\n\n\n ")
  file.close()
  print(f"berhasil menambahkan biodata ke dalam file biodata{namaFile}.txt")

def konfirmasi(NamaFile):
    print(f"apakah kamu yakin ingin membuat file 'biodata{NamaFile}.txt'? ")
    Y = input("Y/any(key): ")
    if Y.upper() == "Y":
      return True
    else:
      return False
while True:
    print("masukan data diri kamu!")
    Nama = UserNama()
    userData = memintaUserData()
    if konfirmasi(NamaFile):
        print("///////////////")
        print("memproses data kamu ke dalam file txt")
        print("mencari file biodata kamu!!")
        NamaFile = menamaiFile(Nama)
        if mencariFile(NamaFile):
            menambahkanDatakeFile(userData, NamaFile)
            print("//////////////")
            print(f"apakah kamu mau memasukan biodata lain? ")
            Y = input("Y/any(key): ")
            if Y.upper() == "Y":
              pass
            else:
              break
    else:
        print("Baik Kamuu tidak jadi membuat file")
        print(f"apakah kamu mau menganti Biodata? ")
        Y = input("Y/any(key): ")
        if Y.upper() == "Y":
          pass
        else:
          break
        continue
