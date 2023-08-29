def numero_perfecto(a):
    n = int(a)
    total = 0
    for i in range(n-1):
        if n%(i+1) == 0:
            total += (i+1)

    if n == total:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))