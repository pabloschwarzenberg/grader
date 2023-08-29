#Conversión de Decimal a Binario
N = eval(input("Ingrese el numero que quiere transformar a binario -> "))
lista = []

while (N >= 1):
    lista.insert(0, N%2)
    N = N // 2

R = "".join(str(i) for i in lista)
print("resultado=", R)
