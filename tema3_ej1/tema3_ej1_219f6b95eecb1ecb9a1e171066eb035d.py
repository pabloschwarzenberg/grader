def suma_divisores(a):
    i = 1
    sum = 0
    es_primo = False
    while i < a:
        if a%i == 0:
            sum += i
        i += 1
    if sum ==1:
        es_primo = True
    return sum, es_primo

if __name__== "__main__":
    n = int(input("Ingrese número: "))
    resp = suma_divisores(n)
    print("Suma:", resp[0])
    print("Primo:", resp[1])