def es_primo(n):
    factorial = 1
    i = 2
    while(i < n):
        factorial *= i;
        i+=1
    if (factorial + 1) % n == 0 and n >1:
        print("El número es primo")
        return True
    else:
        print("El número no es primo")
        return False