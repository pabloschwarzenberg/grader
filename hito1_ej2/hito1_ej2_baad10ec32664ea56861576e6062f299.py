#Contestador de celular
numero_telefono = int(input("Ingrese numero telefonico :"))
hora = int(input("Ingrese hora de llamada entre (0 y 23) hrs :"))
cadena = str(numero_telefono)
largo = len(cadena)
resto = largo -3
ini = ""
fin = ""
if(largo > 3 and largo < 9):
    ini = cadena[0:3]
    fin = cadena[resto:largo]    
    if((hora>=0) and (hora <=7)):  
        print("CONTESTAR")
    elif((hora > 7) and (hora < 15)):
        if(fin == "909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif(hora >= 17 and hora <= 19):
         if(ini == "877"):
             print("NO CONTESTAR")
         else:    
             print("CONTESTAR")
    elif(hora>19):
         print("NO CONTESTAR")
else:
    print("NO CONTESTAR")

print("fin del programa .....")