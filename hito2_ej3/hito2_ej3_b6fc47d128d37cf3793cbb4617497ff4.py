a=str(input("Ingrese una palabra:"))
b=int(input("Ingrese un numero"))
c=list(a)
contador=0
contador2=0
while contador+3<=len(a):
    d=c[contador:contador+b]
    e="".join(d)
    z=a.replace(e,"")
    f=a.find(e,contador+b)
    
    if f<0 and len(z)!=0:
        contador2+=0
        print(e)
    contador+=1
if contador2==0:
    print("ninguna")
    
    
    
    

