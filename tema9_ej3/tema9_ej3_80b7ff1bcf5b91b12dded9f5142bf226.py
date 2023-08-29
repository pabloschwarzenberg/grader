def binario_a_decimal(codigo):
    codigo=codigo[::-1]
    i=0
    suma=0
    while i < len(codigo):
        suma=suma+(2**i)*(int(codigo[i]))
        i=i+1
    return suma
    
def decodificar(mensaje):
    L=mensaje.split(",")
    j=0
    i=0
    while j < len(L):
        L[j]=binario_a_decimal(L[j])
        j=j+1
    while i<len(L):
        L[i]=chr(L[i])
        i=i+1
    mensaje="".join(L)
    return mensaje