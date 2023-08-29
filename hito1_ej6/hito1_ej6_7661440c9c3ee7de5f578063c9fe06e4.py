#Ordenar tres números
#Definir que variables usaremos
a1 = int(input("ingrese un primer numero:"))
a2 = int(input("ingrese un segundo numero:"))
a3 = int(input("ingrese un tercer numero:"))
#ordenar el minimo y el maximo
x = min(a1 ,a2 ,a3)
y = max(a1, a2, a3)
#el de en medio
z = (a1 + a2 + a3) - x - y
#imprimir el orden
#print("el menor numero ingresado es:", x, "el de en medio es:", z, "y el mayor es:", y)
print(x,",",z,"," ,y,)
      