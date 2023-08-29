def binario_a_decimal(n):
    n1=list(n)
    n2="".join(n1)
    n3=int(n2)
    i=0
    suma=0
    while i<=len(n1):
        a=(n3//(10**i))%10
        b=a*(2**i)
        suma+=b
        i+=1
    return suma

mensaje="01101000,01101111,01101100,01100001"
def decodificar(mensaje):
    a=mensaje.split(',')
    mensaje_final=[]
    i=0
    while i<len(a):
        b=a[i]
        b1=binario_a_decimal(b)
        b2=chr(b1)
        mensaje_final.append(b2)
        i+=1
    mensaje_final2="".join(mensaje_final)
    return mensaje_final2