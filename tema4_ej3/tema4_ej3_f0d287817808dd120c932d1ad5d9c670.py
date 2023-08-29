if __name__ == "__main__":
  palabra=input("Ingrese una palabra: ")
  
palabra_final=""
  
def jerigonzo(palabra):
    global palabra_final
    
    for letra in palabra:
        if letra in "aeiouAEIOU":
            palabra_final += letra
            palabra_final += "p"
        palabra_final += letra
    return palabra_final
    
if __name__ == "__main__":
    respuesta=jerigonzo(palabra)  
    print(respuesta)
         