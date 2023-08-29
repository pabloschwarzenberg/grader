class Usuario:
    def __init__(self,nombre ,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self, password): #se adquiere el nuevo valor de la contraseña.
        tieneletra= False
        tienenum= False
        tienemayu= False
        tienecaracteresespceciales= False
        if 8<len(password)<16:
            for letra in password:
                if letra.isalpha(): #si coincide con isalpha, significa que es verdadero.
                    tieneletra= True
                if letra.isdigit():
                    tienenum= True
                if letra.isupper():
                    tienemayu= True
                if (32<=ord(letra)<=47) or (58<=ord(letra)<=64) or (91<=ord(letra)<=96) or (123<=ord(letra)<=1):
                    tienecaracteresespceciales= True
            if tieneletra and tienenum and (tienemayu or tienecaracteresespceciales):
                self.password= password
                return True
            else:
                return False
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