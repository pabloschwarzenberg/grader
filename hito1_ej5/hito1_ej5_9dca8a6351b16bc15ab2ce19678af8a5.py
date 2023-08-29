rut = int(input ("Ingrese el rut que desea calcular su guion: ")) #93015041

if rut <= 9999999:
    rut = str(rut)
    numero1 = int(rut[6])*2
    numero2 = int(rut[5])*3
    numero3 = int(rut[4])*4
    numero4 = int(rut[3])*5
    numero5 = int(rut[2])*6
    numero6 = int(rut[1])*7
    numero7 = int(rut[0])*2
    numero8 = 0*3
    suma = (numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8)
    funcion = suma/11
    funcion2 = suma - (int(funcion)*11)
    funcion3 = 11 - funcion2
    if funcion3 == -10 or funcion3 == 10:
        print("dv=k")
    elif funcion3 == -11 or funcion3 == 11:
        print("dv=0")
    else:
        print("dv=",funcion3)
elif rut <= 99999999:
    rut = str(rut)
    numero1 = int(rut[7])*2
    numero2 = int(rut[6])*3
    numero3 = int(rut[5])*4
    numero4 = int(rut[4])*5
    numero5 = int(rut[3])*6
    numero6 = int(rut[2])*7
    numero7 = int(rut[1])*2
    numero8 = int(rut[0])*3
    funcion = ((numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 )%11) -11
    if funcion == 10 or funcion == -10:
        print("dv=k")
    elif funcion == 11 or funcion == -11:
        print("dv=0")
    else:
        print("dv=",funcion)