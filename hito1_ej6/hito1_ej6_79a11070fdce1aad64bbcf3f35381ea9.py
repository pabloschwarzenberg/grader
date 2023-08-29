#Ordenar tres números
n=int(input("Primer numero entero, "))
b=int(input("Segundo numero entero, "))
m=int(input("tercer numero entero, "))

Ma=max(n,b,m)
Mi=min(n,b,m)
Mx=(n+b+m)-Ma-Mi

print("de menor a mayor es",Mi,",",Mx,",",Ma)
