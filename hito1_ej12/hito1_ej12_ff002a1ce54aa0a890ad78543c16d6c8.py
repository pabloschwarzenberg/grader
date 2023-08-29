#Juego adivina mi número
print("Adivina mi número")
import random
numero_aleatorio=random.randint(1,20)
print(numero_aleatorio)
intentos=5
while intentos>0:
    N=input("Ingrese su número: ")
    N=int(N)
    if(numero_aleatorio<N):
        intentos=intentos-1
        print('el numero que ingresaste es mayor')
    elif(numero_aleatorio>N):
        intentos=intentos-1
        print("el número que ingresaste es menor")
    elif(numero_aleatorio==N):
        print("número correcto")
        break
if(numero_aleatorio!=N):
    print("No adivinaste, mi número era: ",numero_aleatorio)
    
                   
    
    


    
