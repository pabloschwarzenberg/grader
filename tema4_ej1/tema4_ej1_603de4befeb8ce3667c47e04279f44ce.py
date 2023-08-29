import random
def ocultar_letras(palabra,cantidad):
    new = list(palabra)
    ran = []
    for i in range(len(palabra)):
        ran.append(i)
    
    for i in range(0,cantidad):
        a = random.choice(ran)
        ran.remove(a)
        new[a] = "_"
        palabra = str("".join(new))   
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    print(palabra)
    new = list(palabra)
    palabra = list(palabra_secreta)
    
    print(new)
    b = 0

    for i in palabra: 
        if i == letra:
            new[b] = letra
        palabra_n = str("".join(new))
        
        b = b + 1
    return palabra_n


         