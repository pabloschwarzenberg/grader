# Definir una función que reciba una palabra y la retorne encriptada usando el cifrado ROT13
def rot13(palabra):
    # Crear una lista con las letras del alfabeto
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # Crear una lista vacía para guardar la palabra encriptada
    encriptada = []
    # Recorrer cada letra de la palabra
    for letra in palabra:
        # Si la letra es mayúscula, buscar su posición en el alfabeto
        if letra.isupper():
            posicion = alfabeto.index(letra)
            # Desplazar la posición 13 lugares a la derecha, usando el módulo 26 para evitar salirse del rango
            nueva_posicion = (posicion + 13) % 26
            # Obtener la letra correspondiente a la nueva posición y agregarla a la lista de encriptación
            nueva_letra = alfabeto[nueva_posicion]
            encriptada.append(nueva_letra)
        # Si la letra es minúscula, convertirla a mayúscula y repetir el mismo proceso
        elif letra.islower():
            posicion = alfabeto.index(letra.upper())
            nueva_posicion = (posicion + 13) % 26
            nueva_letra = alfabeto[nueva_posicion].lower()
            encriptada.append(nueva_letra)
        # Si la letra no es alfabética, agregarla sin modificar
        else:
            encriptada.append(letra)
    # Unir las letras de la lista en una sola cadena y retornarla
    return "".join(encriptada)

# Probar la función con algunos ejemplos
if __name__ == "__main__":
    print(rot13("Hola")) # Debe imprimir Ubyn
    print(rot13("ROT13")) # Debe imprimir EBG13
    print(rot13("Python")) # Debe imprimir Clguba
