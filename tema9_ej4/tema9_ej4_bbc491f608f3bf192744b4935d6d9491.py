class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password) < 8 or len(password) > 16:
            return False

        contiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password)
        contiene_mayusculas_o_especiales = any(char.isupper() or not char.isalnum() for char in password)

        if not contiene_letras_numeros or not contiene_mayusculas_o_especiales:
            return False

        self.password = password
        return True

    def login(self,password):
        return password == self.password

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           