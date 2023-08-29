def suma_divisores(num):
    suma=0
    i=1
    while i<=num-1:
        if num%i==0:
            suma=suma+i
        i=i+1
    return suma

def numero_perfecto(a):
    if suma_divisores(a)==a:
        return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
           