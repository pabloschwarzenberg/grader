#Ordenar tres números
G = eval(input("Ingrese un numero: "))
H = eval(input("Ingrese un segundo numero: "))
L = eval(input("Ingrese un tercer numero: "))
M = max(G,H,L)
m = min(G,H,L)
r = (G + H + L) - M - m
print("De menor a mayor el órden es ", m ," , ", r , " , ", M) 

