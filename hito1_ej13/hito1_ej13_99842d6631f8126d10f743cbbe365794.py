#Factores Primos
p=int(2)
nr=int(input("ingrese numero:"))

while (nr!=1):
   if(nr%p==0):
       print(str(p)+" ")
       nr=nr/p
   else:
       p=p+1
