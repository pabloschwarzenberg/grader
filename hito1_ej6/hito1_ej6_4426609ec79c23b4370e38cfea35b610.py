#Ordenar tres números enteros
print("escoge 3 numeros")
a = int(input())
b = int(input())
c = int(input())
#ordenar de menor a mayor
if(a >= b)and (a >= c):
    
    if(c > b):
        print(str(b)+","+ str(c)+","+ str(a))
    else:
        print(str(c)+","+ str(b)+","+str(a))

if(b > a)and (b > c):
    
    if(c > a):
        print(str(a)+","+str(c)+","+str(b))
    else:
        print(str(c)+","+ str(a)+","+ str(b))
    
if(c >= b)and (c > a):
    
    if(a > b):
        print(str(b)+","+ str(a)+","+ str(c))
    else:
        print(str(a)+","+str(b)+","+ str(c))      