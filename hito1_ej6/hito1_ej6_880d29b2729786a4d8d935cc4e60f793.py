#entrada
x = eval(input("ingrese su primer numero: "))
y = eval(input("ingrese su segundo numero: "))
z = eval(input("ingrese su tercer numeroo: "))
#procesamiento
ma = max(x,y,z)
mi = min(x,y,z)
d = (x + y + z)-ma-mi
#salida
print("maximo y minimo", end=",")
print("el numero mayor es: ", ma, end=",")
print("el numero menor es: ", mi)
print("de menor a mayorr el orden es:",mi,";",d,",",ma)
      