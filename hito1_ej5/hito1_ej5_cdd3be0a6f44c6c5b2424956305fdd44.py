x1 = int(input("Ingrese un su rut: "))

#print(len(str(x1)))
d1 = str(x1)
if len(d1) == 8:
    f1 = int(d1[7]) * 2

    f2 = int(d1[6]) * 3

    f3 = int(d1[5]) * 4

    f4 = int(d1[4]) * 5

    f5 = int(d1[3]) * 6

    f6 = int(d1[2]) * 7

    f7 = int(d1[1]) * 2

    f8 = int(d1[0]) * 3

    R1 = int(f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)

if len(d1) == 7:
    f2 = int(d1[6]) * 2

    f3 = int(d1[5]) * 3

    f4 = int(d1[4]) * 4

    f5 = int(d1[3]) * 5

    f6 = int(d1[2]) * 6

    f7 = int(d1[1]) * 7

    f8 = int(d1[0]) * 2

    R1 = int(f2 + f3 + f4 + f5 + f6 + f7 + f8)

R2 = R1//11

R3 = R1 - (R2 * 11)

R4 = 11 - R3
if R4 == 10:
    print("dv = K")
elif R4 == 11:
    print("dv =", 0)
else:
    print("dv =", R4)