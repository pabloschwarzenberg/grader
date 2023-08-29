a=int(input("ingrese su primer numero: "))
b=int(input("ingrese su segundo numero: "))
c=int(input("ingrese su tercer numero: "))
ma=max(a,b,c)
mi=min(a,b,c)
med=(a+b+c)-ma-mi
print("de menor a mayor los numeros son: ",mi," , ", med," , ",ma)