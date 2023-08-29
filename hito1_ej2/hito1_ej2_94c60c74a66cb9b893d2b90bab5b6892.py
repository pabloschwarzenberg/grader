#Contestador de celular
      #1-Solicitar numero y hora al usuario

numero = input("Ingrese numero telefónico:")
hora = int(input("Ingrese hora de la llamada:"))

#2- Condición del problema:si la llamada ocurre entre las 0 y las 7, se debe imprimir CONTESTAR

if(hora>=0 and hora <=7):
    print("CONTESTAR")




#Extraer los ultimos tres digitos del número telefónico
    
num = numero.split()
num_antep=num[0][5]
num_penultimo=num[0][6]
num_ultimo=num[0][7]


#3-Condición del problema: Si la llamada ocurre antes de las 14 no se contesta expeto si termina en 909
if(hora<=14 and hora >7):
    
    if(num_antep=="9" and num_penultimo=="0" and num_ultimo=="9"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

#ver los primeros tres digitos del número
    
num = numero.split()
num_prim=num[0][0]
num_segundo=num[0][1]
num_tercero=num[0][2]

#4- Condición del problema: Durante la tarde solo contesto entre las 17 y 19, excepto el que comienza con 877
if(hora>14 and hora <=17):
    print("NO CONTESTAR")

if(hora>17 and hora <=19):
    
    if(num_prim=="8" and num_segundo=="7" and num_tercero=="7"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

#4- Condición del problema: Despues de las 19 horas no se contesta celular
if(hora>19 and hora <24):
    print("NO CONTESTAR")