def decodificar(mensaje):
  string_final = ""
  mensaje = mensaje.split(",")
  for i in mensaje:
    k_letra = 0
    for letra in i:
          if letra == "0":
              k_letra = k_letra*2
          if letra == "1":
              k_letra = (k_letra*2)+1
    print(k_letra)   
    string_final += chr(k_letra)
  return string_final


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         