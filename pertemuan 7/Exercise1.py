print("masukan data diri kamu!")
Nama = input("Nama: ")
Age = int(input("Age: "))
Address = input("Address: ")
email = input("Email: ")

bioFile = open("Test.txt", "w" )
bioFile.write(f" nama: {Nama} \n umur: {Age} \n tempat tinggal: {Address} \n email: {email}")
bioFile.close()

bioFile = open("Test.txt", "r" )
text = bioFile.read()
print(text)
bioFile.close()
