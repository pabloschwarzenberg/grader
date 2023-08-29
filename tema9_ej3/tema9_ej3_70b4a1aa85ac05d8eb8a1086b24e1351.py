def decodificar(mensaje):
    menssage_separated_by_comma = mensaje.split(",")
    mensaje = ""
    for binary_character in menssage_separated_by_comma:
        value_variable = int(binary_character,2)
        mensaje += chr(value_variable)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         