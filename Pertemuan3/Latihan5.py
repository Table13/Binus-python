a = int(input("masukan nilai A: "))
b = int(input("masukan nilai B: "))
c = int(input("masukan nilai C: "))

d = b**2 - 4*a*c

x1 = -b + (d ** 0.5) / 2 * a
x2 = -b - (d ** 0.5) / 2 * a

if d > 0: #nilai akar asli
    print("nilai diskriminan",d,"artinya kedua akar adalah bilangan asli yaitu X1 =",x1,". X2 =",x2)
elif d == 0: #memiliki akar kembar
    print("nilai diskriminan",d,"artinya akar adalah angka kemabr yaitu", x1)
elif d < 0: #memiliki angka imajinier
    print("nilai diskriminan",d,"artinya kedua akar memiliki angka imjainer yaitu X1 =",x1,". X2 =",x2)
