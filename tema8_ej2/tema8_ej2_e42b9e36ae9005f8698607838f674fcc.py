def buscarTodas(a, b):
    if a.find(b) == -1:
        return ''
    else:
        apariciones = []
        inicio = 0
        fin = len(b)
        while fin < len(a):
            if a[inicio:fin] == b:
                apariciones.append(str(inicio))
            inicio += 1
            fin += 1
    return ' '.join(apariciones)

if __name__ == "__main__":
    pass
           