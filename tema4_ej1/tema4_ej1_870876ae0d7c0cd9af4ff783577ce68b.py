from random import randint, sample, randrange
def ocultar_letras(palabra,cantidad):
    p1 = list(palabra)
    x = 0
    z = 0
    while x < cantidad:
        p1.pop(randint(1,cantidad))
        x = x+1
    while len(p1) <=len(palabra) and z < len(palabra):
        if p1[z] != palabra[z] and p1[z] != 0:
            p1.insert(z,'_')
        z = z+1
    return ''.join(p1)
    
def revisar_letra(palabra,palabra_secreta,letra):
    a1 = list(palabra_secreta)
    a2 = list(palabra)
    i = 0
    while i <len(palabra):
        if palabra_secreta[i] == '_' and palabra[i] == letra:
            a1.pop(i)
            a1.insert(i,a2[i])
        i = i+1
    return ''.join(a1)