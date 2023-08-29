class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        import string
        passwordl=list(password)
        if len(passwordl)>16 or len(passwordl)<8:
            return False
        if ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9') not in (passwordl):
            return False
        numeros=list('0123456789')
        for i in range(len(numeros)):
            t=password.find(numeros[i])
            if t!=-1:
                self.password=''.join(passwordl)
                passwordl.remove(numeros[i])
        if min(passwordl) in string.ascii_lowercase:
            self.password=''
            return False
        else:
            return True

    def login(self,password):
        if password==self.password:
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
           