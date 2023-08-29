l=[]
p=0
while True:
    try:
        n=int(input("Ingrese un numero: "))
        if(n==-1):
            break
    except ValueError:
        print("Debe ser numerico")
    l.append(n)
for x in l:
    p+=int(x)
if(len(l)>0):
    print("cantidad=",len(l))
    print("suma=",p)
    print("maximo=",max(l))
else:
    print("cantidad=",len(l))
    print("suma=0")
    print("maximo=nd")