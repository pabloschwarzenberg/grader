class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letras = 'abcdefghijklmnopqrstuvwxyz'
        numeros = '0123456789'
        ln = letras + numeros
        if 8 < len(password) < 16:
            for i in range(9):
                if password.find(i) != -1:
                    for a in letras:
                        if password.find(a) != -1:
                            for b in letras.upper():
                                for c in ln:
                                    if password.find(b) != -1 or password.find(c) == -1:
                                        self.password.append(password)
                                        return True
        else:
            return False


    def login(self,password):
        if self.password == password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           