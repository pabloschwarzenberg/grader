#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
def binario(cant,numero):

    cant=int(cant)


    if len(numero)==cant:

        print(numero)

        return

    

    for dig in ["0","1"]:

        numero=numero+dig

        binario(cant,numero)

        numero=numero[0:len(numero)-1]


if __name__ == "__main__":
    n=int(input())
    binario(n,"")

    

        

