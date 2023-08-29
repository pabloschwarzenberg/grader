abcedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "*", "(", ")", "_", "-"]


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        confirmación = False
        caracteres = False
        especial = 0
        for i in password:
            for j in abcedario:
                j = j.upper()
                print(j, "comparando", i)
                if i == j:
                    especial = 1
                    break
            for j in caracteres_especiales:
                if i == j:
                    especial = 1
                    break
        if especial >= 1:
            caracteres = True
        if 8 <= len(password) <= 16 and caracteres:
            self.password = password
            confirmación = True
            print(password)
        return confirmación

    def login(self, password):
        if password == self.password:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("clavesecreta1")) 