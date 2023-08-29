def numero_perfecto(a):
    div=1
    contador=0
    for div in range(1,a):
        if a%div==0:
            contador+=div
            div+=1
        else:
            div+=1
    if a==contador:
        return True
    else:      
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           