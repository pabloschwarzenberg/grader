def numero_perfecto(num):
    suma = 0
    for i in range (1,num):
        if num % i == 0:
            suma += i
    return suma == num
print(numero_perfecto(6))
def jerigonzo(palabra):
    traducir=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            traducir += letra
            traducir += "p"
        traducir += letra
    return traducir

    palabra = input("ingresa una palabra: ")
    print(jerigonzo(palabra))
    pass
