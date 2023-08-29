#Factores Primos
print("Hola estudiante")
num = int(input("Ingresa un numero: "))

def descomponer(num):
    primos =[]
    for i in range(2, num+1):
        while num % i == 0:
            primos.append(i)
            num = num / i
    return primos
print(descomponer(num))
      