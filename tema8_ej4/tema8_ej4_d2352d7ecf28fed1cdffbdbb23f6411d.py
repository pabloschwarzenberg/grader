def rot13(palabra):
    l1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    l2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    l_palabra=list(palabra)
    palabra_final=[""]
    for letra in l_palabra:
        if letra in l1:
            n=ord(letra)+13
            letra_nueva=chr(n)
            palabra_final.append(letra_nueva)
        elif letra in l2:
            n=ord(letra)-13
            letra_nueva=chr(n)
            palabra_final.append(letra_nueva)
    palabra_final="".join(palabra_final)
    return palabra_final

if __name__=="__main__":
    pass
           