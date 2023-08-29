class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if self._validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def _validar_password(self, password):
        # Reglas de validación de la contraseña
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        if not any(char.isupper() or not char.isalnum() for char in password):
            return False
        return True

    def login(self, password):
        return password == self.clave
