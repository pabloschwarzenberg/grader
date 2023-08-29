r=1

while r==1:
    numero = str(input("Ingrese el numero de teléfono --> "))
    print("El numero es: ", numero)
    largo=str(numero)

    if len(numero)==8:

        hora = int(input("Ingrese la hora a la cual se llama --> "))
        print("La hora a la que se llama es:",hora)


        if (hora<8):
            print("CONTESTAR")

        if ((hora>=7) and (hora<=14)):

            t=str(largo[5:8])
            if (largo[5:8]== "909"):
                print("CONTESTAR")
            if (largo[5:8]!= "909"):
                print("NO CONTESTAR")


        if (hora>=14) and (hora<=16):
            print("NO CONTESTAR, entre 14 y 17 horas")

        if (hora>=17) and (hora<=19):
            a=str(largo[0:3])
            if (largo[0:3]=="877"):
                print("NO CONTESTAR")
            if (largo[0:3]!="877"):
                print("CONTESTAR")

        if (hora>=19):
            print("NO CONTESTAR")

        r=r+1

    else:
        print("El número de telefono no es valido, vuelva a ingresarlo")