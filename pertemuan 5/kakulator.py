print("KAKULATOR")

def f_pertambahan(value1, value2):
    hasil = value1 + value2 
    print("Hasil penjumlahan dari",value1, "+", value2, "=", hasil)

def f_pengurangan(value1, value2):
    hasil = value1 - value2 
    print("Hasil penjumlahan dari",value1, "+", value2, "=", hasil)

def f_pembagian(value1, value2):
    if value2 != 0:
        hasil = value1 / value2 
        print("Hasil penjumlahan dari",value1, "+", value2, "=", hasil)
    else:
        print("tidak bisa dibagi dengan 0")

def f_perkalian(value1, value2):
    hasil = value1 * value2 
    print("Hasil penjumlahan dari",value1, "+", value2, "=", hasil)

def f_modulus(value1, value2):
    if (value2 != 0 and value1 != 0) and (value1 >= value2):
        hasil = value1 % value2
        print("Hasil penjumlahan dari",value1, "+", value2, "=", hasil)
    else:
        print("tidak bisa dibagi dengan 0")

def f_operator():
    operator = input("Masukan operator (+|-|/|*|%|stop): ")
    operator_list = ("+","-","/", "*", "%", "stop")
    if operator in operator_list:
        return operator
    else:
        print("TIDAK ADA PILIHAN")
        return f_operator()

def f_value1():
    value1 = input("masukan nilai pertama: ")
    return int(value1)

def f_value2():
    value2 = input("masukan nilai kedua: ")
    return int(value2)

run = True
while run:
    
    operator = f_operator()
    if operator == "stop":
        print("PROGRAM TELAH BERHENTI. terimakasih sudah mengguanakan program ini")
        break
    
    value1 = f_value1()
    value2 = f_value2()
    
    if operator == "+":
        f_pertambahan(value1, value2)
    elif operator == "-":
        f_pengurangan(value1, value2)
    elif operator == "/":
        f_pembagian(value1, value2)
    elif operator == "*":
        f_perkalian(value1, value2)
    elif operator == "%":
        f_modulus(value1, value2)
    
    print()
