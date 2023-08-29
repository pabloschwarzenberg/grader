def rot13(palabra):
    abc1='abcdefghijklm'
    abc2='nopqrstuvwxyz'
    zzzz=dict(zip(abc1+abc2, abc2+abc1))
    return ''.join(zzzz.get(x.lower(), x) for x in palabra)
    pass

if name =="_main_":
    palabra=input("ingresa la palabra que quieras encriptar: ")
    resultado=rot13(palabra)
    print("el resultado es: ",resultado)