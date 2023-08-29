#Ordenar tres números
def Numeros_a_ordenar(n1, n2, n3):
    numeromenor = min(n1, n2, n3)
    Numeromayor = max(n1, n2, n3)
    numeromedio = (n1 + n2 + n3) - numeromenor - Numeromayor
#defines los numeros colocando de mayor a menor en orden
    print(numeromenor, "," ,numeromedio, "," , Numeromayor)
#se imprime el orden de los numeros con las comas entre comillas para que se muestre asi
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
#preguntas los numeros que hay que ordenar, con int porque tienen que ser enteros
Numeros_a_ordenar(n1, n2, n3)     