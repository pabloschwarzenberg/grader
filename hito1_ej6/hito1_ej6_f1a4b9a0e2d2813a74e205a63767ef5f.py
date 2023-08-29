#Ordenar tres números
def ordenar_numeros(n1, n2, n3):
    numeros= [n1, n2, n3]
    numeros.sort()
    numeros_ordenados= ",".join(str(n)for n in numeros)
    print(numeros_ordenados)

n1= int(input("Digite primer numero: "))
n2= int(input("Digite el segundo numero: "))
n3= int(input("Digite el tercer numero: "))

ordenar_numeros(n1, n2, n3)