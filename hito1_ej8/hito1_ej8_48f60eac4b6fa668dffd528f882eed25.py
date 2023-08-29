#Descomponer un número
number = int(input(" ingrese un numero para ser descompuesto: "))
number = [int(d) for d in str(number)]
counter = 0

if (len(number) == 4 ):
    print(str(number[0]) + "M + " + str(number[1]) + "C + " + str(number[2]) + "D + " + str(number[3]) + "U")
elif (len(number) == 3):
    print(str(number[0]) + "C +" + str(number[1]) + "D + " + str(number[2]) + "U")
elif (len(number) == 2):
    print(str(number[0]) + "D +" + str(number[1]) + "U")
elif (len(number) == 1):
    print(str(number[0]) + "U")