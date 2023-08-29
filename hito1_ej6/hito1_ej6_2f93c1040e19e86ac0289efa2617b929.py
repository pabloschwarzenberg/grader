#Ordenar tres números
var1=int(input("ingrese un numero: "))
var2=int(input("ingrese un numero: "))
var3=int(input("ingrese un numero: "))
   
varm=min(var1, var2, var3)
varM=max(var1, var2, var3)
varMe=(var1 + var2 + var3) - varm - varM

print("{},{},{}".format(varm,varMe,varM))