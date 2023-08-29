def numero_perfecto(a):
    suma=0
    i=1
    while i < a:
        division = a/i
        if division.is_integer():
            suma += i
        i+=1
    if suma == a:
        return True
        
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           