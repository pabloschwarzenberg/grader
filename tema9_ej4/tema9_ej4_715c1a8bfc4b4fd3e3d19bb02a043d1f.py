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

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            return False
        if not any(char.isupper() for char in password) and not any(not char.isalnum() for char in password):
            return False
        return True

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False (No cumple la longitud mínima)
    print(usuario.cambiar_password("clavesecreta1_"))  # True (Cumple todas las reglas)
    print(usuario.cambiar_password("clavesecreta"))  # False (No contiene una letra mayúscula o carácter especial)
    print(usuario.cambiar_password("clasesecreta1"))  # False (No contiene una letra mayúscula o carácter especial)
    print(usuario.cambiar_password("claveSecreta1"))  # True (Cumple todas las reglas)
    print(usuario.login("clavesecreta1_"))  # True (Contraseña válida)
    print(usuario.login("claveSecreta1"))  # False (Contraseña inválida)
