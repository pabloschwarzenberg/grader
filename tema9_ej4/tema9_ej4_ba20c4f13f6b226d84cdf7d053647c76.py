class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""
    
    def cambiar_password(self, password):
        # Validar las reglas de la contraseña
        if len(password) < 8 or len(password) > 16:
            return False
        
        has_letter = False
        has_number = False
        has_special_char = False
        
        for char in password:
            if char.isalpha() and char.isupper():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif not char.isalnum():
                has_special_char = True
        
        if (has_letter or has_special_char) and has_number:
            self.clave = password
            return True
        
        return False
    
    def login(self, password):
        return self.clave == password

#

def decodificar(mensaje):
    # Separar los números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a decimal y luego a su correspondiente carácter ASCII
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir los caracteres y retornar el mensaje descifrado
    mensaje_descifrado = ''.join(caracteres)
    return mensaje_descifrado