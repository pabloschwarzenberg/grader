def ordenro(n1, n2, n3):

    if n1 > n2:
        n1, n2 = n2, n1 
    if n2> n3:
        n2 , n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1 
    return n1, n2, n3

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
n1, n2, n3 = ordenro (n1, n2, n3)

print("Resultados: {},{},{}".format(n1,n2,n3))