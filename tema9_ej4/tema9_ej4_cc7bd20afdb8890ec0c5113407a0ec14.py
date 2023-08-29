class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:

            abecedario = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
            c_especial = "!#$%&/()=[]{}-_/*+."

            for i in password:

                for j in range(len(password)):
                    if i == abecedario[j]:
                        self.password = password
                        return True

                for j in range(len(c_especial)):
                    if i == c_especial[j]:
                        self.password = password
                        return True
            return False


        else:
            return False

    def login(self,password):
        if password == self.password:
            return True
        else:
            return False
