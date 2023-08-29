# Ejemplo 1
numero1 = 77389909
hora1 = 13

if hora1 >= 0 and hora1 <= 7:
    resultado1 = "CONTESTAR"
elif hora1 < 14 and numero1 % 100 == 909:
    resultado1 = "CONTESTAR"
elif hora1 >= 17 and hora1 <= 19 and numero1 // 10000000 == 877:
    resultado1 = "CONTESTAR"
else:
    resultado1 = "NO CONTESTAR"

print("Ejemplo 1:")
print("Número telefónico:", numero1)
print("Hora de la llamada:", hora1)
print("Resultado:", resultado1)


# Ejemplo 2
numero2 = 98927674
hora2 = 20

if hora2 >= 0 and hora2 <= 7:
    resultado2 = "CONTESTAR"
elif hora2 < 14 and numero2 % 100 == 909:
    resultado2 = "CONTESTAR"
elif hora2 >= 17 and hora2 <= 19 and numero2 // 10000000 == 877:
    resultado2 = "CONTESTAR"
else:
    resultado2 = "NO CONTESTAR"

print("\nEjemplo 2:")
print("Número telefónico:", numero2)
print("Hora de la llamada:", hora2)
print("Resultado:", resultado2)


# Ejemplo 3
numero3 = 87765545
hora3 = 18

if hora3 >= 0 and hora3 <= 7:
    resultado3 = "CONTESTAR"
elif hora3 < 14 and numero3 % 100 == 909:
    resultado3 = "CONTESTAR"
elif hora3 >= 17 and hora3 <= 19 and numero3 // 10000000 == 877:
    resultado3 = "CONTESTAR"
else:
    resultado3 = "NO CONTESTAR"

print("\nEjemplo 3:")
print("Número telefónico:", numero3)
print("Hora de la llamada:", hora3)
print("Resultado:", resultado3)
