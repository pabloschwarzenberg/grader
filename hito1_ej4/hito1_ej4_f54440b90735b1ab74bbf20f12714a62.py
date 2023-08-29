#Conversión de Decimal a Binario
n = int(input("Ingrese el numero que sera convertido a binario: "))
bina = ""

while n != 1:
    num = n % 2
    n = n // 2
    bina += str(num)

bina += str(n)

n_binario = bina[len(bina)::-1]
print("resultado=", n_binario)