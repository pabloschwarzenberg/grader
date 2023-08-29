#calculadora
l=[]
while True:
    p=int(input("ingrese numero:"))
    if p!=-1:
        print("ingrese -1 para terminar")
    l.append(p)
    

    if p==-1:
        l.remove(-1)
        print("cantidad=",len(l))
        print("suma=",sum(l))
        if max(l)<1:
            print("maximo=nd")
        else:
            print("maximo=",max(l))
        print("fin")
        break

  
       


