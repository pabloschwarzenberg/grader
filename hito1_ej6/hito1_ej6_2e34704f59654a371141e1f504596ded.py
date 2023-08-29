#Ordenar tres números
n1=int(input("ingrese un numero"))
n2=int(input("ingrese segundo numero"))
n3=int(input("ingrese tercer numero"))
if(n1<=n2<=n3):
    print("el orden de menor a mayor",[n1,n2,n3])
elif(n1<=n3<=n2):
    print("el orden de mayor a menor es",[n1,n3,n2])
elif (n2 <= n1 <= n3):
    print("el orden de mayor a menor es", [n2, n1, n3])
elif(n2<=n3<=n1):
    print("el orden de mayor a menor es",[n2,n3,n1])
elif(n3<=n1<=n2):
    print("el orden de mayor a menor es",[n3,n1,n2])
elif (n3<=n2<=n1):
    print("el orden de mayor a menor es", [n3, n2, n1])