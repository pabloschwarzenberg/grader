#Ordenar tres números
a = int(input("Introduzca su primer numero: "))
b = int(input("Introduzca su segundo numero: "))
c = int(input("Introduzca su tercer numero: "))

minimo  = min(a , b , c)
maximo  = max(a , b , c)
intermedio = (a + b + c) - minimo - maximo

print("los numeros de menor a mayor son : {},{},{}" .format(minimo,intermedio,maximo))