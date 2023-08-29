soluciones=[]
def masuno(solucion):
    solucion+="1"
    return solucion
def mascero(solucion):
    solucion+="0"
    return solucion
def yesornoTrueorFalse(solucion,n):
    global soluciones
    if len(solucion)==n and solucion not in soluciones:
        return True
    else:
        return False
def guardarsolucion(solucion):
    global soluciones
    soluciones.append(solucion)
    return
def generadordeopcion(solucion,i):
    if i==0:
        return masuno(solucion)
    else:
        return mascero(solucion)
def backtracking(n,solucion=""):#meterunavacíaeirgenerandolasopciones
    if yesornoTrueorFalse(solucion,n)==True:
        guardarsolucion(solucion)
        return
    opciones=[]
    for i in range(2):
        a=generadordeopcion(solucion,i)
        opciones.append(a)
    for i in opciones:
        backtracking(n,i)
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
backtracking(n)
for i in soluciones:
    print(i)
           