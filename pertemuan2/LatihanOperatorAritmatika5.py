import math

flt_longitude_A = float(input("masukan longitude A: "))
flt_latitude_A = float(input("masukan latitude A: "))
flt_longitude_B = float(input("masukan longitude B: "))
flt_latitude_B = float(input("masukan latitude B: "))

pi = 3.141592643589326

flt_radians_long_a = flt_longitude_A * pi / 180
flt_radians_lat_a = flt_latitude_A * pi / 180
flt_radians_long_b = flt_longitude_B * pi / 180
flt_radians_lat_b = flt_latitude_B * pi / 180

delta_long = flt_radians_long_b - flt_radians_long_a
delta_lat = flt_radians_lat_b - flt_radians_lat_a

a = math.sin(delta_lat / 2)**2 + math.cos(flt_radians_lat_a) * math.cos(flt_radians_lat_b) * math.sin(delta_long / 2)**2

c = 2 * math.atan2(math.sqrt(a),math.sqrt(1 - a))

d = 6371 * c

print(a, c, d)
print("jarak dari titik a ke titik b adalah",d,"KM")
