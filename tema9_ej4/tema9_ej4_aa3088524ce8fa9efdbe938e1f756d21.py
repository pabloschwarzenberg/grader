class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password) < 8 or len(password) > 16:
            return False
        Tiene_letra= False
        Tiene_numero= False
        Tiene_mayuscula= False
        Tiene_caracter_especial= False

        for caracter in password:
            if caracter.isalpha():#materia nueva
                Tiene_letra= True
                if caracter.isupper():#materia nueva
                    Tiene_mayuscula= True
            elif caracter.isdigit():#materia nueva
                Tiene_numero= True
            else:
                Tiene_caracter_especial= True

        if Tiene_letra and Tiene_numero and (Tiene_caracter_especial or Tiene_mayuscula):
            self.clave = password
            return True

        return False

    def login(self,password):
        return self.password == password

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           