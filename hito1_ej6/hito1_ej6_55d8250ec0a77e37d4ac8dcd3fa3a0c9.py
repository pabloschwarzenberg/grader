#Ordenar tres números
print("Ingrese 3 números")
n1=int(input("Ingrese un número"))
n2=int(input("Ingrese un número"))
n3=int(input("Ingrese un número"))
mini=min(n1,n2,n3)
maxi=max(n1,n2,n3)
medio=(n1+n2+n3) -mini -maxi
print("Los números ordenados de mayor a menor son:{},{},{}".format(mini,medio,maxi))