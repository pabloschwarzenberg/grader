#Cálculo del dígito verificador de un rut
print("Para calcular digito verificador")
rut = str(input("Ingrese su rut sin dígito verificador:"))
if len(rut)==8:
    lista = rut[::-1]
    a1=int(lista[0])*2
    a2=int(lista[1])*3
    a3=int(lista[2])*4
    a4=int(lista[3])*5
    a5=int(lista[4])*6
    a6=int(lista[5])*7
    a7=int(lista[6])*2
    a8=int(lista[7])*3

    suma = a1+a2+a3+a4+a5+a6+a7+a8
    resto = suma%11
    resta = 11-resto

    if resta == 10:
        print("dv = K")
    elif resta == 11:
        print("dv = 0")
    else: 
        print("dv = ", resta)

elif len(rut)==7:
    lista2 = rut[::-1]
    b1=int(lista2[0])*2
    b2=int(lista2[1])*3
    b3=int(lista2[2])*4
    b4=int(lista2[3])*5
    b5=int(lista2[4])*6
    b6=int(lista2[5])*7
    b7=int(lista2[6])*2

    suma2 = b1+b2+b3+b4+b5+b6+b7
    resto2 = suma2%11
    lista2 = 11-resto2

    if lista2 == 10:
        print("dv = k")
    elif lista2 == 11:
        print("dv =0")
    else:
        print("dv =", lista2)
      