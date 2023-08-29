def rot13(texto):
    mayuscula=("ABCDEFGHYJKLMNOPQRSTUVWXYZABCDEFGHYJKLM")
    minuscula=("abcdefghijklmnopqrstuvwxyzabcdefghijklm")
    x=""
    for h in texto:
        if (h in mayuscula):
            x=x+mayuscula[mayuscula.find(h)+13]
        elif (h in minuscula):
            x=x+minuscula[minuscula.find(h)+13]
        else:
            x=x+h

    return x
if __name__=="__main__":
 texto=input("texto:")
 print(rot13(texto))

           