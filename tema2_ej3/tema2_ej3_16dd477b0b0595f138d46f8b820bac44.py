def numero_perfecto(a):
    n=1
    c=0
    for n in range (1,a):
        if a%n==0:
            c=c+n
    if c==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           