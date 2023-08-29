# Todas las aprariciones del string b en el string a
def buscarTodas(a, b):
    frase = list(a)
    lugares = []
    for i in frase:
        lugar = frase.index(i)
        lugar = str(lugar)
        if i == b:
            lugares.append(lugar)
            frase.remove(i)
            lugar = int(lugar)
            frase.insert(lugar," ")
        else:
            continue
    lugares_final = []
    for k in lugares:
        lugar_final = lugares.index(k)
        if lugar_final == len(lugares) - 1:
            lugares_final.append(k)
        else:
            lugares_final.append(k)
            lugares_final.append(" ")
    lugares_final = "".join(lugares_final)
    return lugares_final

if __name__ == "__main__":
    pass