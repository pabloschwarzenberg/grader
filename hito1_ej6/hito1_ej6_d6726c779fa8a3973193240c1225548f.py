#Ordenar tres números
#entrada 
p1 = int(input(" ingrese su primer numero: "))
p2 = int(input(" ingrese su segundo numero: "))
p3 = int(input(" ingrese su tercer numero: "))
#desarrollo
a = min(p1,p2,p3)
b = max(p1,p2,p3)
c = (p1 + p2 + p3)- a - b
#salida
print("la repuesta es: {}, {}, {}".format(a, c, b))