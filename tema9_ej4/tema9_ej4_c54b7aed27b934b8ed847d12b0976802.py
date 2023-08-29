class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        c=len(password)
        numeros=0
        letras=0
        if c<=16 and c>=8:
            for carct in password:
                if carct.isnumeric():
                    numeros=numeros+1
                elif carct.isalpha() and carct.islower():
                    letras=letras+1
            if numeros+letras != c:
                self.password=password
                return True
        return False
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
           