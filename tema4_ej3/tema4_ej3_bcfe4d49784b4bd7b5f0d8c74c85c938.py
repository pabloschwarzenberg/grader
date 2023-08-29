def jerigonzo(string):
    vowels = "aeiouAEIOU"
    jerigonzo_text = ""
    for letter in string:
        if letter in vowels:
            jerigonzo_text += letter + "p" + letter.lower()
        else:
            jerigonzo_text += letter
    return jerigonzo_text

    
if __name__ == "__main__":
  texto = input("Ingrese un texto: ")
  resultado = jerigonzo(texto)
  print("Texto original:", texto)
  print("Texto en jerigonzo:", resultado)