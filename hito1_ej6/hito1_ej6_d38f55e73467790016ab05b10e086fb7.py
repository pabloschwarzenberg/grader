#Pedir Numeros#

numero_1 = int(input("Ingrese numero 1: "))
                
numero_2 = int(input("Ingrese numero 2: "))

numero_3 = int(input("Ingrese numero 3: "))

if numero_1 < numero_2 and numero_1 < numero_3 and numero_2 < numero_3:
    resultado = numero_1, numero_2, numero_3

elif numero_2 < numero_1 and numero_2 < numero_3 and numero_1 < numero_3:
    resultado = numero_2, numero_1, numero_3

elif numero_1 < numero_3 and numero_1 < numero_2 and numero_3 < numero_2:
    resultado = numero_1, numero_3, numero_2

elif numero_2 < numero_3 and numero_2 < numero_1 and numero_3 < numero_1:
    resultado = numero_2, numero_3, numero_1

elif numero_3 < numero_1 and numero_3 < numero_2 and numero_1 < numero_2:
    resultado = numero_3, numero_1, numero_2

else:
    resultado = numero_3, numero_1, numero_2


print(resultado)