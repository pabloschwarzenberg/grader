class Usuario:
    def __init__(self,nombre,email):
        self.letrasmin = "abcdefghijklmnopqrstuvwxyz"
        self.letrasmay = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeros = "1234567890"
        self.caract = "#.,:;-_´¨^`[]+*¿¡}çÇ{?'=()/&¬%$·!º|@ª\""
        self.nombre = nombre
        self.email = email
        self.password=""

    def cambiar_password(self,password):
        if len(password) >= 8 and len(password) <= 16:
            i = 0
            while i < len(password):
                if password[i] in self.letrasmin:
                    i = 0
                    while i < len (password):
                        if password[i] in self.numeros:
                            i=0
                            while i < len(password):
                                if password[i] in self.letrasmay or password[i] in self.caract:
                                    self.password = password
                                    return True
                                i += 1
                        i += 1
                i += 1
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
           