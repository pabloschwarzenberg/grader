def decodificar(mensaje):
    letras = mensaje.split(",")
    letrasDecodificadas = []
    for palabra in letras:
      contador = 0
      for j in range (0,8):
        contador += int(palabra[j])*(2**(7-j))
      letrasDecodificadas.append(chr(contador))
    mensaje = ""
    for letra in letrasDecodificadas:
        mensaje += letra
      
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         