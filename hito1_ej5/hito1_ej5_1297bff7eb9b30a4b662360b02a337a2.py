#Cálculo del dígito verificador de un rut
rut=input("Ingrese su rut sin el digito verificador: ")
a = len(rut)
if len(rut)== 8:
    rut = list(rut)
    a = rut[7]
    b = rut[6]
    c = rut[5]
    d = rut[4]
    e = rut[3]
    f = rut[2]
    g = rut[1]
    h = rut[0]
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
    r = 11-dv
    if r == 11:
        r = 0
    if r == 10:
        r = str("k")
        
if len(rut)==7:
    rut = list(rut)
    a = rut[6]
    a = int(a) * 2
    b = rut[5]
    b = int(b) * 3
    c = rut[4]
    c = int(c) * 4
    d = rut[3]
    d = int(d) * 5
    e = rut[2]
    e = int(e) * 6
    f = rut[1]
    f = int(f) * 7
    g = rut[0]
    g = int(g) * 2
    s = a+b+c+d+e+f+g
    dv = s%11
    r = 11-dv
    if r == 11:
        r = 0
    if r == 10:
        r = str("k")
print("dv=", r)
