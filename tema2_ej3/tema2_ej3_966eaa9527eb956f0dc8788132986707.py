def numero_perfecto(a):
    div = 0
    n = 1
    while n < a:
        if a % n == 0:
            div += n
        n += 1
    if div == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n = a
    b = 1
    c = 0

    while b < n:
        if numero_perfecto(b) is True:
            c += b
        b += 1
    print(c)
           