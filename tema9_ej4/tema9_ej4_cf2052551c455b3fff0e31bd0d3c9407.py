import re
s='[@_!#$%^&*()<>?/\|}{~:]'

class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""
        self.val = True

    def cambiar_password(self, password):
        p = password
        x = True
        a = 0
        b = 0

        while x:
            if (len(p) < 8 or len(p) > 16):
                break
            elif not re.search("[a-z]", p):
                break
            elif not re.search("[0-9]", p):
                break
            elif (not (re.search(s, p) ) and not any(char.isupper() for char in password)):
                a = 1       
                break

            elif re.search('\s', p):
                break
            elif a + b == 2:
                break
            else:
                
                x = False
                self.password = password
                print(password)
                return True
        if x:
            return False


    def login(self, password):
        if password == self.password:
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
           