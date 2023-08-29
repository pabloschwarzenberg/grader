#Ordenar tres numeros
x = int(input("ingrese un numero: "))
y = int(input("ingrese un segundo numero: "))
z = int(input("ingrese un tercer numero: "))
Ma = max(x,y,z)
Mi = min(x,y,z)
D = (x + y + z) - Ma - Mi
print(Mi,",",D,",",Ma)