#Ordenar tres números
n1=int(input("Ingresa un número"))
n2=int(input("Ingresa un número"))
n3=int(input("Ingresa un número"))
menor=min(n1,n2,n3)
mayor=max(n1,n2,n3)
medio=(n1+n2+n3)-min(n1,n2,n3)-max(n1,n2,n3)
print(menor,",",medio,",",mayor)