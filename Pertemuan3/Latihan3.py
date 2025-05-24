print("""
Pilih jenis konvensi yang anda mau
1.Celcius ke Fahrenheit
2.Celcius ke Kelvin
3.Fahrenheit ke Celsius
4.Fahrenheit ke Kelvin
5.Kelvin ke Celcius
6.Kelvin ke Fahrenheit
""")

jenisKonvensi = int(input("masukan konvensi berdasarkan nomernya: "))

if ((jenisKonvensi >= 1) and (jenisKonvensi <=6)):
    suhu = int(input("masukan Suhu yang ingin di ubah: "))
    if jenisKonvensi == 1:
        f = 9/5 * Suhu + 32
        print("Suhu yang di ingin di ubah adalah Celsius ke Fahrenheit.",suhu,"Celsius menjadi",f,"Fahrenheit")
    elif jenisKonvensi == 2:
        k = suhu + 273
        print("Suhu yang di ingin di ubah adalah Celsius ke Kelvin.",suhu,"Celsius menjadi",k,"Kelvin")
    elif jenisKonvensi == 3:
        c = 5/9 * suhu - 32
        print("Suhu yang di ingin di ubah adalah Fahrenheit ke Celsius.",suhu,"Fahrenheit menjadi",c,"Celsius")
    elif jenisKonvensi == 4:
        k = 5/9 * (suhu-32) + 273
        print("Suhu yang di ingin di ubah adalah Fahrenheit ke Kelvin.",suhu,"Fahrenheit menjadi",k,"Kelvin")
    elif jenisKonvensi == 5:
        c = suhu - 273
        print("Suhu yang di ingin di ubah adalah Kelvin ke Celsius.",suhu,"Kelvin menjadi",c,"Celsius")
    elif jenisKonvensi == 6:
        f = 9/5 * (suhu-273) + 32
        print("Suhu yang di ingin di ubah adalah Kelvin ke Fahrenheit.",suhu,"Kelvin menjadi",f,"Fahrenheit")
else:
    print("MOHON PILIH JENIS NOMOR KONVESI YANG TERTERA!!!")
