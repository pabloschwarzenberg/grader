#Descomponer un número
import math
print("Descomponer un numero.")
numero = int(input("Ingrese un numero de 4 dígitos: "))
a = (numero//1000) % 10
b = (numero//100) % 10
c = (numero//10) % 10
d = (numero//1) % 10
digitos=int(math.log10(numero))+1
if  digitos == 4:
    print(a,"M + ",b,"C + ",c,"D + ",d,"U")
elif digitos == 3:
    print(b, "C + ", c, "D + ", d, "U")
elif digitos == 2:
    print(c, "D + ", d, "U")
elif digitos == 1:
    print(d, "U")      