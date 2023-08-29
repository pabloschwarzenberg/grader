class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letter = False
        has_number = False
        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha():
                has_letter = True
                if char.isupper():
                    has_uppercase = True
            elif char.isdigit():
                has_number = True
            else:
                has_special_char = True

        if has_letter and (has_number or has_special_char) and has_uppercase:
            self.clave = password
            return True

        return False

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
if __name__ == "__main__":
    usuario = Usuario("ejemplo", "ejemplo@example.com")
    print(usuario.login("password"))  # False, clave vacía
    print(usuario.cambiar_password("password"))  # False, no cumple las reglas
    print(usuario.login("password"))  # False, clave no actualizada

    print(usuario.cambiar_password("Password1#"))  # True, cumple las reglas
    print(usuario.login("Password1#"))  # True, clave actualizada
