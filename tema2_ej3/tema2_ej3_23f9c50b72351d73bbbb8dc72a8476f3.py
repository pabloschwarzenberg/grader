def numero_perfecto(a):
    contador=1
    divisores=0
    sumadivisores=0
    while contador<a:
        posible_divisor= a%contador
        if posible_divisor==0:
            sumadivisores+=contador
            divisores+=1
        contador+=1
    if sumadivisores==a:
        return True  
    elif sumadivisores!=a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           