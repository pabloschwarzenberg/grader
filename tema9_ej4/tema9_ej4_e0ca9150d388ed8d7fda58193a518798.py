class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        #print(password)
        if(len(password) < 9):
             return False
        if(len(password) > 16):
             return False
        hasLetter = False
        hasNumber = False
        hasMayus = False
        hasSpecial = False
        for letra in password:
            if(letra.isdigit()):
                hasNumber = True
                continue
            if(letra.isupper()):
                hasMayus = True
                continue
            if(letra.islower()):
                hasLetter = True
                continue
        chars = set('@#$%^&+=,._')
        if any((c in chars) for c in password):
            hasSpecial = True
        #print("hasLetter: %r"% hasLetter)
        #print("hasNumber: %r"% hasNumber)
        #print("hasMayus: %r"% hasMayus)
        #print("hasSpecial: %r"% hasSpecial)
        if(hasLetter and hasNumber and hasMayus or hasSpecial):
            self.password = password
            return True
        return False

    def login(self,password):
        if(self.password == password):
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
           
