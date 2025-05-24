umur = int(input("masukan umur anda: "))

"""
Baby = 0 - 1
Toddler = 2 - 3
Preschooler = 4 - 5
Child = 6 - 12
Teenager = 13 - 17
Young Adult = 18 - 21
Pre-adult = 22 - 30
Adult = 31 - 50
Pre-elderly = 51 - 70
Elderly = 71 and above
"""

if ((umur >= 0 ) and (umur <= 1)):
    print("KAMU ADALAH BAYI")
elif ((umur >= 2) and (umur <= 3)):
    print("KAMU ADALAH BALITA")
elif ((umur >= 4) and (umur <= 5)):
    print("KAMU ADALAH ANAK TK")
elif ((umur >= 6) and (umur <= 12)):
    print("KAMU ADALAH ANAK")
elif ((umur >= 13) and (umur <= 17)):
    print("KAMU ADALAH ANAK REMAJA")
elif ((umur >= 22) and (umur <= 30)):
    print("KAMU ADALAH PRA-DEWASA")
elif ((umur >= 31) and (umur <= 50)):
    print("KAMU ADALAH ORANG DEWASA")
elif ((umur >= 51)) and (umur <= 70):
    print("KAMU ADALAH LANSIA")
elif ((umur >= 71)):
    print("ANDA ADALAH SEPUH")
else:
    print("??? KAMU BELUM LAHIR!!")
