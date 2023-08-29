#Conversión de Decimal a Binario
numero = int(input("Ingrese un número decimal:"))
n = numero
k=[]

while numero > 0:
    res = int(numero%2)
    print("Valor para calcular:",res)
    k.append(res)
    numero = (numero-res)/2
string=""
resultado="resultado="

for binario in k[::-1]:
    a="".join(map(str,k[::-1]))
    print("resultado=",a,end="")
    break