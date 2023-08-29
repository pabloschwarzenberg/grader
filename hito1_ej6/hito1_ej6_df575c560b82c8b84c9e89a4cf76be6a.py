#Ordenar tres números
a=int(input("Ingrese primer número:"))
b=int(input("Ingrese segundo número:"))
c=int(input("Ingrese tercer número:"))
if ((a <= c) and (c<b)):
    print("Ordenados de menor a mayor quedan:",(a,c,b))
elif ((a <= b) and (b<c)):
    print("Ordenados de menor a mayor quedan:",(a,b,c))
elif ((b <= a) and (a<c)):
    print("Ordenados de menor a mayor quedan:",(b,a,c))
elif ((a>b) and (b <= c)):
    print("Ordenados de menor a mayor quedan:",(b,c,a))
elif ((c <= a) and (a<b)):
    print("Ordenados de menor a mayor quedan:",(c,a,b))
elif ((c <= b) and (b<a)):
    print("Ordenados de menor a mayor quedan:",(c,b,a))
elif ((c==b) and (b==a)):
    print("Ordenados de menor a mayor quedan:",(c,b,a))
elif ((a<b) and (b==c)):
    print("Ordenados de menor a mayor quedan:",(a,b,c))
elif ((a<c) and (c==b)):
    print("Ordenados de menor a mayor quedan:",(a,b,c))
    
