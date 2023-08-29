#Descomponer un número
N = int(input("Ingrese un numero de hasta 4 digitos:"))
d = N % 10
c = int((N % 100)/10)
b = int((N % 1000)/100)
a = int((N % 10000)/1000)

if N > 999:
    print(str(a)+"M +", str(b)+"C +", str(c)+"D +", str(d)+"U")
if N < 1000:
    print(str(b) + "C +", str(c) + "D +", str(d) + "U")