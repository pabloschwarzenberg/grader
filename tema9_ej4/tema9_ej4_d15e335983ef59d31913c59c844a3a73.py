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
        has_special = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_uppercase = True
            elif char.isalpha() and char.islower():
                has_letter = True
            elif char.isdigit():
                has_number = True
            else:
                has_special = True

        if (has_letter or has_number) and (has_uppercase or has_special):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return self.password == password

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  
    print(usuario.cambiar_password("clavesecreta1_"))  
    print(usuario.cambiar_password("clavesecreta"))  
    print(usuario.cambiar_password("clasesecreta1"))  
    print(usuario.cambiar_password("claveSecreta1"))  
    print(usuario.login("clavesecreta1_"))  
    print(usuario.login("claveSecreta1"))