numero = (input("Ingrese un numero de maximo 4 digitos: "))

x = []
for n in numero:
    x.append(n)

letras = ("M", "C", "D", "U")

if len(x) == 4:
    print((x[0]+letras[0]),"+",(x[1]+letras[1]),"+",(x[2]+letras[2]),"+",(x[3]+letras[3]))

if len(x) == 3:
    print((x[0]+letras[1]),"+",(x[1]+letras[2]),"+",(x[2]+letras[3]))

if len(x) == 2:
    print((x[0]+letras[2]),"+",(x[1]+letras[3]))

if len(x) == 1:
    print((x[0]+letras[3]))

      