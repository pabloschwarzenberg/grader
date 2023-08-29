def rot13(palabra):
    abecedario=("abcdefghijklmnopqrstuvwxyz")
    rota13=("nopqrstuvwxyzabcdefghijklm")
    texto_temporal=list(palabra)
    palabraenrot13=[]
    for patio in texto_temporal:
        encontrar_palabra=abecedario.find(patio)
        palabraenrot13.append(rota13[encontrar_palabra])
    terminada="".join(palabraenrot13)
    return(terminada)