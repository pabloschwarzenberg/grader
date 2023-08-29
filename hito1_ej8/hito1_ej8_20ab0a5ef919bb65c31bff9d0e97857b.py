#Descomponer un número
n=int(input("Ingrese un numero: "))
unidades=["M","C","D","U"]
ns=list(str(n))
x=""
sal=[]

for i in range(len(ns)):
    x=(ns[len(ns)-i-1]+(unidades[3-i]))
    sal.append(x)

sal.reverse()
resultado=""
for i in sal:
    resultado=resultado+i+" + "

print(resultado[:-3])     