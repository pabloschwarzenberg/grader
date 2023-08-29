#Descomponer un número
x= int(input("Ingrese un número de hasta 4 digitos:"))
while len(str(x))>4 or x<1:
    x= int(input("Ingrese un número de hasta 4 digitos:"))
char= str(x)
if len(str(x)) == 1:
    print(char[0] + "U")
elif len(str(x)) == 2:
    print(char[0] + "D + " + char[1] + "U")
elif len(str(x)) == 3:
    print(char[0] + "C + " + char[1] + "D + " + char[2] + "U")
elif len(str(x)) == 4:
    print(char[0] + "M + " + char[1] + "C + " + char[2] + "D + " + char[3] + "U")