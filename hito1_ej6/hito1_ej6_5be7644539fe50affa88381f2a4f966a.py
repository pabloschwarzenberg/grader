#Ordenar tres números
var1 = int(input("ingrese un numero: "))
var2 = int(input("ingrese un numero: "))
var3 = int(input("ingrese un numero: "))
a = min(var1,var2,var3)
c = max(var1,var2,var3)
b = (var1 + var2 + var3) - a - c
print( a, "," ,b, "," ,c)