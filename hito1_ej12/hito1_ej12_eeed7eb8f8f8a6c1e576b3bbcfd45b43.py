#Juego adivina mi número
import random
var_NumSecreto = random.randint(1, 20)
print(var_NumSecreto)
for k in range (0, 5):
    var_Numero = int(input("Ingrese número secreto: "))
    if var_Numero > var_NumSecreto:
        print("mi número es menor")
    elif var_Numero < var_NumSecreto:
        print("mi número es mayor")
    elif var_Numero == var_NumSecreto:
        print("Adivinaste, mi número era " + str(var_NumSecreto))
        break
else:
    print("No adivinaste, mi número era " + str(var_NumSecreto))