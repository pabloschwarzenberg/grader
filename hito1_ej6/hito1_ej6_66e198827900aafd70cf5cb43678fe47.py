#Ordenar tres número
n1=int(input("ingrese cualquier numero"))
n2=int(input("ingrese otro numero"))
n3=int(input("ingrese otro numero"))
a=min(n1,n2,n3)
c=max(n1,n2,n3)
b=(n1+n2+n3)-a-c
print("los numeros ordenados son:{},{},{}".format(a,b,c))