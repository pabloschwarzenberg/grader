from math import *
a = int(input("Escriba un numero natural de hasta 4 digitos: "))
if a<=9999:
    M = (a//1000)
    C = (a%1000//100)
    D = (a%100//10)
    U = (a%10//1)
    if a>=1000 and a<=9999:
        print("La descomposicion de su numero es: {0}M + {1}C + {2}D + {3}U".format(M,C,D,U))
    if a >= 100 and a<=999: 
        print("La descomposicion de su numero es: {0}C + {1}D + {2}U".format(C,D,U))
    if a >= 10 and a<=99:
        print("La descomposicion de su numero es: {0}D + {1}U".format(D,U))
    if a >= 1 and a<=9:
        print("La descomposicion de su numero es: {0}U".format(U))
        
    

else:
    print("Ingrese un numero de 4 digitos maximo")
    
