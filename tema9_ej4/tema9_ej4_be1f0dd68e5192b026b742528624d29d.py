class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        contador=0
        contador_a=0
        contador_b=0
        contador_c=0
        contador_d=0
        tamano=len(password)
        if (tamano>=8 and tamano<=16):
            for i in password:
                if i.isalpha():
                    contador=contador+1
                if (i.isalpha()==False and i.isdigit()==False):
                    contador_a=contador_a+1
                if i.isupper():
                    contador_b=contador_b+1
                if i.isdigit():
                    contador_c=contador_c+1
            if (contador_b>=1 or contador_a>=1):
                contador_d=contador_d+1
            if (contador>=1 and contador_d==1 and contador_c>=1):
                self.password=password
                return True
            else:
                return False
        else:
            return False
        pass
    def login(self,password):
        if (self.password==password):
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
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           