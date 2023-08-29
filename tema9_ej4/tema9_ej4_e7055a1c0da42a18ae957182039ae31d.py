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

        if (has_letter and has_number) and (has_uppercase or has_special_char):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
usuario1 = Usuario("JohnDoe", "johndoe@example.com")
print(usuario1.nombre)     # Imprime "JohnDoe"
print(usuario1.email)      # Imprime "johndoe@example.com"
print(usuario1.clave)      # Imprime ""

usuario1.cambiar_password("Passw0rd#")
print(usuario1.clave)      # Imprime "Passw0rd#"

print(usuario1.login("Passw0rd#"))  # Imprime True
print(usuario1.login("incorrect"))  # Imprime False
