def decodificar(mensaje):
    ##
    A = str(mensaje[0:8])
    D1 = (int(str(A),2))
    L1 = chr(D1)
    
    ##
    B = str(mensaje[10:17])
    D2 = (int(str(B),2))
    L2 = chr(D2)
    
    ##
    C = str(mensaje[19:26])
    D3 = (int(str(C),2))
    L3 = chr(D3)
    
    ##
    D = str(mensaje[28:35])
    D4 = (int(str(D),2))
    L4 = chr(D4)
    palabra = L1+L2+L3+L4
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
