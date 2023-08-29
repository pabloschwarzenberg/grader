class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        todo_ok = False
        carac = 0
        CARAC = 0
        numer = 0
        no_ca = 0
        for i in password:
            if i in 'QWERTYUIOPASDFGHJKLÑZXCVBNM':
                CARAC += 1
            elif i in 'qwertyuiopasdfghjklñzxcvbnm':
                carac += 1
            elif i in '1234567890':
                numer += 1
            else:
                no_ca += 1
        if (CARAC + carac > 0 and numer > 0) and (CARAC > 0 or no_ca > 0):
            todo_ok = True
        if 8 <= len(password) <= 16 and todo_ok:
            self.password = password
            return True
        return False

    def login(self, password):
        return password == self.password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
