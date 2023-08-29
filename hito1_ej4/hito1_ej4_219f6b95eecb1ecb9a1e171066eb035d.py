#Conversión de Decimal a Binario
n = int(input("Ingrese número decimal: "))
lista = []
while n>0:
    resto = int(n%2)
    lista.append(resto)
    n = (n-resto)/2
num_bin = ""
for e in lista[::-1]:
    num_bin = num_bin + str(e)
print("resultado=",num_bin)
