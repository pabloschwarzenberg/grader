import difflib as d

def levenshtein(palabra1, palabra2):
    L = list(d.ndiff(palabra1,palabra2))
    for i in range(len(L)):
        L[i] = L[i].replace(" ","")
    ins = 0
    eli = 0
    ree = 0
    seReemp = False
    i = 0
    while i< len(L):
        letra = L[i]
        if letra[0] == "+": 
            ins += 1
        if letra[0] == "-":
            if i <len(L)-1:
                sigLetra = L[i+1]
                if sigLetra[0] == "+":
                    ree +=1
                    i+=1
                else:
                    eli += 1    
            else:
                eli += 1
        i+=1
    distancia = ins+eli+ree
    if distancia > 1:
        salida = "+1"
    elif distancia == 1 and (ins == 1 or eli == 1):
        salida = "IB"
    elif distancia == 1 and (ree == 1):
        salida = "1S"
    elif distancia == 0:
        salida = "0D"
    return salida