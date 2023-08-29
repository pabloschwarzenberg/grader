def rot13(word):
    pass

if __name__=="__main__":
    word=input("Ingresa la palabra para encriptarla: ")
    word.lower()
    word=rot13(word)
    print("El resultado seria: ",word)
def rot13(s):
    chates = "abcdefghijklmnopqrstuvwxyz"
    trikitraka = chates[13:]+chates[:13]
    rot_char = lambda c: trikitraka[chates.find(c)] if chates.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )