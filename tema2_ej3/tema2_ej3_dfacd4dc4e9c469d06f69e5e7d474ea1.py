def suma_divisores(a):
    d=1
    suma = 0
    while d<a-1:
        if a%d == 0:
            suma +=d
            print(d)
        d += 1
    if suma == 1:
         return suma
    else:
         return suma
         
def numero_perfecto(a):
    if suma_divisores(a) == a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           