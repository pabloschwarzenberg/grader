#Contestador de celular
numero = str(input("ingrese el numero telefonico (el numero tiene que ser de 8 digitos ): "))
hora =int(input("ingrese hora de la llamada (la hora tiene que ser ingresada en el formato de 0 a 23 horas): "))
m = numero[5:9]
n = numero[0:3]
int(m)
int(n)
if (hora >= 0) and (hora <= 19):
    if(hora<=7):
        print("CONTESTAR")
    elif (hora>=7) and (hora<=14):
        if(m=="909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif (hora>=17) and (hora<=19):
        if(n=="877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
else:
    print("NO CONTESTAR")