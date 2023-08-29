#Cálculo del dígito verificador de un rut
rut_titular = input("Ingrese su rut: ")
A= len(rut_titular)
if len(rut_titular)== 8:
    rut = list(rut_titular)
    a = rut_titular[7]
    a = int(a) * 2
    b = rut_titular[6]
    b = int(b) * 3
    c = rut_titular[5]
    c = int(c) * 4
    d = rut_titular[4]
    d = int(d) * 5
    e = rut_titular[3]
    e = int(e) * 6
    f = rut_titular[2]
    f = int(f) * 7
    g = rut_titular[1]
    g = int(g) * 2
    h = rut_titular[0]
    h = int(h) * 3
    suma = a+b+c+d+e+f+g+h
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
        
if len(rut_titular)==7:
    rut = list(rut_titular)
    a = rut_titular[6]
    a = int(a) * 2
    b = rut_titular[5]
    b = int(b) * 3
    c = rut_titular[4]
    c = int(c) * 4
    d = rut_titular[3]
    d = int(d) * 5
    e = rut_titular[2]
    e = int(e) * 6
    f = rut_titular[1]
    f = int(f) * 7
    g = rut_titular[0]
    g = int(g) * 2
    suma = a+b+c+d+e+f+g
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
print("dv=", resultado)      