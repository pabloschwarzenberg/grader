def numero_perfecto(num):
    suma = 0
    for i in range (1,num):
        if num % i == 0:
            suma += i
    return suma == num
print(numero_perfecto(6))