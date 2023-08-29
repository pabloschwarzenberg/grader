#Ordenar tres números
n1=int(input("ingrese el primer numero"))
n2=int(input("ingrese el segundo numero"))
n3=int(input("ingrese el tercero numero"))
mn=min(n1,n2,n3)
mx=max(n1,n2,n3)
medio = (n1+n2+n3)-mn-mx
print(mn,medio,mx)

    