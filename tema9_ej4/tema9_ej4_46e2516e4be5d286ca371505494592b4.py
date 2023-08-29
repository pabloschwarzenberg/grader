#Usuario de Twitter

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        nuevo_Usuario = Usuario(self.nombre, self.email)
        if len(password)>=8 and len(password)<=16: ##Largo
            if password.isalpha()==False:       ##Que contenga letras y numeros
                if password.islower()==False or password.isalnum()==False: #Al menos una mayuscula o caracter especial
                    Usuario.password=password
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def login(self,password):
        if self.password==password:
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