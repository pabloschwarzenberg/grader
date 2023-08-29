#Creador: Daniel Ugarte
def decodificar(mens):
    ##
    a = str(mens[0:8])
    decl1=(int(str(a), 2))
    let1=chr(decl1)
    ##
    b = str(mens[10:17])
    decl2=(int(str(b), 2))
    let2=chr(decl2)
    ##
    c = str(mens[19:26])
    decl3=(int(str(c), 2))
    let3=chr(decl3)
    ##
    d = str(mens[28:35])
    decl4=(int(str(d), 2))
    let4=chr(decl4)
    pal = let1+let2+let3+let4
    return pal
if __name__ == "__main__":
    mens=decodificar("01101000,01101111,01101100,01100001")
    print(mens)
         