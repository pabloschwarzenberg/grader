class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        l_password = list(password)
        if 7 < len(l_password) < 17:
            list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            list2 = "@ ! # $ % & ? ¿ + * - _ ; :"
            list2 = list2.split()
            for p in l_password:
                for d in range(0, 10):
                    d = str(d)
                    if d == p:
                        for p in l_password:
                            for i in list1:
                                for s in list2:
                                    if i == p:
                                        self.password = password
                                        return True
                                    if s == p:
                                        self.password = password
                                        return True
                                    else:
                                        continue
        self.password=""
        return False

    def login(self, password):
        if password==self.password:
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
           