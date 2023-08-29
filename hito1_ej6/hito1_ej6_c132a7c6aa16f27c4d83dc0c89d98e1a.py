#Ordenar tres números
v1= int(input("ingrese primer numero:"))
v2= int(input("ingrese un segundo numero:"))
v3= int(input("ingrese un tercer numero:"))
m1= max(v1,v2,v3)
m2= min(v1,v2,v3)
m3= (v1 + v2 + v3) - m1 - m2
print("el orden de menor a mayor es ", m2, " , " , m3, " , ", m1)