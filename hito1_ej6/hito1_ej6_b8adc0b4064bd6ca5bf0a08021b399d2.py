x1 = eval(input("ingrese primer digito: "))
x2 = eval(input("ingrese segundo digito: "))
x3 = eval(input("ingrese tercer digito: "))
MAYOR = 0
MENOR = 0
INTERMEDIO = 0
if (x1 >= x2 and x1 >= x3):
    MAYOR = (x1)
if (x2 >= x1 and x2 >= x3):
    MAYOR = str(x2)
if (x3 >= x1 and x3 >= x2):
    MAYOR = x3

if (x1 <= x2 and x1 <= x3):
    MENOR = x1
if (x2 <= x1 and x2 <= x3):
    MENOR = x2
if (x3 <= x1 and x3 <= x2):
    MENOR = x3

if (x1 <= x2 and x1 >= x3) or (x1 >= x2 and x1 <= x3):
    INTERMEDIO = x1
if (x2 <= x1 and x2 >= x3) or (x2 >= x1 and x2 <= x3):
    INTERMEDIO = x2
if (x3 <= x1 and x3 >= x2) or (x3 >= x1 and x3 <= x2):
    INTERMEDIO = x3

print("{},{},{}".format(MENOR, INTERMEDIO, MAYOR))