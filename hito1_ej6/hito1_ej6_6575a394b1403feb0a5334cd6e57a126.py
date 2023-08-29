#Ordenar tres números
x = str(input('Ingrese primer numero entero:' ))
y = str(input('Ingrese segundo numero entero:' ))
z = str(input('Ingrese tercer numero entero:' ))
if x < y < z :
    Resultado1 = (x+','+y+','+z)
    print(Resultado1)
if x < z < y :
    Resultado1 = (x+','+z+','+y)
    print(Resultado1)
if y < x < z :
    Resultado1 = (y+','+x+','+z)
    print(Resultado1)
if y < z < x :
    Resultado1 = (y+','+z+','+x)
    print(Resultado1)
if z < x < y :
    Resultado1 = (z+','+x+','+y)
    print(Resultado1)
if z < y < x :
    Resultado1 = (z+','+y+','+x)
    print(Resultado1)
if x == y < z :
    Resultado1 = (x+','+y+','+z)
    print(Resultado1)
if x == z < y :
    Resultado1 = (x+','+z+','+y)
    print(Resultado1)
if y == z < x :
    Resultado1 = (y+','+z+','+x)
    print(Resultado1)
if x == z == y :
    Resultado1 = (x+','+y+','+z)
    print(Resultado1)
if x < y == z :
    Resultado1 = (x+','+y+','+z)
    print(Resultado1)
if y < x == z :
    Resultado1 = (y+','+x+','+z)
    print(Resultado1)
if z < y == x :
    Resultado1 = (z+','+y+','+x)
    print(Resultado1)
    