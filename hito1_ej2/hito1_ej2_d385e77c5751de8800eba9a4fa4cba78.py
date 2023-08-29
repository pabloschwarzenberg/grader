#Contestador de celular
telefono = int(input("ingrese numero de telefono: "))
hora = int(input("hora de la llamada: "))

terminaEn = telefono % 10**3
telefono_texto = str(telefono)
comienzaEn = telefono_texto[0:3]

if(hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif(hora > 7 and hora <=14):
    if(terminaEn == 909):
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif(hora >= 17 and hora <= 19):
    if(comienzaEn == "877"): 
        print('NO CONTESTAR')
    else:
        print('CONTESTAR') 
elif(hora > 19):
    print('NO CONTESTAR')      