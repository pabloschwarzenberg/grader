#Juego adivina mi número
import random
# se puede ocupar libreria supongo
SN=random.randint(1,20)
intentos=5

print("buenas, tengo un numero secreto que debes adivinar, teni 5 intento sino perdí")

while(intentos>0):
    print("Intentos:",intentos)
    numero=int(input("Ingresa tu número: "))
    # IGUAL
    if(numero==SN):
        print("Adivinaste, mi número era ",SN)
        break
    # MAYOR
    elif(numero<SN):
        print("Mi número es mayor.")
    # MENOR
    elif(numero>SN):
        print("Mi número es menor.")
    # PORSIACASO
    else:
        print("Input inválido.")
    intentos-=1
else:
    print("No adivinaste, mi número era",SN)
