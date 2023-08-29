#Ordenar tres números:
#Definir la función
def ordenar(n1,n2,n3):
    n = [n1,n2,n3]
    n.sort()
#"sort" ordena los número dentro de la función
    nOrdenados = ", ".join(map(str, n)) 
#"join" separa por lo que indiquen las comillas que se le anteponen
#"map" aplica la def de la función a cada item dentro de ella
#"str" posterior a sort "ordena en una cadena de texto", es decir, de forma ascendente.
    return nOrdenados
#Solicitar datos de entrada:
a = int(input("Ingrese el primer número: ")) 
b = int(input("Ingrese el segundo número: ")) 
c = int(input("Ingrese el tercer número: ")) 
#Llamar a la función para ordenar los números 
resultado = ordenar(a,b,c)
#Imprimir los números ordenados 
print("Los números ordenados de menor a mayor son:", resultado) 