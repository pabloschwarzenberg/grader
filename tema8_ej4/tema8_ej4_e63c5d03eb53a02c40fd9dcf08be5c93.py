def rot13(palabra)
 letras = "abcdefghijklmnopqrstuvwxyz"
 conver = letras[13:]+letras[:13]
 con_letra = lambda c: conver[letras.find(c)] if letras.find(c)>-1 else c
 return ''.join( con_letra(c) for c in s )
 pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           