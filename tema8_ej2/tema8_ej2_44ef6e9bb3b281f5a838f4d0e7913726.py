def buscarTodas(a, b):
    apariciones = []
    for i in range(0, len(a)):
        if a[i] == b:
            apariciones.append(str(i))
    
    return ' '.join(apariciones)

if __name__ == "__main__":
    pass
           