# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    for i in range(2,a + 1):
        if a % i == 0:
           divisores.append(i)

    siul = sum(divisores)
    siulmenosa = siul - a


    return siulmenosa
   
if __name__=="__main__":
    a=int(input("Ingrese el numero: "))
    print(suma_divisores(siulmenosa,a))           