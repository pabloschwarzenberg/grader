#Juego adivina mi número
import random
magia=random.randint(1,20)
intentos=0
while True:
    tunumero=int(input("Introduce un numero entre el 1 y el 20:"))
    if tunumero==magia:
        print("Felicidades, lo lograste")
        break
    else:
        print("Introduce tu numero otra vez")
        intentos+=5
        print("El numero de intentos es: "+str(intentos))
print("Hasta pronto")
                 

