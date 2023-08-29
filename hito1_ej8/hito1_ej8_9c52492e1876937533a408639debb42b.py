#Descomponer un número
x = int(input("Ingrese Un Digito De Cuatro Numeros"))
while len(str(x)) > 4 or x < 1:
    x = int(input("Ingrese Un Digito De Cuatro Numeros"))
xy = str(x)
if len(str(x)) == 1:
    print(xy[0] + "U")
elif len(str(x)) == 2:
    print(xy[0] + "D+" + xy[1] + "U")
elif len(str(x)) == 3:
    print(xy[0] + "C+" + xy[1] + "D+" + xy[2] + "U")
elif len(str(x)) == 4:
    print(xy[0] + "M+" + xy[1] + "C+" + xy[2] + "D+" + xy[3] + "U")