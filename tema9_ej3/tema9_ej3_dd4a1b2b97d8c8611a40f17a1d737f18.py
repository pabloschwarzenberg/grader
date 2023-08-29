def binario(a):
    b=bin(a)
    b=b[0]+b[2::]
    return b

def codificar(i):
    p=chr(i)
    return p

x=range(65,91)
y=range(97,122)
x=list(x)
y=list(y)
x1=list(map(binario,x))
y1=list(map(binario,y))
x2=list(map(codificar,x))
y2=list(map(codificar,y))

def decodificar(mensaje):
    intento=""
    i=0
    j=0
    while i<len(mensaje):
        t=mensaje[j:j+8]
        if t in x1:
            i=x1.index(t)
            c=x2[i]
            intento=intento+c
            intento="".join
            
        if t in y1:
            i=y1.index(t)
            p=y2[i]
            intento=intento+p
            
        i=i+8
        j=j+9 
    return intento
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         