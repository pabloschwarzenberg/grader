def numero_perfecto(n):
    sumador=0
    for i in range (1,n,1):
        if n%i == 0:
            sumador+=i
    if sumador==n:
        return True
    else: 
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           