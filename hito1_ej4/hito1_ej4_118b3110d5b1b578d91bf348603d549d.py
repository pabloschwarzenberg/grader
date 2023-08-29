#Conversión de Decimal a Binario
x = int(input("Ingrese un número:"))

k=""
while x>=2:
    k += str(x%2)
    x = x//2
k +="1"
bina = k[::-1]
print("resultado=",bina)