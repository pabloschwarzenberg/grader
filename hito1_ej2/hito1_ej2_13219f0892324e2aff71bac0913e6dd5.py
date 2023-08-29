#Contestador de celular
import math
numero_telefonico=int(input("ingrese numero telefonico: "))
hora=int(input("ingrese hora: "))
ultimos_numeros=numero_telefonico % 1000
primeros_numeros=numero_telefonico // 10 ** (int(math.log(numero_telefonico, 10)) - 3 + 1)
if hora <=7 and hora >= 0:
    print("contestar")
elif hora <= 14 and ultimos_numeros==909:
    print("contestar")
elif hora <= 14:
    print("no contestar")
elif 17 <= hora and hora <= 19 and primeros_numeros==877:
    print("no contestar")
elif hora >= 17 and hora <= 19:
    print("contestar")
elif 19 <= hora:
    print("no contestar")
    