def numero_perfecto(a):
    pozo=0
    for n in range(1,a):
        if a%n==0:
            pozo=pozo+n
    if pozo==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           