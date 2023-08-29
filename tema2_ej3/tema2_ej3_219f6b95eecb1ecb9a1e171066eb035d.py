def numero_perfecto(n):
    i = 1
    sum = 0
    es_perfecto = False
    while i < n:
        if n % i == 0:
            sum += i
        i += 1
    if sum == n:
        es_perfecto = True
    return es_perfecto

if __name__=="__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
           