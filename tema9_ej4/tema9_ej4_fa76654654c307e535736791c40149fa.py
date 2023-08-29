class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        dig=False
        upper=False
        lower=False
        alnum=False
        for carac in password:
            if carac.isdigit()==True:
                dig=True
            if carac.isupper()==True:
                upper=True
            if carac.islower()==True:
                lower=True
        if password.isalnum()==False:
            alnum=True
        if dig==True and upper==True and lower==True:
            return True
        elif dig==True and alnum==True and lower==True:
            return True
        else:
            return False

    def login(self, password):
        if password == self.password:
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
           