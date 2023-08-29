rut = int(input("Ingrese el RUT sin digito verificador: "))
rut = str(rut)
if len(rut) == 8:
    digito8 = rut[7]
    digito8 = int(digito8)
    digito7 = rut[6]
    digito7 = int(digito7)
    digito6 = rut[5]
    digito6 = int(digito6)
    digito5 = rut[4]
    digito5 = int(digito5)
    digito4 = rut[3]
    digito4 = int(digito4)
    digito3 = rut[2]
    digito3 = int(digito3)
    digito2 = rut[1]
    digito2 = int(digito2)
    digito1 = rut[0]
    digito1 = int(digito1)
    suma = (digito8*2) + (digito7*3) + (digito6*4) + (digito5*5) + (digito4*6) + (digito3*7) + (digito2*2) + (digito1*3)
    div = suma//11
    resto = suma - (div*11)
    resultado = 11 - resto
    if resultado == 11:
        print("dv=0")
    elif resultado == 10:
        print("dv=k")
    else:
        print("dv=",resultado)
if len(rut) == 7:
    digito7 = rut[6]
    digito7 = int(digito7)
    digito6 = rut[5]
    digito6 = int(digito6)
    digito5 = rut[4]
    digito5 = int(digito5)
    digito4 = rut[3]
    digito4 = int(digito4)
    digito3 = rut[2]
    digito3 = int(digito3)
    digito2 = rut[1]
    digito2 = int(digito2)
    digito1 = rut[0]
    digito1 = int(digito1)
    suma = (digito7*2) + (digito6*3) + (digito5*4) + (digito4*5) + (digito3*6) + (digito2*7) + (digito1*2)
    div = suma//11
    resto = suma - (div*11)
    resultado = 11 - resto
    if resultado == 11:
        print("dv=0")
    elif resultado == 10:
        print("dv=k")
    else:
        print("dv=",resultado)