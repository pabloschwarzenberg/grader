class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        contador = 0
        num = '0123456789'
        abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        simbolos = '<>¡!#$%/&*()_+=-¿?ç[«¢∞|°£≠–±]|ª¶~•…Ÿ{’”»}'
        for letras in password:
            busqueda_numero = num.find(letras)
            if busqueda_numero != -1:
                contador += 1
                break

        for letras in password:
            busqueda_mayuscula = abecedario.find(letras)
            busqueda_simbolo = simbolos.find(letras)
            if busqueda_mayuscula != -1 or busqueda_simbolo != -1:
                contador += 1
                break

        if contador == 2:
            self.password = password
            return True
        else:
            return False
        pass

    def login(self,password):
        if password == self.password:
            return True
        else:
            return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           