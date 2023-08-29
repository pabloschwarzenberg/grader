class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        #Verificar si la pasword tiene entre 8 y 16 caracteres:
        if len(password)>= 8 and len(password)<=16:
            #pasa a revisar la siguiente condicion
            if password.isalpha() or password.isdigit():
                return False
            elif password.isalnum():
                contador = 0
                for i in range(len(password)):
                    if password[i].isupper():
                        contador += 1
                    else:
                        continue
                if contador >= 1:
                    self.password = password
                    return True
                else:
                    return False
            else:
                self.password = password
                return True
        else:
            return False

    def login(self,password):
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
           