print("Ordenar de menor a mayor")
n1=input("Inserte el numero 1: ")
n2=input("Inserte el numero 2: ")
n3=input("Inserte el numero 3: ")
if(n1<=n2<=n3):
    print(str(n1)+","+str(n2)+","+str(n3))
elif(n1<=n3<=n2):
    print(str(n1) + "," + str(n3) + "," + str(n2))
elif(n2<=n1<=n3):
    print(str(n2) + "," + str(n1) + "," + str(n3))
elif(n2<=n3<=n1):
    print(str(n2) + "," + str(n3) + "," + str(n1))
elif(n3<=n2<=n1):
    print(str(n3) + "," + str(n2) + "," + str(n1))
elif(n3<=n1<=n2):
    print(str(n3) + "," + str(n1) + "," + str(n2))