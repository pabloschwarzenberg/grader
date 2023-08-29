#Descomponer un número
n = int(input("Ingrese un número de 4 dígitos: "))

u = n%10
n = n//10
d = n%10
n = n//10
c = n%10
n = n//10
m = n%10

print(m,"M +",c,"C +", d,"D +",u,"U.")
   