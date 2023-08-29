#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())

i = "x"
def combinaciones(n,i):
    if i=="x":
        i = (2**n)-1
        print("IT WORKED",i)

    if i==0:
        print("0"*n)
        return print(" FIN ")

    else:
        binar = bin(i)           # la funcion bin retorna: 0b+"i en binario" 
        binario = binar[2:]      # se quita la parte de 0b, solo queda el binario
        if len(binario)==n:
            print(binario)
            return combinaciones(n,i-1)
        else:
            print("0"*(n-len(binario))+ binario)
            return combinaciones(n,i-1)


#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
           