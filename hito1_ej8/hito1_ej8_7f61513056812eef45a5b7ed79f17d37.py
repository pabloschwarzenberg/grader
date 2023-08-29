#Descomponer un número
x=int(input("Ingrese un numero de maximo 4 digitos: "))
a=str((x//1000)%10)
b=str((x//100)%10)
c=str((x//10)%10)
d=str(x%10)

if x>999:
    print(a+"M","+", b+"C","+", c+"D","+", d+"U")
if 999>=x>99:
    print(b+"C","+", c+"D","+", d+"U")
if 99>=x>9:
    print(c+"D","+", d+"U")
if 9>=x>=1:
    print(d+"U")