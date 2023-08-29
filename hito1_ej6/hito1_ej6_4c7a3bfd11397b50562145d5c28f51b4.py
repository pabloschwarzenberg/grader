#Ordenar tres números
print("ingrese tres numero que quieras ordenar")
n1=int(input("numero 1: "))
n2=int(input("numero 2: "))
n3=int(input("numero 3: "))
if(n1<=n2<=n3):
    print("su orden de menor a mayor seria ")
    print(n1,",",n2,",",n3)
elif(n1<=n3<=n2):
    print("su orden de menor a mayor seria ")
    print(n1,",",n3,",",n2)
elif(n3<=n2<=n1):
    print("su orden de menor a mayor seria ")
    print(n3,",",n2,",",n1)
elif(n3<=n1<=n2):
     print("su orden de menor a mayor seria ")
     print(n3,",",n1,",",n2)
elif(n2<=n1<=n3):
    print("su orden de menor a mayor seria ")
    print(n2,",",n1,",",n3)
elif(n2<=n3<=n1):
    print("su orden de menor a mayor seria ")
    print(n2,",",n3,",",n1)