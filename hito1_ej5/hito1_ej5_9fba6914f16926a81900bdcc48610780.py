rut = input("Ingrese su rut: ")
a = len(rut)

if len(rut)== 7:
    rut = list(rut)
    a1 = rut[6]
    a1 = int(a1) * 2
    b2 = rut[5]
    b2 = int(b2) * 3
    c3 = rut[4]
    c3 = int(c3) * 4
    d4 = rut[3]
    d4 = int(d4) * 5
    e5 = rut[2]
    e5 = int(e5) * 6
    f6 = rut[1]
    f6 = int(f6) * 7
    g7 = rut[0]
    g7 = int(g7) * 2
    
    suma = a1+b2+c3+d4+e5+f6+g7
    digito_verificador = suma % 11
    resultado = 11-digito_verificador
    
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")

if len(rut) == 8:
    rut = list(rut)
    a1 = rut[7]
    a1 = int(a1) * 2
    b2 = rut[6]
    b2 = int(b2) * 3
    c3 = rut[5]
    c3 = int(c3) * 4
    d4 = rut[4]
    d4 = int(d4) * 5
    e5 = rut[3]
    e5 = int(e5) * 6
    f6 = rut[2]
    f6 = int(f6) * 7
    g7 = rut[1]
    g7 = int(g7) * 2
    h8 = rut[0]
    h8 = int(h8) * 3
    
    suma = a1+b2+c3+d4+e5+f6+g7+h8
    dv = suma%11
    resultado = 11-dv
    
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")

print("dv =", resultado)