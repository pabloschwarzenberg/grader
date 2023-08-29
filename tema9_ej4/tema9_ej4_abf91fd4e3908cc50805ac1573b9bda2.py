class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):

        Upper = 0
        Especial = 0

        if len(password) < 8 or len(password) > 16:

            return False

        if 8 <= len(password) <= 16:

            for i in password:

                if i.isupper():

                    Upper += 1

                if not i.isupper() and not i.islower() and not i.isdigit():

                    Especial += 1

            if Upper != 0 or Especial != 0:

                self.password = password
                
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
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           