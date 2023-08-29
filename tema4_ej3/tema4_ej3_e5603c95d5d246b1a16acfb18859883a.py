def jerigonzo(texto):
    resultado = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    return resultado
if name == "main":
  texto_original = input("Ingrese un texto: ")
  texto_traducido = jerigonzo(texto_original)
  print("Texto traducido a jerigonzo:", texto_traducido)