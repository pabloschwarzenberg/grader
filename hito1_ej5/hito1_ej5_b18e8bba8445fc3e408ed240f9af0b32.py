#Cálculo del dígito verificador de un rut
r = input("Ingrese su rut ")
a = len(r)
if len(r)== 8:
    rut = list(r)
    a = r[7]
    b = r[6]
    c = r[5]
    d = r[4]
    e = r[3]
    f = r[2]
    g = r[1]
    h = r[0]
    a = int(a) * 2
    b = int(b) * 3
    c = int(c) * 4
    d = int(d) * 5
    e = int(e) * 6
    f = int(f) * 7
    g = int(g) * 2
    h = int(h) * 3
    s = a+b+c+d+e+f+g+h
    dv = s%11
    n = 11-dv
    if n == 11:
        n = 0
    if n == 10:
        n = str("k")
        
if len(r)==7:
    r = list(r)
    a = r[6]
    a = int(a) * 2
    b = r[5]
    b = int(b) * 3
    c = r[4]
    c = int(c) * 4
    d = r[3]
    d = int(d) * 5
    e = r[2]
    e = int(e) * 6
    f = r[1]
    f = int(f) * 7
    g = r[0]
    g = int(g) * 2
    s = a+b+c+d+e+f+g
    dv = s%11
    n = 11-dv
    if n == 11:
        n = 0
    if n == 10:
        n = str("k")
print("dv=", n)