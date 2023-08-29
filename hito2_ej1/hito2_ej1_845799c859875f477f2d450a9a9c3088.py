lista=[]
def alinear(s1,s2):
    np1 = 0
    np2 = 0
    while True:
        if s2[np2] != s1[np1]:
            lista.append("_")
            np1 += 1
    
        elif s2[np2] == s1[np1]:
            lista.append(s2[np2])
            np2 += 1
        elif np1 > len(s1):
            agr = np2
            while True:
                lista.append(s2[agr])    #desde la posicion ultima de s2
                agr += 1
                if agr == len(s2):
                    break
        break
    return lista

s1 = str(input("Ingresa la primera secuencia de ADN: "))
s2 = str(input("Ingresa la segunda secuencia de ADN: "))
      
res = alinear(s1,s2)
print(lista)