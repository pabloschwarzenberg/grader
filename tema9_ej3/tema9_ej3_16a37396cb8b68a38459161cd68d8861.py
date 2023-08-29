def decodificar(mensaje):
    binario = ''
    while mensaje // 2 != 0:
        binario = str(mensaje % 2) + binario
        mensaje = mensaje // 2
    return str(mensaje) + binario

if __name__ == "__main__":
    pass        
         