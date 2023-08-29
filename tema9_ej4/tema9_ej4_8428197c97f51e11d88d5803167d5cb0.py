class Usuario:
    def _init_(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        length = len(password)
        has_uppercase = False
        has_special_character = False

        # Verificamos si la password cumple las reglas
        if length < 8 or length > 16:
            return False
        
        for char in password:
            if char.isupper():
                has_uppercase = True
            elif not char.isalpha() and not char.isdigit():
                has_special_character = True

        if not has_uppercase and not has_special_character:
            return False

        # Si cumple las reglas, actualizamos la clave
        self.clave = password
        return True

    def login(self, password):
        # Comparamos la password ingresada con la clave
        if password == self.clave:
            return True
        else:
            return False
