def es_primo(num):
    if num == 0 or num == 1:
        print("no es primo")
        return False
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
           