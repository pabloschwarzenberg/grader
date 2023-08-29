def bin_dec(b): # <- 10100
    b = str(b)[::-1]
    c = 0
    for i in range(len(b)):
        c += int(b[i]) * (2 ** i)
    return c # -> 20

def decodificar(d):
    a = ''
    d = d.split(',')
    for i in d:
        n = bin_dec(i)
        a = a + chr(n)
    return a

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         