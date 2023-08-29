#Ordenar tres números

a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))
z=min(a,b,c)#menor
x=max(a,b,c)#mayor
y= (a + b + c) - z - x #en medio
print("",z,",",y,",",x,)
