def numero_perfecto(a):
    total = 0
    for i in range(1, a-1):
        if a%i == 0:
            total += i
    if total == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           