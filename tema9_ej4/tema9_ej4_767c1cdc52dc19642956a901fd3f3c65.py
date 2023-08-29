class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letras="abcdefghijklmnopqrstuvwxyzñ"
        num="0123456789"
        count=""
        if 8<=len(password)<=16:
            for i in range(len(password)):
                if password[i] in letras:
                    count+="l"
                if password[i] in num:
                    count+="n"
        else:
            return False
        if len(password)>=len(count):
            if "l" in count:
                if "n" in count:
                    if len(password)>len(count):
                        self.password=password
                        return True
                    if len(password)==len(count):
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    def login(self,password):
        if password==self.password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           