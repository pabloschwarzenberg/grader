def rot13(palabra):
    abecedario=("abcdefghijklmnopqrstuvwxyz")
    rotacion13=("nopqrstuvwxyzabcdefghijklm")
    texto_temporal=list(palabra)
    palabra_rot13=[]
    for frase in texto_temporal:
        encontrar_palabra=abecedario.find(frase)
        palabra_rot13.append(rotacion13[encontrar_palabra])
    fin="".join(palabra_rot13)
    return(fin)