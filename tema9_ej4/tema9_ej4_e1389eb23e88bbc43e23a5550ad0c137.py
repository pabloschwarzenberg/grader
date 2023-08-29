class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            letras=False
            num=False
            may=False
            carac=False
            especiales="!?¿¡@,.;#$%&_"

            for i in password:
                if i in especiales:
                    carac=True
                if i==i.upper():
                    may=True
                if i.isdigit():
                    num=True
                if not i.isdigit() and i not in especiales:
                    letras=True

            if (letras==True and num==True) and carac==True or may==True:

                self.password=password
                return True
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
    print(usuario.cambiar_password("clavesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))