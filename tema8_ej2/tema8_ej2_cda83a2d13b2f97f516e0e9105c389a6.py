def buscarTodas(a,b):
    aparicion = ''
    i = 0
    for letra in a:
        if letra == b :
            c = a.find(b,i)
            aparicion += str(c)+" "
        i += 1
    aparicion_final = aparicion.strip()
    return aparicion_final

if __name__ == "__main__":
    pass
           