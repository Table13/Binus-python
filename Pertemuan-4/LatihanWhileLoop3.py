print("""
A = 4.00
A- = 3.75
B+ = 3.50
B = 3.00
B- = 2.75
C+ = 2.50
C = 2.00
C- = 1.75
D = 1.50
E = 1.20
""")
y = -1
varpenampung = 0
satu = 1
while True:
    print('pencet "enter" untuk di jumlah')
    nilai = input("masukan nilai " + str(satu)+ ": ")
    y += 1
    satu += 1
    if nilai == "E":
        varpenampung += 1.20
    elif nilai == "D":
        varpenampung += 1.50
    elif nilai == "C-":
        varpenampung += 1.75
    elif nilai == "C":
        varpenampung += 2.00
    elif nilai == "C+":
        varpenampung += 2.50
    elif nilai == "B-":
        varpenampung += 2.75
    elif nilai == "B":
        varpenampung += 3.00
    elif nilai == "B+":
        varpenampung += 3.50
    elif nilai == "A-":
        varpenampung += 3.75
    elif nilai == "A":
        varpenampung += 4.00
    else:
        x = varpenampung/y
        if x <= 1.20:
            abjad = "E"
        elif x <= 1.50:
            abjad = "D"
        elif x <= 1.75:
            abjad = "C-"
        elif x <= 2.00:
            abjad = "C"
        elif x <= 2.50:
            abjad = "C+"
        elif x <= 2.75:
            abjad = "B-"
        elif x <= 3.00:
            abjad = "B"
        elif x <= 3.50:
            abjad = "B+"
        elif x <= 3.75:
            abjad = "A-"
        elif x <= 4.00:
            abjad = "A"
        else:
            abjad = ""
        print("Nilai rata-rata kamu adalah " + str(x) + " di tandai dengan abjad "+ abjad)
        break
