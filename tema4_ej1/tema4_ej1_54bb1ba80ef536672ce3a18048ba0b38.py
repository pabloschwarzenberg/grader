import random

def ocultar_letras(palabra,cantidad):
    z = [str(x) for x in palabra ]
    a = random.sample(range(0,len(palabra)),cantidad)
    t = a[0]
    print(a)
    print(t)
    for x in a:
        z.pop(x)
        z.insert(x, '_')
        Pal = ''.join([str(y) for y in z])
        palabra = Pal
    return Pal

def revisar_letra(palabra_secreta,palabra,letra):
    z = [str(x) for x in palabra ]
    w = [str(x) for x in palabra_secreta]
    for x,y in enumerate(w):
      if y == letra:
        z[x] = letra
    Pal = "".join([str(y) for y in z])
    return Pal

         