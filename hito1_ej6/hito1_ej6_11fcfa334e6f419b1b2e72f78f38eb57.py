#Ordenar tres números
   n1=int(input("Numero 1: ")) 
n2=int(input("Numero 2: "))
n3=int(input("Numero 3: ")) 
if (n1<n2 and n2<n3):
    print(n1,"\n",n2,"\n",n3)
elif(n2<n1 and n2<n3):
    print(n2,"\n",n1,"\n",n3)
elif(n3<n2 and n2<n1):
    print(n3,"\n",n2,"\n",n1)
elif(n1<n3 and n3<n2):
    print(n1,"\n",n3,"\n",n2)
elif(n3<n1 and n1<n2):
    print(n3,"\n",n1,"\n",n2)
elif(n2<n3 and n3<n1):
    print(n2,"\n",n3,"\n",n1)
elif(n1 == n2 and n2 == n3):
    print("todos son iguales")   