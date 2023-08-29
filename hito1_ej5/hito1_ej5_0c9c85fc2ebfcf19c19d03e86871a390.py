#Cálculo del dígito verificador de un rut
rut = int(input("ingrese numero rut, sin digito verificador: "))


if rut > 9999999:
    nro1 = rut % 10
    nro2 = rut % 100
    nro2 = nro2 // 10
    nro3 = rut % 1000
    nro3 = nro3 // 100
    nro4 = rut % 10000
    nro4 = nro4 // 1000
    nro5 = rut % 100000
    nro5 = nro5 // 10000
    nro6 = rut % 1000000
    nro6 = nro6 // 100000
    nro7 = rut % 10000000
    nro7 = nro7 // 1000000
    nro8 = rut % 100000000
    nro8 = nro8 // 10000000


    suma = int(nro1*2 + nro2*3 + nro3*4 + nro4*5 + nro5*6 + nro6*7 + nro7*2 + nro8*3)
    resto = int(suma/11)
    resta= suma - (11*resto)
    dv = 11-resta
    

    if dv == 11:
        print("dv=",0)
    elif dv == 10:
        print("dv= K")
    else:
        print("dv=", dv)

else:
    nro10 = rut % 10
    nro20 = rut % 100
    nro20 = nro20 // 10
    nro30 = rut % 1000
    nro30 = nro30 // 100
    nro40 = rut % 10000
    nro40 = nro40 // 1000
    nro50 = rut % 100000
    nro50 = nro50 // 10000
    nro60 = rut % 1000000
    nro60 = nro60 // 100000
    nro70 = rut % 10000000
    nro70 = nro70 // 1000000

    suma = int(nro10*2 + nro20*3 + nro30*4 + nro40*5 + nro50*6 + nro60*7 + nro70*2)
    resto = int(suma/11)
    resta= suma - (11*resto)
    dv = 11-resta
    
    if dv == 11:
        print("dv=",0)
    elif dv == 10:
        print("dv= K")
    else:
        print("dv=", dv)