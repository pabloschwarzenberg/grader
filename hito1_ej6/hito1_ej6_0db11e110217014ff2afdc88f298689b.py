#Ordenar tres números
a=int(input("Primer numero: "))
b=int(input("Segundo numero: "))
c=int(input("Tercer numero: "))
if((a<b) and (a<c)):
    if(b<c):
        print(str(a)+","+str(b)+","+str(c))
    else:
        print(str(a)+","+str(c)+","+str(b))
if((b<a) and (b<c)):
    if(a<c):
        print(str(b)+","+str(a)+","+str(c))
    else:
        print(str(b)+","+str(c)+","+str(a))
if((c<a) and (c<b)):
    if(a<b):
        print(str(c)+","+str(a)+","+str(b))
    else:
        print(str(c)+","+str(b)+","+str(a))
            