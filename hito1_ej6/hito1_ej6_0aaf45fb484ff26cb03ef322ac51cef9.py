#Ordenar tres números
n1 = eval(input("Primer numero: "))
n2 = eval(input("Segundo numero: "))
n3 = eval(input("Tercer numero: "))
  
a = max(n1, n2, n3)
c = min(n1, n2, n3)
b = (n1 + n2 + n3) - c - a
  
print("Los numeros ordenados son: {}, {}, {}".format(c,b,a))
 