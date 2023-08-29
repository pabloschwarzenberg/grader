numero = 0
numerostr = "a"
while numero < 99 or numero < 999 or numero > 9999:
    numero = int(input("Dime un numero milesimo: "))
    numerostr = str(numero)


print(numerostr [0],"M+" ,numerostr [1],"C+",numerostr [2],"D+",numerostr[3],"U+")