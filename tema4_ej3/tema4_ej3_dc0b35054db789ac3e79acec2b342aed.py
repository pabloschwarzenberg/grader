# Definir una función que reciba un texto y retorne el mismo texto traducido a jerigonzo
def jerigonzo(texto):
    # Crear una lista con las vocales
    vocales = ["a", "e", "i", "o", "u"]
    # Crear una lista vacía para guardar el texto traducido
    traduccion = []
    # Recorrer cada letra del texto
    for letra in texto:
        # Agregar la letra a la lista de traducción
        traduccion.append(letra)
        # Si la letra es una vocal, agregar una p y repetir la vocal
        if letra.lower() in vocales:
            traduccion.append("p")
            traduccion.append(letra)
    # Unir las letras de la lista en una sola cadena y retornarla
    return "".join(traduccion)

# Probar la función con algunos ejemplos
if __name__ == "__main__":
    print(jerigonzo("Hola")) # Debe imprimir Hopolapa
    print(jerigonzo("Jerigonzo")) # Debe imprimir Jeperipigoponzopo
    print(jerigonzo("Universidad")) # Debe imprimir Upunipiversipidapad
