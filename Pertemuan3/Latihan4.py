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

if jenisKonvensi == 1:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    F = 9/5 * Suhu + 32
    print("Suhu yang di ingin di ubah adalah Celsius ke Fahrenheit.",Suhu,"Celsius menjadi",F,"Fahrenheit")
elif jenisKonvensi == 2:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    K = Suhu + 273
    print("Suhu yang di ingin di ubah adalah Celsius ke Kelvin.",Suhu,"Celsius menjadi",K,"Kelvin")
elif jenisKonvensi == 3:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    C = 5/9 * Suhu - 32
    print("Suhu yang di ingin di ubah adalah Fahrenheit ke Celsius.",Suhu,"Fahrenheit menjadi",C,"Celsius")
elif jenisKonvensi == 4:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    K = 5/9 * (Suhu-32) + 273
    print("Suhu yang di ingin di ubah adalah Fahrenheit ke Kelvin.",Suhu,"Fahrenheit menjadi",K,"Kelvin")
elif jenisKonvensi == 5:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    C = Suhu - 273
    print("Suhu yang di ingin di ubah adalah Kelvin ke Celsius.",Suhu,"Kelvin menjadi",C,"Celsius")
elif jenisKonvensi == 6:
    Suhu = int(input("masukan Suhu yang ingin di ubah: "))
    F = 9/5 * (Suhu-273) + 32
    print("Suhu yang di ingin di ubah adalah Kelvin ke Fahrenheit.",Suhu,"Kelvin menjadi",F,"Fahrenheit")
else:
    print("MOHON PILIH JENIS NOMOR KONVESI YANG TERTERA!!!")
