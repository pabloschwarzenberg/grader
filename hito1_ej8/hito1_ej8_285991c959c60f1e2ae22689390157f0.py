#Descomponer un número
 
while True:
    n=int(input("Ingrese numero a descomponer:"))
    if(0<=n<=9999):
        break
    else:
        print("ingrese numero de maximo 4 cifras")


if(0<=n<=9):
    n1=str(n)[0]
    print(n1,"U")
    
elif(10<=n<=99):
    n1=str(n)[0]
    n2=str(n)[1]
    print(n1,"D +",n2,"U")
    
elif(100<=n<=999):
    n1=str(n)[0]
    n2=str(n)[1]
    n3=str(n)[2]
    print(n1,"C +",n2,"D +",n3,"U")
    
elif(1000<=n<=9999):
    n1=str(n)[0]
    n2=str(n)[1]
    n3=str(n)[2]
    n4=str(n)[3]
    print(n1,"M +",n2,"C +",n3,"D +",n4,"U")
     