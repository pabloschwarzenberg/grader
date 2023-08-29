def numero_perfecto(n):
    suma = 0
    if n == 1:
        suma == 0
    for i in range(1,n):
        if n%i == 0:
            suma = suma + i
    if suma == n:
        return True
    elif suma != n:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           