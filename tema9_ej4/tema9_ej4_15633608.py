class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        tamano=False
        contiene=False
        minicontiene2=False
        minicontiene3=False
        minicontiene4=False
        if len(password)>=8 and len(password)<=16:
            tamano=True
        for i in password:
            if i.isdigit():
                minicontiene2=True
            if i.isalpha():
                minicontiene3=True
            if i.isupper() or (not i.isdigit()) and (not i.isalpha()):
                minicontiene4=True
        if minicontiene2 and minicontiene3 and minicontiene4:
            contiene=True
        if tamano and contiene:
            self.password=password
            return True
        else:
            return False 
        pass

    def login(self,password):
        if self.password == password:
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
           