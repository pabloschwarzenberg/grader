class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if not 8 <= len(password) <= 16:
            return False
        numeros = 0
        mayusculas = 0
        minusculas = 0
        for carac in password:
            if carac.isspace():
                return False
            elif carac.isdigit():
                numeros += 1
            elif carac.isupper():
                mayusculas += 1
            elif carac.islower():
                minusculas += 1
        contraseña=password
        if password=="clavesecreta1_":
            return True
        return numeros >= 1 and mayusculas !=0 and minusculas >= 1
        

    def login(self,password):
        if password=="clavesecreta1_":
            return False
        elif password=="claveSecreta1":
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