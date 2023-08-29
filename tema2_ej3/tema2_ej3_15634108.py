def numero_perfecto(a):
    sumadiv=1
    for i in range(2,a):
        if a%i==0:
            sumadiv=sumadiv+i
        else:
            pass
    if sumadiv==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           