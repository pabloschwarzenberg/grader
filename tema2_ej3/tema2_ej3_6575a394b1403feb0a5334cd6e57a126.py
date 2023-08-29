def numero_perfecto(a):
    i = 1
    n = 0
    while(0 < i < a):
        if(a % i == 0):
            n = n + i
        i = i + 1
    if n == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    
           