a = eval(input("ingrese un numero:"))
def numero_perfecto(a):
    divisores = [1]
    for i in range(2,a + 1):
        if a % i == 0:
           divisores.append(i)

    siul = sum(divisores)
    siulmenosa = siul - a


    return siulmenosa

resultado = numero_perfecto(a)

while True:
    if numero_perfecto(a) == a:
        print("true")
    else:
        print("false")
    break