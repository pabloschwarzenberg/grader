#calculadora
nt=[]
cantidad=0
n=0
maximo=0
suma=0
while n!=-1:
    n=int(input("ingrese un número:"))
    if n!=-1:
        nt.append(n)
for n1 in nt:
    suma+=n1
if len(nt)>0:
    print("cantidad=", len(nt))
    print("suma=", suma)
    print("maximo=", max(nt))
else:
    print("maximo=nd")
    print("cantidad=0")
    print("suma=0")
