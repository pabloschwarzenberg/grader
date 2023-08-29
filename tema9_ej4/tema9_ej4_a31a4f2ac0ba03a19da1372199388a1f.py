class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a = 8 <= len(password) <= 16
        mayusculas = "ABDCEFGHIJKLMNÑOPQRSTUVWXYZ"
        especial = "!#$%&/()=?¡'¿\|°¬,.-;:_´+¨*~{}[]^`"
        
        i = 0
        while i < len(password):
            if (password[i] in mayusculas) == True or (password[i] in especial) == True:
                b = True
                break
            elif (password[i] in mayusculas) == False and (password[i] in especial) == False:
                if i == len(password)-1:
                    b = False
                    break
                else:
                    i += 1
        if a == True and b == True:
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
           