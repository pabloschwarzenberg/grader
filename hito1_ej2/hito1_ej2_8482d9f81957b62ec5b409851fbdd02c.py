numero= str(input("ingrese su número telefónico: "))
hr= int(input("ingrese la hora en que se registra su llamada: "))

if (0 <= hr <= 7):
    print("contestar")

elif (14 <= hr <= 16):
    print("no contestar")

elif (8 <=  hr <=14 ):
    if str(numero[-3]) == "9" and str(numero[-2]) == "0" and str(numero[-1]) == "9":
        print("contestar")
    else:
        print("no contestar")
    

elif(17 <= hr <= 19 ):
    if str(numero[-3]) == "8" and str(numero[-2]) == "7" and str(numero[-1]) == "7":
        print("contestar")
    else:
        print("no contestar")

elif( 20 <= hr ):
    print ("no contestar")

else:
    print("no contestar")



  


                

    