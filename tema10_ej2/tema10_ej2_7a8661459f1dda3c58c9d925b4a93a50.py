def levenshtein(palabra1,palabra2):

    cont = 0
    for i in range(0,len(palabra1)):
        if palabra1[i] in palabra2:
            cont += 1
    
    salida = ""

    aux = cont
    cont = len(palabra1)-cont
    if aux > 1:
        salida = "+1"
    if ((len(palabra2)-1) == aux) or ((len(palabra2)+1) == aux):
        salida = "IB"
    if (len(palabra2)-1) == aux and cont == 1:
        salida = "1S"

    if palabra1 == palabra2:
        salida = "0D"
    return salida
