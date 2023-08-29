def numero_perfecto(n):
    sumatorio=0
    for i in range(1,n):
        if n%i==0:
            sumatorio=sumatorio+i
    if sumatorio==n:
        return True
    else:
        return False

if __name__ == "__main__":
    N=int(input("Ingresa numero: "))
    A=numero_perfecto(N)
    print(A)