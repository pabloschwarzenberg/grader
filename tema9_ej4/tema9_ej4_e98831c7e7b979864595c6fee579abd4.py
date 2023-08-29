class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        numeros = ["0","1","2","3","4","5","6","7","8","9"]
        caracteres=["!","#","$","&","/","_","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        if 8 <= len(password) <= 16:
            for i in numeros:
                if password.find(i)!=-1:
                    for i in caracteres:
                        if password.find(i)!=-1:
                            self.password=password
                            return True
            else:
                return False
        else:
            return False


    def login(self, password):
        if self.password==password:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
