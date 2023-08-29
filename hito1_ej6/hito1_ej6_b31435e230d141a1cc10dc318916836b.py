#Ordenar tres números
print("ingrese sus numeros:")
a= int(input("primer numero: "))
b= int(input("segundo numero: "))
c= int(input("tercer numero: "))

mayor = max(a,b,c)
menor = min(a,b,c)
d= (a + b + c) - mayor - menor
print("ordenados de menor a mayor es: " , menor,", ", d, ", ", mayor)