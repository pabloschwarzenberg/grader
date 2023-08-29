class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ''

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            checks = []
            x = 0
            letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
            num = ['1','2','3','4','5','6','7','8', '9', '0']
            spec = ['!','#','$','%','&','(',')','*','+','-','_','¿','.','{']
            mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for elem in password:
                for let in letra:
                    if let == elem:
                        x = 1
            checks.append(x)
            x = 0
            for elem in password:
                for n in num:
                    if n == elem:
                        x = 1
            checks.append(x)
            x = 0
            for elem in password:
                for s in spec:
                    if s == elem:
                        x = 1
            checks.append(x)
            x = 0
            for elem in password:
                for u in mayus:
                    if u == elem:
                        x = 1
            checks.append(x)

            if checks[0] == 1 and checks[1] == 1 and (checks[2] == 1 or checks[3] == 1):
                self.password =password
                return True
        return False

    def login(self, password):
        if password == self.password:
            return True
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
           