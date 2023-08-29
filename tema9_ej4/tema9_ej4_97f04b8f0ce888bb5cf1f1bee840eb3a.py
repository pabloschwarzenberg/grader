class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        Alfabeto_May = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        Alfabeto_Min = "abcdefghijlmnñopqrstuvwxyz"
        Numeros = "0123456789"

        Largo = len(password)
        Numero = False
        Letra = False
        Minuscula = False
        Mayuscula = False
        Caracter_Especial = False


        for Caracter in password:
            if Caracter in Alfabeto_May:
                Mayuscula = True
                Letra = True
            elif Caracter in Alfabeto_Min:
                Minuscula = True
                Letra = True
            elif Caracter in Numeros:
                Numero = True
            else:
                Caracter_Especial = True
        if Largo >= 8 and Largo <= 16:
            if Letra == True and Numero == True:
                if Mayuscula == True or Caracter_Especial == True:
                    self.password = password
                    return True
                else:
                    return False
            else:
                return False
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
           