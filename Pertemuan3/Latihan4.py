A = int(input("SISI A : "))
B = int(input("SISI B : "))
C = int(input("SISI C : "))

if ((A + B > C) and (C + B > A) and (A + C > B)):
    if ((A == B) and (A == C) and (C == B)):
        print("INI ADALAH SEGITIGA SAMA SISI")
        if A**2 + B **2 < C**2:
            print("SEGITIGA LANCIP")
        else:
            print("SEGITIGA TUMPUL")
    elif ((A == B) or (A == C) or (C == B)):
        print("INI ADALAH SEGITIGA SAMA KAKI")
        if A**2 + B **2 < C**2:
            print("SEGITIGA LANCIP")
        else:
            print("SEGITIGA TUMPUL")
    elif A**2 + B **2 == C**2:
        print("INI ADALAH SEGITIGA SIKU SIKU")
    else:
        print("INI ADALAH SEGITIGA SEMBARANG")
        if A**2 + B **2 < C**2:
            print("SEGITIGA LANCIP")
        else:
            print("SEGITIGA TUMPUL")
else:
    print("BUKAN SEGITIGA")
    
