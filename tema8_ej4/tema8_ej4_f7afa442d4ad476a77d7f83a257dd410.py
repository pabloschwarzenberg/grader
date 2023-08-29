def rot13(palabra):
    abecedario=("abcdefghijklmnopqrstuvwxyz")
    rotacion13=("nopqrstuvwxyzabcdefghijklm")
    texto_temporal=list(palabra)
    palabraenrot13=[]
    for tetera in texto_temporal:
        encontrar_palabra=abecedario.find(tetera)
        palabraenrot13.append(rotacion13[encontrar_palabra])
    terminada="".join(palabraenrot13)
    return(terminada)