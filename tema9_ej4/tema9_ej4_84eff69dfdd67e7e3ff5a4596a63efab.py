class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return password == self.password

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letters = False
        has_numbers = False
        for char in password:
            if char.isalpha():
                has_letters = True
            elif char.isdigit():
                has_numbers = True

        if not has_letters or not has_numbers:
            return False

        has_uppercase = any(char.isupper() for char in password)
        has_special = any(not char.isalnum() for char in password)

        if not has_uppercase and not has_special:
            return False

        return True


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))           
    print(usuario.cambiar_password("clavesecreta1_"))    
    print(usuario.cambiar_password("clavesecreta"))     
    print(usuario.cambiar_password("clasesecreta1"))     
    print(usuario.cambiar_password("claveSecreta1"))   
    print(usuario.login("clavesecreta1_"))                
    print(usuario.login("claveSecreta1"))               


