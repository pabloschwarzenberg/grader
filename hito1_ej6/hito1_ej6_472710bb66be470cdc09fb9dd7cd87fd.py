A = int(input("Ingrese su primer numero: "))
G = int(input("Ingrese su segundo numero: "))
H = int(input("Ingrese su tercer numero: "))

numero_mayors = max(A,G,H)
print("el número mayor es: ", numero_mayors)
numero_menors = min(A,G,H)
print("el número menor es: ", numero_menors)

V = (A + G + H) - numero_mayors - numero_menors

print("De menor a mayor el órden es ", numero_menors  ," , ", V , " , ", numero_mayors) 
