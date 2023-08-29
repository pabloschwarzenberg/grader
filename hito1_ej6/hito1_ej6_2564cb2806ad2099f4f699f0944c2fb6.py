#Ordenar tres números
a=int(input("Insertar primer número:"))
b=int(input("Insertar segundo número:"))
c=int(input("Insertar tercer número:"))
if(a<=b<=c):print(str(a)+","+str(b)+","+str(c))
else:
    if(b<=c<=a):print(str(b)+","+str(c)+","+str(a))
    else:
        if(c<=a<=b):print(str(c)+","+str(a)+","+str(b))
        else:
            if(a<=c<=b):print(str(a)+","+str(c)+","+str(b))
            else:
                if(b<=a<=c):print(str(b)+","+str(a)+","+str(c))
                else:
                    if(c<=b<=a):print(str(c)+","+str(b)+","+str(a))
            
      