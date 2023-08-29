def numero_perfecto(a):
    d = 1
    suma = 0
    while d < a:
        z = a%d
        if z == 0:
            suma+=d
        d+=1
    if suma == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           