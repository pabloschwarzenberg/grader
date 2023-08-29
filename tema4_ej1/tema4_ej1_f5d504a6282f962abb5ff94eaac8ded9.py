import random

def ocultar_letras(palabra, cantidad):
    # Convierte la palabra en una lista de caracteres
    letras = list(palabra)
    
    # Genera una lista de índices aleatorios
    indices_ocultos = random.sample(range(len(letras)), cantidad)
    
    # Reemplaza las letras en los índices ocultos por "_"
    for indice in indices_ocultos:
        letras[indice] = "_"
    
    # Une los caracteres de la lista en una cadena
    palabra_oculta = "".join(letras)
    
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convierte las palabras en listas de caracteres
    letras_secretas = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)
    
    # Revisa si la letra está en la palabra secreta
    for i in range(len(letras_secretas)):
        if letras_secretas[i] == letra:
            letras_mostradas[i] = letra
    
    # Une los caracteres de las listas en cadenas
    nueva_palabra_mostrada = "".join(letras_mostradas)
    
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    
    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            
            if letras_mostradas == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break
        else:
            print("¡Incorrecto! Inténtalo de nuevo.")
        
        intentos -= 1
        
    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)
