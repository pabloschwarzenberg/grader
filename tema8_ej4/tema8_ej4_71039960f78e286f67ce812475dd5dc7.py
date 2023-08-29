def rot13(palabra):
  abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rot_13_abc = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
  palabra_tmp = ""
  for i in range(len(palabra)):
    indice = abecedario.index(palabra[i])
    palabra_tmp += rot_13_abc[indice]
  return palabra_tmp
  
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)