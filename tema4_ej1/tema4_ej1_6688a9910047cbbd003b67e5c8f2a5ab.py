import random
def ocultar_letras(palabra,cantidad):
    n = cantidad
    palabra_enlistada = list(palabra)
    i = 0
    while i < n:
        letra = random.choice(palabra_enlistada)
        while letra == "_":
            letra = random.choice(palabra_enlistada)
        posicion_letra = palabra_enlistada.index(letra)
        palabra_enlistada.pop(posicion_letra)
        palabra_enlistada.insert(posicion_letra,"_")
        i += 1
    palabra_ocultada = "".join(palabra_enlistada)
    return palabra_ocultada

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta_enlistada = list(palabra_secreta)
    palabra_enlistada = list(palabra)
    if letra in palabra_secreta_enlistada:
        if palabra_secreta_enlistada.count(letra) > 1:
            posiciones = []
            for i in range(len(palabra_secreta_enlistada)):
                if palabra_secreta_enlistada[i] == letra:
                    posiciones.append(i)
            for l in posiciones:
                palabra_enlistada.pop(l)
                palabra_enlistada.insert(l,letra)
        else:
            posicion_letra = palabra_secreta_enlistada.index(letra)
            palabra_elistada.pop(posicion_letra)
            palabra_enlistada.insert(posicion_letra,letra)
    palabra_modificada = "".join(palabra_enlistada)
    return palabra_modificada
    if letra not in palabra_secreta_enlistada:
        return "La letra no se encuentra en la palabra"
                    

