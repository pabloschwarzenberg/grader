#Descomponer un número
a = int(input("Ingrese el numero que desee descomponer:"))
while len(str(a)) > 4 or a < 1:
    a = int(input("Ingrese el numero que desee descomponer:"))
b = str(a)
if len(str(a)) == 1:
    print(b[0] + "U")
elif len(str(a)) == 2:
    print(b[0] + "D + " + b[1] + "U")
elif len(str(a)) == 3:
    print(b[0] + "C + " + b[1] + "D + " + b[2] + "U")
elif len(str(a)) == 4:
    print(b[0] + "M + " + b[1] + "C + " + b[2] + "D + " + b[3] + "U")