hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""
def estadisticas_frase(frase):
    a=list(frase)
    s = len(frase.split())
    D=0
    y=0
    e=0
    p=0
    q=0

    for x in range(len(a)):
        if (a[x] == 'a'):
            D = D + 1
            y=y+1

        elif (a[x] == 'e'):
            D = D + 1
            y = y + 1
            q=q+1
        elif (a[x] == 'i'):
            D=D+1
            y = y + 1
        elif (a[x] == 'o'):
            D=D+1
            y = y + 1
        elif (a[x] == 'u'):
            D=D+1
            y = y + 1
        elif (a[x] == 'b'):
            D=D+1
            y = y + 1
        elif (a[x] == 'c'):
            D=D+1
            y = y + 1
        elif (a[x] == 'd'):
            D=D+1
            y = y + 1
        elif (a[x] == 'f'):
            D=D+1
            y = y + 1
        elif (a[x] == 'g'):
            D=D+1
            y = y + 1
        elif (a[x] == 'h'):
            D=D+1
            y = y + 1
        elif (a[x] == 'j'):
            D=D+1
            y = y + 1
        elif (a[x] == 'k'):
            D=D+1
            y = y + 1
        elif (a[x] == 'l'):
            D=D+1
            y = y + 1
        elif (a[x] == 'm'):
            D=D+1
            y = y + 1
        elif (a[x] == 'n'):
            D=D+1
            y = y + 1
        elif (a[x] == 'p'):
            D=D+1
            y = y + 1
        elif (a[x] == 'q'):
            D=D+1
            y = y + 1
        elif (a[x] == 'r'):
            D=D+1
            y = y + 1
        elif (a[x] == 's'):
            D = D + 1
            y = y + 1
        elif (a[x] == 't'):
            D=D+1
            y = y + 1
        elif (a[x] == 'v'):
            D=D+1
            y = y + 1
        elif (a[x] == 'w'):
            D=D+1
            y = y + 1
        elif (a[x] == 'x'):
            D=D+1
            y = y + 1
        elif (a[x] == 'y'):
            D=D+1
            y = y + 1
        elif (a[x] == 'z'):
            D=D+1
            y = y + 1
        elif (a[x] == 'ñ'):
            D=D+1
            y = y + 1
        elif (a[x] == ' '):
            e=e+1
            y = y + 1
        elif (a[x] == '.'):
            y = y + 1
            p=p+1
        elif (a[x] == '´'):
            y = y + 1
        elif (a[x] == 'A'):
            D = D + 1
            y = y + 1

        elif (a[x] == 'B'):
            D = D + 1
            y = y + 1
            q = q + 1
        elif (a[x] == 'C'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'D'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'E'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'F'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'G'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'H'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'I'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'J'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'K'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'L'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'M'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'N'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'O'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'P'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'Q'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'R'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'S'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'T'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'U'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'V'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'W'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'X'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'Y'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'Z'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'Ñ'):
            D = D + 1
            y = y + 1
        elif (a[x] == 'á'):
            D = D + 1
            y=y+1

        elif (a[x] == 'ó'):
            D = D + 1
            y = y + 1
            q=q+1
        elif (a[x] == 'í'):
            D=D+1
            y = y + 1

    w = D / s
    r=y+18
    return s,r,w,e,p


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
