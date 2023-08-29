#calculadora
n=0
x=[]
i=0
while i!=-1:
    i=int(input("ingrese valor: "))
    if  i!=-1:
        x.append(i)
print("suma=",sum(x))
print("cantidad=",len(x))
if len(x)==0:
      print("valor maximo=nd")
else: 
    print("valor maximo=",max(x))