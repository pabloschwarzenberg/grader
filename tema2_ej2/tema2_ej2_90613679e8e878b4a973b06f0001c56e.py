# completa el código de la función
def amigos(a, b):
    listaA = []
    listaB = []
    for n in range(1, a):
        if a%n == 0:
            listaA.append(n)
    for i in range(1, b):
        if b%i == 0:
            listaB.append(i)
    if a in listaB:
        listaB.remove(a)
    if b in listaA:
        listaA.remove(b)

    if sum(listaA) == b and sum(listaB) == a:
        return True
    else:
        return False
if __name__ == "__main__":
    a = int(input("Ingrese 1er numero: "))
    b = int(input("Ingrese 2do Numero: "))
    print(amigos(a, b))

           