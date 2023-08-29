def numero_perfecto(a):
    divsum=0
    for i in range(1,a+1):
        div=0
        if a%i==0:
            div=a//i
            divsum+=div
        else:
            divsum+=0
    divsum-=a
    if divsum==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           