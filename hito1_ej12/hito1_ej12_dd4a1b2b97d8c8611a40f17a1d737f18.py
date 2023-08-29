#Juego adivina mi número
import random
secreto=random.randint(1,20)
intentos=0

while intentos<=5:
    mi_numero=int(input("Ingrese numero: "))
    if mi_numero<secreto:
        print("El numero que pusiste es menor al secreto")
        intentos+=1
    if mi_numero>secreto:
        print("El numero que pusiste es mayor al secreto")
        intentos+=1
    if mi_numero!=secreto and intentos==5:
        print("No adivinaste, mi numero era",secreto)
        break
    
    if mi_numero==secreto:
        print("Adivinaste, mi numera era",secreto)
        break      