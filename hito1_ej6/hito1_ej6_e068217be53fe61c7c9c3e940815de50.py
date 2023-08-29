n1 = int(input("ingrese un numero :"))
n2 = int(input("ingrese un numero :"))
n3 = int(input("ingrese un numero :"))

if(n1 < n2) and (n2 < n3):
    print(n1, ",", n2, ",", n3)
elif (n2 < n1) and (n1 < n3):
    print(n2, ",", n1, ",", n3)
elif (n3 < n1) and (n2 < n1):
    print(n3, ",", n2, ",", n1)
elif (n1==n3) and (n2<n3 or n2 <n1):
    print(n2,",",n1,",",n3)
elif(n1==n2) and (n3<n1 or n3 <n2):
    print(n3,",",n2,",",n1)
elif(n2==n3) and (n1<n2 or n1<n3):
    print(n1,",",n2,",",n3) 
elif(n1>=n2)and(n1>= n3):
    print(n2,",", n1,",", n3) 