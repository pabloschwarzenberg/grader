# ASCII
def bin_dec(b):
    b = b[::-1]
    decimal = 0
    i = 0
    for d in b:
        decimal += 2**i * int(d)
        i += 1
    return decimal
        
    
def decodificar(s):
    s = s.split(',')
    nuevalista = []
    mensaje = ''
    for numero in s:
        nuevodecimal = bin_dec(numero)
        nuevalista.append(nuevodecimal)
    for decimal in nuevalista:
        mensaje += chr(decimal)
    return mensaje
