def decodificar(men):
    ##
    a = str(men[0:8])
    dec1=(int(str(a), 2))
    l1=chr(dec1)
    ##
    b = str(men[10:17])
    dec2=(int(str(b), 2))
    l2=chr(dec2)
    ##
    c = str(men[19:26])
    dec3=(int(str(c), 2))
    l3=chr(dec3)
    ##
    d = str(men[28:35])
    dec4=(int(str(d), 2))
    l4=chr(dec4)
    p = l1+l2+l3+l4
    return p
if __name__ == "__main__":
    men=deco("01101000,01101111,01101100,01100001")
    print(men)