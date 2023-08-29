def d(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    return suma

def numero_perfecto(a):
    if d(a) == a:
        return True
    else:
        return False
        
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           