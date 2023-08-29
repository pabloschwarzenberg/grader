def rot13(palabra):
    abc='abcdefghijklm'
    cde='nopqrstuvwxyz'
    zzzz=dict(zip(abc+cde, cde+abc))
    return ''.join(zzzz.get(x.lower(), x) for x in palabra)
    pass

if "_name_"=="_main_":
    palabra=input("ingresa la palabra que quieras encriptar: ")
    resultado=rot13(palabra)
    print("el resultado es: ",resultado)
           