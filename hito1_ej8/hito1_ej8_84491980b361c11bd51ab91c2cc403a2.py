#Descomponer un número
x=int(input("Ingrese un numero"))
u=x%10
d=int(x%100/10)
c=int(x%1000/100)
m=int(x%10000/1000)
print(m,"M+",c,"C+",d,"D+",u,"U")    