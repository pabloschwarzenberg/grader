a = eval(input("ingrese un numero:"))
def suma_divisores(a):
    divisores = [1]
    for i in range(2,a + 1):
        if a % i == 0:
           divisores.append(i)

    siul = sum(divisores)
    siulmenosa = siul - a


    return siulmenosa

resultado = suma_divisores(a)
print(resultado)

while True:
    if suma_divisores(a) == 1:
        print("True")
    else:
        print("False")
    break


           