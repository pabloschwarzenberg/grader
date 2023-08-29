n1=int(input("escriba un numero: "))
n2=int(input("escriba otro numero: "))
n3=int(input("escriba otro numero: "))

if n1<n2<n3:
    print("los numeros ordenados de menor a mayor son", n1, n2, n3)
elif n1<n3<n2:
    print("los numeros ordenados de menor a mayor son", n1, n3, n2)
elif n3<n2<n1:
    print("los numeros ordenados de menor a mayor son", n3, n2, n1)
elif n2<n3<n1:
    print("los numeros ordenados de menor a mayor son", n2, n3, n1)
elif n2<n1<n3:
    print("los numeros ordenados de menor a mayor son", n2, n1, n3)
elif n3<n2<n1:
    print("los numeros ordenados de menor a mayor son", n3, n1, n2)
else:
    print("se ingrearon numeros iguales")