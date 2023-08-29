#Contestador de celular
numero=int(input("Ingrese numero telefonico:"))
hora=int(input("ingrese hora de la llamada"))

#calculo 909
x1=numero/1000
x2=str(x1).split(".")
x3=int(x2[1])


#desrrollo del programa

if(numero<10000000)or(numero>99999999):
    print("Tu número de teléfono es invalido")

elif (hora<0)or(hora>23):
    print("tu hora no es valida")

elif (hora>=0) and (hora<=7):
    print("CONTESTAR")

elif (hora<14 and hora>7 and x3==909):
    print("CONTESTAR")

elif hora<14 and hora>7:
    print("NO CONTESTAR")

elif(hora>=17 and hora<=19)and(numero>=87700000 and numero<=87799999):
    print("NO CONTESTAR")

elif (hora>=17 and hora<=19):
    print("CONTESTAR")

elif hora>19:
    print("NO CONTESTAR")     