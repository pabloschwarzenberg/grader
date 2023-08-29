def numero_perfecto(a):
    divisor=[1]
    for i in range (2,a+1):
        if a % i ==0:
            divisor.append(i)
    div=sum(divisor)
    d=div-a
    if d==a:
        return True
    else:
        return False
    return d

#if __name__=="__main__":
#   a=int(input("Ingrese a: "))
#    print(numero_perfecto(a))
           