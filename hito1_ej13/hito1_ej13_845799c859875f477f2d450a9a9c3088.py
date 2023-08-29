num = int(input("Ingresa un numero: "))

numeros=[]

while True:
    for n in range(2, num+1):
        if num % n == 0:
            num = num / n
            numeros.append(n)
            if num == 1:
                break
    break      


for n in numeros:
    print(n)
