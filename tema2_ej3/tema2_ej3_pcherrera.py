def numero_perfecto(a):
    i = 1
    suma1 = 0
    while a > i :
        if a % i == 0 :
            suma1 = suma1 + a/i
            i = i + 1
        else :
            i = i + 1
    suma1 = suma1 - a + 1
    if suma1 == a:
       return True
    else:
       return False    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           