def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s ) 


if __name__=="__main__":
    s=input("Ingresa la palabra que quieras encriptar: ")
    s.lower()
    resultado=rot13(s)
    print("El resultado es: ",resultado)
           