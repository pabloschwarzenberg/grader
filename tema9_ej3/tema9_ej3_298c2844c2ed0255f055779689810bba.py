def decodificar(mensaje):
    L=mensaje.split(",")
    L2=""
    for x in L:
        L2+=chr(int(x[:8], 2))
    return L2

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

def jerigonzo(s):
    K="aeoiuAEOIU"
    L=""
    for x in range(len(s)):
        if s[x] in K:
            L+=s[x]+"p"+s[x]
        else:
            L+=s[x]
    return L