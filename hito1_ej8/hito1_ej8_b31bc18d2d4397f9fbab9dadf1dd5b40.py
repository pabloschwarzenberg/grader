numero = int(input("Ingrese su numero de hasta cuatro digitos: "))

x1 = numero %10
x2 = int((numero % 100)/10)
x3 = int((numero % 1000)/100)
x4 = int((numero % 10000)/1000)


if (((x4==0) and (x3 > 0) and (x2 > 0) and (x1 > 0))):
    print (" %sC+%sD+%sU" %  (x3, x2, x1))
    

else:
    if ((x4==0) and (x3 == 0) and (x2 > 0) and (x1 > 0)):
        print (" %sD+%sU" %  (x2, x1))

    else:
        if ((x4==0) and (x3 == 0) and (x2 == 0) and (x1 > 0)):
            print (" %sU" %  ( x1))

        else:
            if ((x4==0) and (x3 == 0) and (x2 == 0) and (x1 == 0)):
                print ("TODOS LOS NUMEROS SON CERO")

            else:
                if ((x4 > 0) and (x3 > 0) and (x2 > 0) and (x1 > 0)):
                    print (" %sM+%sC+%sD+%sU" %  (x4, x3, x2, x1))