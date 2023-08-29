#Ordenar tres números
#entradas

a = int(input("ingrese primer número a evaluar: "))
b = int(input("ingrese segundo número a evaluar: "))
c = int(input("ingrese tercer número a evaluar: "))

#evaluacion
if a <= b <= c:
    print((a), ",", (b), ",", (c))

elif a <= c <= b:
    print((a), ",", (c), ",", (b))

elif b <= a <= c:
    print((b), ",", (a), ",", (c))

elif b <= c <= a:
    print((b), ",", (c), ",", (a))

elif c <= a <= b:
    print((c), ",", (a), ",", (b))

elif c <= b <= a:
    print((c), ",", (b), ",", (a))     
else:
    print("Dos o más números ingresados son iguales")