from collections import defaultdict


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if not 8 <= len(password) <= 16:
            return False
        char_count = {"alpha": 0, "num": 0, "special": 0, "upper": 0, "lower": 0}
        for char in password:
            if char.isalpha():
                char_count["alpha"] = char_count["alpha"] + 1
            if char.isdigit():
                char_count["num"] = char_count["num"] + 1
            if not char.isalnum():
                char_count["special"] = char_count["special"] + 1
            if char.isupper():
                char_count["upper"] = char_count["upper"] + 1
            if char.islower():
                char_count["lower"] = char_count["lower"] + 1

        if not char_count["alpha"] > 0:
            return False
        if not char_count["num"] > 0:
            return False
        if not (char_count["upper"] > 0 or char_count["special"] > 0):
            return False
        self.password = password
        return True

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

           