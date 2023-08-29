class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if 8<= len(password) <= 16:
            n_num = 0
            n_min = 0
            n_car = 0
            for i in range(len(password)):

                # letras
                if 97 <= ord(password[i]) <= 122:
                    n_min += 1

                # numeros
                elif 48 <= ord(password[i]) <= 57:
                    n_num += 1

                # caracteres especiales
                elif 33 <= ord(password[i]) <= 47 or 58 <= ord(password[i]) <= 96 or 123 <= ord(password[i]) <= 126:
                    n_car += 1
            if n_min > 0 and n_car > 0 and n_num > 0:
                self.password = password
                return True
            else:
                return False
        else:
            return False

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False           