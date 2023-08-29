def buscarTodas(a,b):
    contador=0
    string = ''
    for i in a:
        if i==b:
            string = string + str(contador) + ' '
        contador += 1
    return string.strip()


if __name__ == "__main__":
    pass
           