#Descomponer un número
number_string=str(input("ingrese un numero"))

if len(number_string)==4:
    print(number_string[0], "M +", number_string[1], "C +", number_string[2], "D +", number_string[3], "U")
if len(number_string)==3:
    print (number_string[0], "C +", number_string[1], "D +", number_string[2], "U")
if len(number_string)==2:
    print (number_string[0], "D +", number_string[1], "U")
if len(number_string)==1:
    print ( number_string[0], "U")

