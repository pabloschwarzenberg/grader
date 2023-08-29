import codecs

def rot13(palabra):
    PalabraFinal = codecs.encode(palabra,'rot_13')
    return PalabraFinal
    

if __name__=="__main__":
    Palabra=input("\nIngresa la palabra que quieras encriptar: ")
    rot13(Palabra)
           