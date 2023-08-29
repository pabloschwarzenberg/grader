#Descomponer un número
import math
a=input("Inserte número:")
if 10000>int(a)>=1000:#numero 4 digitos
    print(a[0],"M +",a[1],"C +",a[2],"D +",a[3],"U")
elif 1000>int(a)>=100:#numero 3 digitos
    print(a[0],"C +",a[1],"D +",a[2],"U")
elif 100>int(a)>=10:#numero 2 dígitos
    print(a[0],"D +",a[1],"U")
elif 10>int(a)>=0:#numero 1 dígito
    print(a[0],"U")
else:
    print("Inserte número de hasta 4 dígitos")












      