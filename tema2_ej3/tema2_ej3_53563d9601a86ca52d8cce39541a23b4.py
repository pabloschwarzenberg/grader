def numero_perfecto(x):
    sum = 0
    div = x
    while div > 1:
        div = div - 1
        if (x % div) == 0:
            sum += div
    if sum==x:
        return True
    if sum !=x:
        return False
if __name__=="__main__":
    x=int(input("Ingrese a: "))
    print(numero_perfecto(x))