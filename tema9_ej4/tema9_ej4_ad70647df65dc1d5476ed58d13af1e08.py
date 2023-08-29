class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
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

        return False

    def login(self, password):
        return password == self.clave

usuario = Usuario("John Doe", "johndoe@example.com")
print(usuario.cambiar_password("Password1#"))  # True
print(usuario.login("Password1#"))  # True
print(usuario.login("WrongPassword"))  # False

           