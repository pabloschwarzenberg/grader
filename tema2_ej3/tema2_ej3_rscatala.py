def numero_perfecto(n):
    sum_divisores = 0
    i=1
    while i < n:
        if n%i == 0:
            sum_divisores += i
        i += 1
    if sum_divisores == n:
        return True
    else:
        return False

if __name__=="__main__":
    num=int(input("Ingrese un número: "))
    print(numero_perfecto(num))
    suma_perfectos = 0
    for numeral in range(1,num):     
        if numero_perfecto(numeral) == True:
            suma_perfectos += numeral
    print("La suma de los números perfectos menores a ",num," es: ",suma_perfectos)
           