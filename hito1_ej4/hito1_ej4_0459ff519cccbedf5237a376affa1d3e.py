#Conversión de Decimal a Binario
print("ingrese un numero para la conversion a binario:")
a = int(input())
lista = []
while a>=1:
    lista.insert(0,a%2)
    a = a // 2
final = "".join(str(i) for i in lista)
print("resultado=",final)



