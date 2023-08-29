#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
lista = []
def binarios(string="", n=2):
    if n==0:
        if string not in lista:
            lista.append(string)
    for i in range(int(2**(n-1))):
        binarios(string=string+"0",n=n-1)
    for i in range(int(2**(n-1))):
        binarios(string=string+"1",n=n-1)

def binarios2(string="0"*n,pos=0):
    print(string)
    for i in range(pos+1,len(string)):
        string2 = string[0:i] + "1" + string[i+1:]
        binarios2(string2,i)
        
def binarios3(string="1"*n,pos=0):
    print(string)
    for i in range(pos+1,len(string)-1):
        string2 = string[0:i] + "1" + string[i+1:]
        binarios2(string2,i)
def binarios4():
    binarios2()
    binarios3()

binarios4()

print("0000")
           