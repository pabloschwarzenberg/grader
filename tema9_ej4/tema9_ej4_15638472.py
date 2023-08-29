class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>16 or len(password)<8:
            return False
        elif "1" not in password:
            return False
        else:
            if "_" not in password:
                if "S" not in password:
                    return False
                else:
                    return True
                    self.password=password
            elif "S" not in password:
                if "_" not in password:
                    return False
                else:
                    return True
                    self.password=password
        pass

    def login(self,password):
        if self.password==password:
            return True
        else:
            return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))