def decodificar(mensaje):
    n_binarios = mensaje.split(',')
    letras = [chr(int(n_binario, 2)) for n_binario in n_binarios]
    m_descifrado = ''.join(letras)
    return m_descifrado
         