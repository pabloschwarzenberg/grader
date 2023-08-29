a = input("ingrese rut: ")
m1 = int(a[-1]) * 2
m2 = int(a[6]) * 3
m3 = int(a[5]) * 4
m4 = int(a[4]) * 5
m5 = int(a[3]) * 6
m6 = int(a[2]) * 7
m7 = int(a[1]) * 2
s = m1 + m2 + m3 + m4 + m5 + m6 + m7
d = 11 - (s % 11)
if d == 11:
    print("dv=0")
elif d == 10:
    print("dv=k")
else:
    print("dv=", d)

      