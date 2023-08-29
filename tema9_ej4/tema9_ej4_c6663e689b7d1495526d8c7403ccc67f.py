class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        largo=0
        letra=0
        numero=0
        mayuscula=0
        especial=0
        if len(password)>=8 and len(password)<=16:
            largo=1
        for i in password:
            if i.isalpha():
                letra+=1
            if i.isnumeric():
                numero+=1
            if i.isupper():
                mayuscula+=1
            if not i.isalnum():
                especial+=1
        if largo!=0 and letra!=0 and numero!=0 and (mayuscula!=0 or especial!=0):
            self.password=password
            return(True)
        else:
            return(False)
    def login(self,password):
        if self.password==password:
            return(True)
        else:
            return(False)

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           