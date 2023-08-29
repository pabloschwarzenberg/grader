class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=0
        digitos=0
        letras=0
        mayusculas=0
        caracteres_especiales=0
        for i in password:
            if i.isdigit():
                digitos+=1
            elif i.isalpha():
                letras+=1
                if i.isupper():
                    mayusculas+=1
        caracteres_especiales = len(password) - letras - digitos
        if letras > 0 and digitos > 0 and len(password)>7 and len(password) < 17 and (mayusculas > 0 or caracteres_especiales > 0):
            self.password=password
            return True
        else:
            return False

    def login(self,password):
        if password == self.password:
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

