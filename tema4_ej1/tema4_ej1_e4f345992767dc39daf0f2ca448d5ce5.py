from random import randint
def ocultar_letras(p, c):
    p = "maquina"
    a = []
    p = list(p)
    while c != 0:
        x = randint(1,len(p)-1)
        if x not in a:
         a.append(x)
         c-=1
         p[x] = "_"
    p = "".join(p)
    return p

def revisar_letra(p_s,p,l):
    x = list(p_s)
    p = list(p)
    if l in x:
        y = p_s.find("-")
        p[y] = l
    p = "".join(p)
    print(p)
    return p