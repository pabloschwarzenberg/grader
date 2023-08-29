#Factores Primos
#factores primos 
x=int(2)
numerop=int(input("ingrese el numero"))
while(numerop!=1):
    if (numerop%x==0):
        print(str(x)+ "")
        numerop=numerop/x
    else:
        x=x+1      