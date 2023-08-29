class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:
            list1 = list("1234567890")
            list2 = list("abcdefghijklmnopqrstuvwxyz")
            list3 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            y = list(password)
            count1 = 0
            for i in range(0, len(list1)):
                if password.find(list1[i]) != -1:
                    y.remove(list1[i])
                    count1 = count1 + 1
            if count1 != 0:
                count2 = 0
                for j in range(0, len(list2)):
                    while str(y).find(list2[j]) != -1:
                        x = int(len(y))
                        y.remove(list2[j])
                        count2 = count2 + 1
                if count2 != 0:
                    if len(y) != 0:
                        return True

            return False

        else:
            return False

        pass

    def login(self, password):
        if password== self.password:
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
           