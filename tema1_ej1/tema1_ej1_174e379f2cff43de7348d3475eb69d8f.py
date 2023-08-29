n = int(input("digite el número "))
num = (n * (n + 1) / 2)
resultado = 0
for i in range(1,n + 1):
    resultado += i

resultado = sum(range(1, n + 1))


print(resultado)