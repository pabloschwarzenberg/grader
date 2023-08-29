#Descomponer un número
number = input("Escribe un numero con un maximo de 4 digitos: ")
largo = len(number)

if largo == 1:
    print(number, "U")
elif largo == 2:
    print(number[0], "D +", number[1], "U")
elif largo == 3:
    print(number[0], "C +", number[1], "D +", number[2], "U")
elif largo ==4:
    print(number[0], "M +", number[1], "C +", number[2], "D+", number[3], "U")      