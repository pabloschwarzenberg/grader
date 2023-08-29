class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"
        mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        simbolos = "#$%&*+-_.,<>"
        num = 0
        letras = 0
        simb = 0
        mayus = 0
        if len(password)<=16 and len(password)>=8:
            for i in range(0, len(password)):
                if abecedario.find(password[i]) != -1:
                    letras += 1
                if mayusculas.find(password[i]) != -1:
                    mayus += 1
                if numeros.find(password[i]) != -1:
                    num += 1
                if simbolos.find(password[i]) != -1:
                    simb += 1
            if num != 0 and letras != 0:
                if simb != 0 or mayus != 0:
                    self.password+=password
                    return True
                else:
                    return False
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
           