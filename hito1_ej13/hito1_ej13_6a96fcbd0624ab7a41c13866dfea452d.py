def get_prime_list(upper):
    max_num = 2
    prime_list = []
    for num in range(2, int(upper) + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                max_num = num
                prime_list.append(max_num)
                # print(max_num)
    return list(reversed(prime_list))


numero = int(input("Ingrese un número: "))
primos = get_prime_list(numero)
factores = []
while True:
    if numero == 1:
        break
    for primo in primos:
        if numero % primo == 0:
            numero = numero / primo
            factores.append(primo)
[print(factor) for factor in factores]