def rot13(s):
    rot=lambda x:chr(ord(x)+13) if chr(ord(x.lower())+13).isalpha()==True else chr(ord(x)-13)
    s=[rot(i) for i in filter(lambda x:x!=',',map(str,s))]
    return "".join(s)
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           