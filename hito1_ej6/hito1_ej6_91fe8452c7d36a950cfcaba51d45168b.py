#Ordenar tres números
n1=int(input("ingrese primer numero:"))
n2=int(input("ingrese segundo numero:"))
n3=int(input("ingrese tercer numero:"))
menor=min(n1,n2,n3)
mayor=max(n1,n2,n3)
resultado=(n1+n2+n3)-mayor-menor
print("el orden de las variables de menor a mayor es:",menor,",",resultado,",",mayor)