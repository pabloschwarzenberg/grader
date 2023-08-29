class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.clave=''
        self.email=email

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            if ('a' in password or 'b' in password or 'c' in password or 'd' in password or 'e' in password or 'f' in password or 'g' in password or 'h' in password or 'i' in password or 'j' in password or 'k' in password or 'l' in password or 'm' in password or 'n' in password or 'o' in password or 'p' in password or 'q' in password or 'r' in password or 's' in password or 't' in password or 'u' in password or 'v' in password or 'w' in password or 'x' in password or 'y' in password or 'z' in password) and ('0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password) and ('#' in password or '$' in password or '%' in password or '&' in password or '/' in password or '.' in password or '-' in password or ',' in password or '_' in password or 'S' in password):

                self.clave=password
                return True
            else:
                return False
        return False
    def login(self,password):
        if self.clave==password:
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
