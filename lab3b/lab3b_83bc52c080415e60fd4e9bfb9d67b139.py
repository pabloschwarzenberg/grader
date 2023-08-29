#calculadora
l=[]
while True:
    n=int(input('Ingrese un numero:'))
    if n==-1:
        break
    print (n)
    l.append(n)

     
if len(l)>0:
    print("cantidad=",len (l))
    print("suma=",sum(l))
    print("maximo=",max(l))

if len(l)==0:
    print ("cantidad=0")
    print ("suma=0")
    print ("maximo=nd")      