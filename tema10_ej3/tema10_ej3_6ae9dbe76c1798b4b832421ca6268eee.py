def sopaletras(nombre_archivo,palabras):
libro = open(nombre_archivo, "r")
matriz=[]
text=""
a=[]
a = list(palabras[0])
for letra in libro:
    aux=letra.lower().strip().split(",")
    matriz.append(aux)

i=0

while i < len(matriz):
    j = 0
    while j < len(matriz)+1:
        if matriz[i][j]==a[i]:
            text+=matriz[i][j]
            j+=1
        else:
            j+=1
    i += 1

return matriz, a, text

if __name__=="__main__":

print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

    print(sopaletras("sopa.txt", ["cra"]))