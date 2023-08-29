#Ordenar tres números
n1= int(input("ingrese el 1er numero:"))
n2= int(input("ingrese el 2do numero:"))
n3= int(input("ingrese el 3er numero:"))

a=min(n1,n2,n3)
b=max(n1,n2,n3)
c=(n1+n2+n3)-a-b
print("los numeros de menor a mayor son:",a,",",c,",",b)