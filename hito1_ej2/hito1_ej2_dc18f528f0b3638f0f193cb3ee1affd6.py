#Contestador de celular
celular = 0;
hora=0;
aula = True

while(aula):
    celular = input("Ingrese numero de Celular")
    
    if (len(celular) < 8) or (len(celular) > 8):
        aula = True
        print("Celular debe tener un largo de 8 digitos\n")
    else:
        aula = False
        break

aula= True
while(aula):
    print ("\n Ingrese hora de la llamada")
    hora = int(input())
    
    if (hora < 0) or (hora > 23):
        aula = True
        print("Hora debe ser de 0 a 23")
    else:
        aula = False
        break

if( (hora >= 0) and (hora <= 7 ) ):
        print ("Resultado: CONTESTAR")
elif((hora <= 14 ) and (hora > 7 ) ):
        celularString = str(celular)
        ultimosdigitos = celularString[5:7]
        if(ultimosdigitos == "909"):
            print("Resultado: NO CONTESTAR")

        else:
            print("Resultado: CONTESTAR")


elif((hora >= 17 ) and (hora <= 19 ) ):
    celularString = str(celular)
    primeroDigitos = celularString[0:2]

    if(primeroDigitos == "877"):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")

elif((hora > 19 ) and (hora < 23 ) ):
    print("Resultado: NO CONTESTAR")

elif((hora > 14 ) and (hora < 17 ) ):
    print("Resultado: INDEFINIDO")
      