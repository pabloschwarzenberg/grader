#Ordenar tres números
a = int(input("Primero numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))
d = min(a,b,c)
e = max(a,b,c)
f = (a+b+c)-d-e
print( '{},{},{}'.format(d,f,e))