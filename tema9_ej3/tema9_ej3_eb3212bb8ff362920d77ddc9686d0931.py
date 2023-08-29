class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_uppercase = True
            if not char.isalnum() and char != '#':
                has_special_char = True

        if has_uppercase or has_special_char:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password