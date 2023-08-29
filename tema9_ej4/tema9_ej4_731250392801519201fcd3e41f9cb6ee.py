class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        caracteres_raros = ["_"]
        verif_caracter_raro = False
        verif_numero = False
        verif_mayuscula = False
        verif_minusculas = False
        for letra in password:
            if letra.isdigit():
                verif_numero = True
            if letra.isupper():
                verif_mayuscula = True
            if letra in caracteres_raros:
                verif_caracter_raro = True
            if letra.islower():
                verif_minusculas = True
        if verif_numero == True:
            if verif_mayuscula or (verif_minusculas and verif_caracter_raro):
                return True
            else:
                return False
        else:
            return False

    def login(self,password):
        if self.password==password:
           return True
        else:
             return False

               
   

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("clave*Secreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           