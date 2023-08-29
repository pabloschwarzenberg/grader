def buscarTodas(a,b):
    contador = 0
    lugares = ""
    for i in a:
       if i == b:
         lugares += str(contador)
         lugares += " "
         contador += 1
       else:
         contador += 1

    lugares_sin_espacio = (lugares.rstrip())
    return lugares_sin_espacio