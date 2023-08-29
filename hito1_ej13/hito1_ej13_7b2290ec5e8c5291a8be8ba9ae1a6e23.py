num = int(input("Ingresa un número: "))

def primer_primo(num):
    desc_primos = []

    for i in range(2, num+1):
        while num%i == 0:
            desc_primos.append(i)
            num = num/i

    for j in range(0, len(desc_primos)):
        print(str(desc_primos[j]))


primer_primo(num)