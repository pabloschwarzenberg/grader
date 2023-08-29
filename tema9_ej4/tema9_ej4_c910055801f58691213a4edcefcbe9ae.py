class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password) in range(8, 17):
            flag1, flag2, flag3 = False, False, False
            for char in password:
                if char.isdigit():
                    flag1 = True
                if char.isalpha():
                    flag2 = True
                if not (char.isalpha() or char.isdigit()) or not password.islower():
                    flag3 = True
            if flag1 and flag2 and flag3:
                self.password=password
                return True
        return False

    def login(self,password):
        if self.password==password:
            return True
        return False
           