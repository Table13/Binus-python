while True:
    A = int(input("SISI A : "))
    B = int(input("SISI B : "))
    C = int(input("SISI C : "))
    
    if (A) and (B) and (C):
        if ((A + B > C) and (C + B > A) and (A + C > B)):
            if ((A == B) and (A == C) and (C == B)):
                print("INI ADALAH SEGITIGA SAMA SISI")
            elif ((A == B) or (A == C) or (C == B)):
                print("INI ADALAH SEGITIGA SAMA KAKI")
            elif A**2 + B **2 == C**2:
                print("INI ADALAH SEGITIGA SIKU SIKU")
            else:
                print("INI ADALAH SEGITIGA SEMBARANG")
        else:
            print("BUKAN SEGITIGA")
        
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
