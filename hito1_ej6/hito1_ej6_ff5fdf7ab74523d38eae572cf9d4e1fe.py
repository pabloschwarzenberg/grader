#Ordenar tres números
n1=int(input("Ingresar: "))

n2=int(input("Ingresar: "))

n3=int(input("Ingresar: "))

num=[]
num.append(n1)
num.append(n2)
num.append(n3)
num.sort(reverse=False)
ero=[]
for elem in num:
  ero.append(str(elem))
  ero.append(",")
ero="".join(ero)
print (ero)
