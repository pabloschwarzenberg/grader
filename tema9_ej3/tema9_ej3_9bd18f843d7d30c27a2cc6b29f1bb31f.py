def BTD(B):
    D = 0
    i = 0
    while B >= 1:
        k = B%10
        B = B//10
        D += k*pow(2,i)
        i += 1
    return D

def decodificar(m):
    ML = m.split(',')
    P = ''
    for i in ML:
        k = int(i)
        D = BTD(k)
        O = chr(D)
        P += O
    return P

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         