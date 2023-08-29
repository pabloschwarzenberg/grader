#Ordenar tres números
p = int(input("Ingrese el primer numero: "))  
q = int(input("Ingrese el segundo numero: ")) 
r = int(input("Ingrese el tercer numero: ")) 

a = min(p, q, r) 
c = max(p, q, r) 
b = (p + q + r) - a - c 
print("Los numeros ordenados son: {}, {}, {}".format(a, b, c))
