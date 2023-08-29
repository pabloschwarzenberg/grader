#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")

def combis(n,bin=''):
    
    if len(bin)==n:
        print(bin)


    else:
        for i in range(0,2):
            bin_aux=bin+str(i)
            #print(bin_aux)
            combis(n,bin_aux)

combis(n)


