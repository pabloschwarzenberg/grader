class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "1234567890"
        a = 0
        A = 0
        n = 0
        o = 0
        if len(password) >= 8 and len(password) <= 16 :
            for i in range(len(password)):
                u = password[i] in alfabeto
                g = password[i] in ALFABETO
                m = password[i] in numeros
                if u == True:
                    a += 1
                elif g == True:
                    A += 1
                elif m == True:
                    n += 1
                elif u == False and g == False and m == False:
                    o += 1
        if a > 0 and n > 0:
            if A > 0 or o > 0 :
                self.password = str(password)
                return True
            else:
                return False
        else:
            return False
    def login(self,password):
        if str(password) == self.password:
            return True
        else:
            return False