#Descomponer un número
n= int(input("Ingres3 un número de 4 digitos: "))
u = n%10
n = n//10
d = n%10
n = n//10
c = n%10
n = n//10
uM = n%10

print("Descomposición:", uM,"M","+",c,"C","+",d,"D","+",u,"U")