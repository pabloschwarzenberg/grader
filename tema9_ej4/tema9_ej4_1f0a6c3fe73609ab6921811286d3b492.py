class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

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
        
        if has_letter and (has_number or has_special_char) and (has_uppercase or has_special_char):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False
    print(usuario.cambiar_password("clavesecreta1_"))  # True
    print(usuario.cambiar_password("clavesecreta"))  # False
    print(usuario.cambiar_password("clasesecreta1"))  # False
    print(usuario.cambiar_password("claveSecreta1"))  # True
    print(usuario.login("clavesecreta1_"))  # True
    print(usuario.login("claveSecreta1"))  # False
    