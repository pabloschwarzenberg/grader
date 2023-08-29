celular = 0;
hora = 0;
x = True

print("Bienvenido a la contestadora automatica")
while(x):
    celular = input("Ingrese el número de celular: ")

    if (len(celular) < 8) or (len(celular) > 8):
        x = True
        print("Celular debe tener un largo de 8 digitos\n")

    else:
        x = True
        break

x = True
while(x):
    #print("Ingrese hora de la llamada")
    hora = int(input("Ingrese hora de la llamada: "))
    if (hora <0) or (hora>23):
        x = True
        print("Hora debe ser de 0 a 23")
    else:
        x = False
        break

    if ((hora >=0) and (hora <=7)):
        print("CONTESTAR")
    elif((hora <= 14) and (hora > 7)):
        celularString = str(celular)
        ultimosDigitos = celularString[5:8]
        if (ultimosDigitos =="909"):
            print("CONTESTAR")

        else:
            print("NO CONTESTAR")
    elif ((hora >=17) and (hora<= 19)):
        celularString =str(celular)
        primerosDigitos = celularString[0:3]

        if (primerosDigitos =="877"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif ((hora<19) and (hora<23)):
        print("NO CONTESTAR")

    elif((hora>14) and (hora<17)):
        print("INDEFINIDO") 