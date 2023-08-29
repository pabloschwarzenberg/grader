var1 = int(input("ingrese numero 1 :"))
var2 = int(input("ingrese numero 2 :"))
var3 = int(input("ingrese numero 3: "))
if var1 <= var2 and var1 <=var3:
    menor = var1
    if var2<= var3:
        medio= var2
        mayor=var3
    else:
        medio= var3
        mayor= var2
elif var2 <= var1 and var2 < var3:
    menor = var2
    if var1 <= var3:
        medio = var1
        mayor = var3
    else:
        medio = var3
        mayor = var1
else:
    menor= var3
    if var1 <= var2:
        medio= var1
        mayor= var2
    else:
        medio= var2
        mayor = var1
print(int(menor),",", int(medio),",",int(mayor))