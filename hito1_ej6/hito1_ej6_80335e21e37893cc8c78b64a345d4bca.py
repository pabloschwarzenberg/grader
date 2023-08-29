#Ordenar tres números
x = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
a = int(input("ingrese el tercer numero: "))
#procesamiento
if (x < b < a):
menor = x
medio = b
mayor = a
else: 
mayor = b
medio = a
elif (b < x < a):
menor = b 
if (x < a):
medio = x
mayor = a
else: 
menor = a
if (x < b):
medio = x
mayor = b
else:
medio = b
mayor = a
#salida
print("el orden de menor a mayor es: (menor),(medio),(mayor)")
      
      
      
    