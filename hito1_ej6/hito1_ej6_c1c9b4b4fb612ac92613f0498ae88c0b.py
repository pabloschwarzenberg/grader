x=int(input("ingrese un numero"))
y=int(input("ingrese un numero"))
z=int(input("ingrese un numero"))
i=0
a=list()
lista=list()
a.append(x)
a.append(y)
a.append(z)
while i<3:
      lista.append(min(a)) 
      a.remove(min(a))
      i=i+1
print('orden',lista)