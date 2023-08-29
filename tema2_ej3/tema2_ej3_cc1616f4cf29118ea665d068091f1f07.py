def numero_perfecto(n):
    sd = 0
    for i in range(1,n):
        if (n%i==0):
            sd = sd + i
    if sd==n:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           