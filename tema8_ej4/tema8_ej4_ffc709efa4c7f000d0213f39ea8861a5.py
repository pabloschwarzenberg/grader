def rot13(palabra):
    letras=("abcdefghijklmnopqrstuvwxyz")
    rotacion13=("nopqrstuvwxyzabcdefghijklm")
    texto_temporal=list(palabra)
    palabraenrot13=[]
    for casita in texto_temporal:
        averiguar_palabra=letras.find(casita)
        palabraenrot13.append(rotacion13[averiguar_palabra])
    terminada="".join(palabraenrot13)
    return(terminada)