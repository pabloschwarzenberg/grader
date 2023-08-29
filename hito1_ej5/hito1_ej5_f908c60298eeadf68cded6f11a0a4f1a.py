rut = input("Ingresa tu  rut: ")
x = len(rut)
if len(rut)== 8:
    rut = list(rut)
    Digito1 = rut[7]
    Digito1 = int(Digito1) * 2
    Digito2 = rut[6]
    Digito2 = int(Digito2) * 3
    Digito3 = rut[5]
    Digito3 = int(Digito3) * 4
    Digito4 = rut[4]
    Digito4 = int(Digito4) * 5
    Digito5 = rut[3]
    Digito5 = int(Digito5) * 6
    Digito6 = rut[2]
    Digito6 = int(Digito6) * 7
    Digito7 = rut[1]
    Digito7 = int(Digito7) * 2
    Digito8 = rut[0]
    Digito8 = int(Digito8) * 3
    suma = Digito1+Digito2+Digito3+Digito4+Digito5+Digito6+Digito7+Digito8
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
if len(rut)==7:
    rut = list(rut)
    DIGITTO1 = rut[6]
    DIGITTO1 = int(DIGITTO1) * 2
    DIGITTO2 = rut[5]
    DIGITTO2 = int(DIGITTO2) * 3
    DIGITTO3 = rut[4]
    DIGITTO3 = int(DIGITTO3) * 4
    DIGITTO4 = rut[3]
    DIGITTO4 = int(DIGITTO4) * 5
    DIGITTO5 = rut[2]
    DIGITTO5 = int(DIGITTO5) * 6
    DIGITTO6 = rut[1]
    DIGITTO6 = int(DIGITTO6) * 7
    DIGITTO7 = rut[0]
    DIGITTO7 = int(DIGITTO7) * 2
    suma = DIGITTO1+DIGITTO2+DIGITTO3+DIGITTO4+DIGITTO5+DIGITTO6+DIGITTO7 
    dv = suma%11
    resultado = 11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
print("dv=", resultado)