A = eval(input("Ingrese un número: "))
B = eval(input("Ingrese un segundo número: "))
C = eval(input("Ingrese un tercer número: "))
Maximo = max(A,B,C)
Minimo = min(A,B,C)
D = (A + B + C) - Maximo - Minimo
print("el órden es ", Minimo ," , ", D , " , ", Maximo)