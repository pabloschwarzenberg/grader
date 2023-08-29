#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut: "))

if rut >= 10000000 and rut <= 99999999 or rut >= 1000000 and rut <= 9999999:
    d8 = rut % 10
    rut = rut//10

    d7 = rut % 10
    rut = rut//10

    d6 = rut % 10
    rut = rut//10

    d5 = rut % 10
    rut = rut//10

    d4 = rut % 10
    rut = rut//10

    d3 = rut % 10
    rut = rut//10

    d2 = rut % 10
    rut = rut//10

    d1 = rut % 10
    rut = rut//10

    suma= d8*2+d7*3+d6*4+d5*5+d4*6+d3*7+d2*2+d1*3

    resta= suma % 11

    resultado = 11 - resta

    if resultado == 11:
        print("dv=0")
    if resultado == 10:
        print("dv=K")
    else:
        print("dv= ", resultado)
else:
    print("Rut invalido")   