def suma_div(number):
    div=[]
    for i in range(1,number):
        if number%i==0:
            div.append(i)
    return sum(div)

def numero_perfecto(a):
    if suma_div(a)==a:
        return True
    else:
        return False

def suma_perfectos(n):
    suma=0
    for i in range(1,n):
        if numero_perfecto(i)==True:
            suma+=i
    return suma

if __name__=="__main__":
    print("Ver si un número es perfecto o no.")
    num=int(input("Ingrese número: "))
    print(numero_perfecto(num))
    print("Suma de los números perfectos menores que un valor.")
    na=int(input("Ingrese valor: "))
    print(suma_perfectos(na))
