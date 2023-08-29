def descomp(x):
    prime = []
    for i in range(2, x + 1):
        while x % i == 0:
            prime.append(i)
            x = x / i
        return prime


x = int(input("Ingrese un valor"))
print(descomp(x))