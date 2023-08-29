def numero_perfecto(a):
    x = 0
    for i in range(1,a+1):
        if a % i == 0:
            x += i
        else:
            continue
    if x-a == a:
        return True
    else:
        return False
if __name__ =="__main__":
    a = int(input("Ingrese el numero: "))
    print(numero_perfecto(a))