#Ordenar tres números
a=int(input("escriba el primer numero "))
b=int(input("escriba el segundo numero "))   
c=int(input("escriba el tercer numero "))
d=max(a,b,c)
e=min(a,b,c)
f=(a+b+c)-e-d
print(e, "," ,f, "," ,d)