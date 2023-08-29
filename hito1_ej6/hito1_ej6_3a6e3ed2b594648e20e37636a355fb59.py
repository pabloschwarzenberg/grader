n1= int(input("ingrese el primer numero :"))

n2= int(input("ingrese el segundo numero :")) 

n3= int(input("ingrese el treser numero :"))

if ((n1 <= n2) and (n2 <= n3)):
    print (n1, n2, n3)

if ((n2 <= n1) and (n1 <= n3)):
    print (n2, n1, n3)

if ((n3 <= n1 and n2 ) and (n2 <= n1)):
    print(n3, n2,n1)   
    
    