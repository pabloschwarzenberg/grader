#Ordenar tres números
a= int(input("numero:"))
b= int(input("numero:"))
c= int(input("numero:"))

x=max (a,b,c)
y=min (a,b,c)
d=( a + b + c )-x-y

print(y,",",d,",",x) 
