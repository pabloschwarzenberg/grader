#Contestador de celular
numero = int(input("Ingrese el número que le llamó:"))
if(numero<10000000 or numero>99999999):
    print("Número inválido")
else:
    hora = int(input("Ingrese la hora:"))
    if(hora<0 or hora>=24):
        print("No existe esta hora")
    else:
        if(0<=hora<=7):
            print("RESULTADO:CONTESTAR")
        elif(7<hora<14):
            numero = str(numero)
            if(numero[5]=="9" and numero[6]=="0" and numero[7]=="9"):
                print("RESULTADO:CONTESTAR")
            else:
                print("RESULTADO:NO CONTESTAR")
        elif(14<=hora<17):
            print("RESULTADO:NO CONTESTAR")
        elif(17<=hora<=19):
            if(87700000<=numero<=87799999):
                print("RESULTADO: NO CONTESTAR")
            else:
                print("RESULTADO:CONTESTAR")
        else:
            print("RESULTADO:NO CONTESTAR")
