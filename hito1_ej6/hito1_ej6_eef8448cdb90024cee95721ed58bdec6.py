#Ordenar tres números
def num(n1, n2, n3):
    numeros = []
    numeros.append(n1)
    numeros.append(n2)
    numeros.append(n3)
    numeros.sort()
    return numeros

#if name == "main":
print(num(eval(input("Ingrese su numero: ")),eval(input("Ingrese su numero: ")),eval(input("Ingrese su numero: "))))
