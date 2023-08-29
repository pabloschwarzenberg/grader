      #FUNCIONES
#crea una lista con todas las subsecuencias
def subsecuencias(string,numero):
    secuencias=[]
    n=len(string)-(numero-1)
    x=0
    y=0
    while x<n:
        substring=""
        for i in range(0,numero):
            substring+=string[y]
            y+=1
        secuencias.append(substring)
        y-=numero-1
        x+=1
    return secuencias

#crea una lista solo con las subsecuencias que no se repiten
def noRepetidas(subsecuencias):
    noRepetidas=[]
    repetidas_borradas=[]
    for i in subsecuencias:
        if i in noRepetidas:
            noRepetidas.remove(i)
            repetidas_borradas.append(i)    
        elif    not i in repetidas_borradas:
            noRepetidas.append(i)
    if len(noRepetidas)==0:
        noRepetidas.append("ninguna")
    return noRepetidas

#ENTRADA   
string=input("Ingrese string :")
n=int(input("Ingrese número: "))
#SALIDA
todas=subsecuencias(string,n)
noRepetidas=noRepetidas(todas)
for i in noRepetidas:
    print(i)