#Descomponer un número
numero = int(input("Ingrese su numero de hasta cuatro digitos: "))

j1 = numero %10
j2 = int((numero % 100)/10)
j3 = int((numero % 1000)/100)
j4 = int((numero % 10000)/1000)


if (((j4==0) and (j3 > 0) and (j2 > 0) and (j1 > 0))):
    print (" %sC+%sD+%sU" %  (j3, j2, j1))
    

else:
    if ((j4==0) and (j3 == 0) and (j2 > 0) and (j1 > 0)):
        print (" %sD+%sU" %  (j2, j1))

    else:
        if ((j4==0) and (j3 == 0) and (j2 == 0) and (j1 > 0)):
            print (" %sU" %  ( j1))

        else:
            if ((j4==0) and (j3 == 0) and (j2 == 0) and (j1 == 0)):
                print ("TODOS LOS NUMEROS SON CERO")

            else:
                if ((j4 > 0) and (j3 > 0) and (j2 > 0) and (j1 > 0)):
                    print (" %sM+%sC+%sD+%sU" %  (j4, j3, j2, j1))
    
