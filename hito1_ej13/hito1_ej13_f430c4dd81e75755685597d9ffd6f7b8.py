#Factores Primos
a=int(input("Ingrese número:"))
x=int(2)
while a!=1:
     if a%x==0:
         print(str(x)+" ")
         a=a/x
     else:
        x+=1