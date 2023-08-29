a= int(input("ingrese numero entero "))
b= int(input("ingrese numero entero "))
c= int(input("ingrese numero entero "))
if(a<=b and a<=c):
        p=a
        if(b<=c):
                m=b
                g=c
        else:
                m=c
                g=b
elif(b<=a and b<c):
        p=b
        if(a<=c):
                m=a
                g=c
        else:
                g=a
                m=c
else:
        p=c
        if(a<=b):
                m=a
                g=b
        else:
                m=b
                g=a
print(p,",", m,",", g)