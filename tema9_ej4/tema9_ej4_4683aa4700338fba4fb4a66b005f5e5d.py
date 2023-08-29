class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        
        letras_min = 'abcdefghijklmnñopqrstuvwxyz'
        letras_may = letras_min.upper()
        nums = '0123456789'

        reglas = 0

        for caracter in password:
            if caracter in letras_min:
                reglas += 1
            
            if caracter in letras_may:
                reglas += 1
            
            if caracter in nums:
                reglas += 1

            if caracter not in letras_may or caracter not in letras_min or caracter not in nums:
                reglas += 1
            
        if reglas <2:
            self.password = password
            return True
        
        return False

    def login(self,password):
        return True if password == self.password else False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))