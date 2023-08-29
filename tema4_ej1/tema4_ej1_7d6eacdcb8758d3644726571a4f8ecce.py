import random
palabras = ['gato', 'perro', 'casa', 'tombola', 'mesa', 'flor', 'uñas', 'mochila', 'cuaderno', 'lapiz', 'pieza', 'tiempo', 'sol', 'viento']
p = palabras[random.randint(0,13)]
n = random.randint(0,len(p))

def ocultar_letras(palabra,cantidad):
    palabra1 = list(palabra)
    i=0
    lis =[]
    while i < (cantidad-1):
        ap = True
        while ap == True:
            c = random.randint(0, (len(p)-1))
            ap = False
            for i in range(len(lis)):
                if c == lis[i]:
                    ap = True 
        palabra1.pop(c)
        palabra1.insert(c,'_')
        lis.append(c)
        i+=1
    palabra1 = "".join(palabra1)
    return(palabra1)

def revisar_letra(palabra,palabra_secreta,letra):
    palabra_secreta = list(palabra_secreta)
    palabrak = list(palabra)
    if len(letra) == 1:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == "_":
                for k in range(len(palabrak)):
                    if letra == palabrak[k]:
                        palabra_secreta[k] = letra
                    else:
                        continue
        j = "".join(palabra_secreta)
    else:
        letra = list(letra)
        if letra == palabrak:
            palabra_secreta = palabrak
            j = "".join(palabra_secreta)
        else:
            j = "".join(palabra_secreta)
    return(j)
    

if __name__ == "__main__":
    k = ocultar_letras(p,n)
    while True:
        print(k)
        a = input("Ingresar letra o palabra: ")
        k = revisar_letra(p,k,a)
        if k == p:
            print(k)
            break