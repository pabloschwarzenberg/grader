def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    
 def decode(message):
    menssage_separated_by_comma = message.split(",")
    message_result = ""
    for binary_character in menssage_separated_by_comma:
        value_variable = int(binary_character,2)
        message_result += chr(value_variable)
    return message_result
         