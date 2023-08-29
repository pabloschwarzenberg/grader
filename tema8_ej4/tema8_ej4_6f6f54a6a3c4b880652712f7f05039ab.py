def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    secreto = "".join([abecedario[(abecedario.find(c)+13)%26] for c in palabra])
    return secreto

if __name__=="__main__":
    y = input("Escribir algo: \n")
    r=rot13(y)
    print(r)
           