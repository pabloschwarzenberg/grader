def suma_divisores(a):
    divisores = [1]
    for i in range ( 2, a+1):
        if a % i == 0:
            divisores.append(i)
            suma = sum (divisores)   
    return suma - a

def numero_perfecto(a):
    if a == suma_divisores(a):
        return True
    else:
        return False

if __name__=="__main__":
    a = int(input("Ingrese: "))
    print(numero_perfecto(a))