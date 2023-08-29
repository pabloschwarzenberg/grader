def decodificar(mensaje):
    mensaje=mensaje.split(",")
    decimal=[]
    for elem in mensaje:
        if elem=="01100001":
            decimal.append(97)
        if elem=="01100010":
            decimal.append(98)
        if elem=="01100011":
            decimal.append(99)
        if elem=="01100100":
            decimal.append(100)
        if elem=="01100101":
            decimal.append(101)
        if elem=="01100110":
            decimal.append(102)
        if elem=="01100111":
            decimal.append(103)
        if elem=="01101000":
            decimal.append(104)
        if elem=="01101001":
            decimal.append(105)
        if elem=="01101010":
            decimal.append(106)
        if elem=="01101011":
            decimal.append(107)
        if elem=="01101100":
            decimal.append(108)
        if elem=="01101101":
            decimal.append(109)
        if elem=="01101110":
            decimal.append(110)
        if elem=="01101111":
            decimal.append(111)
        if elem=="01110000":
            decimal.append(112)
        if elem=="01110001":
            decimal.append(113)
        if elem=="01110010":
            decimal.append(114)
        if elem=="01110011":
            decimal.append(115)
        if elem=="01110100":
            decimal.append(116)
        if elem=="01110101":
            decimal.append(117)
        if elem=="01110110":
            decimal.append(118)
        if elem=="01110111":
            decimal.append(119)
        if elem=="01111000":
            decimal.append(120)
        if elem=="01111001":
            decimal.append(121)
        if elem=="01111010":
            decimal.append(122)
    letras=[]
    for mal in decimal:
        letras.append(chr(mal))
    mensaje="".join(letras)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         