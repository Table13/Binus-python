while True:
    angka = int(input("masukan angka: "))
    test_ganjil_genap = angka % 2
    if test_ganjil_genap == 1:
            print('ganjil')
    else:
            print('genap')
    
    userInput = input("ingin memberhentikan program? Y/N: ")
    
    if userInput == "Y" or userInput =="y":
        print()
        continue
    elif userInput == "N" or userInput =="n":
        print()
        break
    else:
        print("saya anggap sebagai memberhentikan program")
        break
