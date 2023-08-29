#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut: ")
a = len(rut)
if len(rut)== 8:
    rut = list(rut)
    e = rut[7]
    e = int(e) * 2
    f = rut[6]
    f = int(f) * 3
    g = rut[5]
    g = int(g) * 4
    h = rut[4]
    h = int(h) * 5
    i = rut[3]
    i = int(i) * 6
    j = rut[2]
    j = int(j) * 7
    x = rut[1]
    x = int(x) * 2
    l = rut[0]
    l = int(l) * 3
    suma = e+f+g+h+i+j+x+l
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
        
if len(rut)==7:
    rut = list(rut)
    e = rut[6]
    e = int(e) * 2
    f = rut[5]
    f = int(f) * 3
    g = rut[4]
    g = int(g) * 4
    h = rut[3]
    h = int(h) * 5
    i = rut[2]
    i = int(i) * 6
    j = rut[1]
    j = int(j) * 7
    x = rut[0]
    x = int(x) * 2
    suma = e+f+g+h+i+j+x
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
print("dv=", resultado)      