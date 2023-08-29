#Contestador de celular
print("Este programa le dirá si debe contestar o no la llamada.")
s = str(int(input("Ingrese el numero de telefono (8 digitos) de la llamada entrante: ")))
HORA = int(input("Igrese la hora de la llamada: "))

if len(s)!=8:
    print("El numero ingresado no tiene 8 digitos.")

else:
    if 0<=HORA<=7:
        print("CONTESTAR")

    elif 7<HORA<14:
        if int(s[5:])==909:
            print("CONTESTAR")

        else:
            print("NO CONTESTAR")

    elif 17<=HORA<=19:
        if int(s[:3])==877:
            print("NO CONTESTAR")

        else:
            print("CONTESTAR")

    elif 19<HORA<=23:
        print("NO CONTESTAR")
        