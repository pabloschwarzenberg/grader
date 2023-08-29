__author__ = 'joseletelierh'
def rot13(s):
    def lookup(v):
        o, c = ord(v), v.lower()
        if 'a' <= c <= 'm':
            return chr(o + 13)
        if 'n' <= c <= 'z':
            return chr(o - 13)
        return v
    return ''.join(map(lookup, s))

if __name__=="__main__":
    s=input("Ingresa la palabra que quieras encriptar: ")
    s.lower()
    resultado=rot13(s)
    print("El resultado es: ",resultado)
           