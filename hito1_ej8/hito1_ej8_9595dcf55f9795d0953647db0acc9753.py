#Descomponer un número
n = eval(input("Ingrese un número de 4 dígitos: "))
u = n%10
n = n//10
d = n%10
n = n//10
c = n%10
n = n//10
u_mil = n%10
print(u_mil,"M +",c,"C +",d,"D +",u,"U")