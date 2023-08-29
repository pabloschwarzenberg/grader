#Cálculo del dígito verificador de un rut
RUT = input("Ingrese su rut: ")
if len(RUT) == 8:
    h = RUT[7]
    g = RUT[6]
    f = RUT[5]
    e = RUT[4]
    d = RUT[3]
    c = RUT[2]
    b = RUT[1]
    a = RUT[0]
    hf = int(h) * 2
    gf = int(g) * 3
    ff = int(f) * 4
    ef = int(e) * 5
    df = int(d) * 6
    cf = int(c) * 7
    bf = int(b) * 2
    af = int(a) * 3
    i = (af+bf+cf+df+ef+ff+gf+hf) %11
elif len(RUT) == 7:
    g = RUT[6]
    f = RUT[5]
    e = RUT[4]
    d = RUT[3]
    c = RUT[2]
    b = RUT[1]
    a = RUT[0]
    gf = int(g) * 2
    ff = int(f) * 3
    ef = int(e) * 4
    df = int(d) * 5
    cf = int(c) * 6
    bf = int(b) * 7
    af = int(a) * 2
    i = (af + bf + cf + df + ef + ff + gf) % 11

print(i)
If = float(i)
j = 11 - If
if j == 11:
    print("dv = 0")
elif j == 10:
    print("dv = k")

else:
    dv = j
    print("dv = ", j)
