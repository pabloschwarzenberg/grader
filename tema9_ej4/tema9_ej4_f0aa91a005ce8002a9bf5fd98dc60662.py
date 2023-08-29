class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password = str(password)
        caracteres_especiales = "_#%-QWERTYUIOPASDFGHJKLZXCVBNM"
        numeros = "12345667890"
        if len(password) < 8 or len(password) > 16:
            return False
        for k in password :
            if caracteres_especiales.find(k) != -1 :
                for y in password:
                   if numeros.find(y) !=-1:
                         self.password = password
                         return True
        return False
    def login(self,password):
        password = str(password)
        if password != self.password:
         return False
        else :
            return True

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           