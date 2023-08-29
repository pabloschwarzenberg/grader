#calculadora
n=0
l=[]
cont=0
i=0
suma=0
may=0
while(n!=-1):
    n=int(input("Ingrese numero: "))
    if(n!=-1):
        l.append(n)
        cont=cont+1
        
if(len(l)!=0):
    print("cantidad=",len(l))
    print("suma=",sum(l))
    print("maximo=",max(l))
else:
    print("cantidad=",len(l))
    print("suma=",sum(l))
    print("maximo=nd")      