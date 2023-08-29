def numero_perfecto(a):
    n=1
    divisores=0
    while n<a:
        if a%n==0:
            divisores+=n
            n+=1
        else:
            n+=1
    if divisores==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           