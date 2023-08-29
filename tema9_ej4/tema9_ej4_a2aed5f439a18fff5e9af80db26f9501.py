class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        cambiar = False
        largo = False
        numeros = False
        letras = False
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        mayusc = False
        if len(password)<8 or len(password)>16:
            largo = False
        else:
            largo = True
        for i in range(len(password)):
            if password[i].isdigit():
                numeros = True
            if password[i].isalpha():
                letras = True
            if password[i] in mayusculas:
                mayusc = True
        if largo and numeros and letras and mayusc:
            cambiar = True

        return cambiar
    def login(self, password):
        login = False
        if password == self.password:
            login = True
        return login


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))