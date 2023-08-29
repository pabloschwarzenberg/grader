#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut: ")
a = len(rut)
if len(rut)== 8:
    rut = list(rut)
    a = rut[7]
    a = int(a) * 2
    b = rut[6]
    b = int(b) * 3
    c = rut[5]
    c = int(c) * 4
    d = rut[4]
    d = int(d) * 5
    e = rut[3]
    e = int(e) * 6
    f = rut[2]
    f = int(f) * 7
    g = rut[1]
    g = int(g) * 2
    h = rut[0]
    h = int(h) * 3
    sumas = a+b+c+d+e+f+g+h
    dv = sumas%11
    resultados = 11-dv
    if resultados == 11:
        resultados = 0
    if resultados == 10:
        resultados = str("k")
        
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
    sumas = a+b+c+d+e+f+g
    dv = sumas%11
    resultados = 11-dv
    if resultados == 11:
        resultados = 0
    if resultados == 10:
        resultados = str("k")
print("dv=", resultados)