def suma_divisor(a):
    contador=1
    suma=0
    while contador<a:
        if a%contador==0:
            suma+=contador
        contador+=1
    return suma

def numero_perfecto(a):
    if suma_divisor(a)==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))