#numero primo
import random
num=int(input("Ingrese un numero: "))
if num > 1:
    cont=0
    i=2
    while i<num and cont==0:
        resto=num&i
        
        if resto==0:
            cont+=1
        i+=1
    if cont==0:
        print("El {} es un numero primo". format(num))
    else:
        print("El {} no es un numero primo".format(num))
else:
    print("El {} no es un numero primo".foemat(num))