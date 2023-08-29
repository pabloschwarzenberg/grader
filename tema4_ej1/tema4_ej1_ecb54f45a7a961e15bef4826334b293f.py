import random

def ocultar_letras(palabra,cantidad):
    a=list(palabra)
    b=len(a)
    i=0
    d=0
    while i<cantidad:
       d=random.randint(0,b-1)
       if "_" not in a[d]:
           a.remove(a[d])
           a.insert(d, "_")
           i += 1
       elif "_" in a[d]:
           i+=0
    z="".join(a)
    return (z)

#w=input()
#e=int(input())
#u=ocultar_letras(w,e)
#print(u)

def revisar_letra(palabra_secreta,palabra,letra):
    a=list(palabra_secreta)
    b=list(palabra)
    if letra in palabra_secreta:
        b.pop(10)
        b.append("o")
    c="".join(b)
    return c

if __name__ == "__main__":
    pass
         