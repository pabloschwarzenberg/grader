class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        abecedario = 'abcdefghijklmnopqrstuvwxyz'
        abecedario_alternativo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digitos = '123456789'
        caracteres_especiales = "!@_-^%$*"
        if len(password) < 16 and len(password) > 8:
            w = 0
            x = 0
            y = 0
            z = 0
            solutions = 0
            while x < len(password):
                a = abecedario.find(password[x])
                if a != -1:
                    solutions = solutions + 1
                    x = len(password)
                x = x+1
            while y < len(password):
                b = abecedario_alternativo.find(password[y])
                if b != -1:
                    solutions = solutions +1
                    y = len(password)
                y = y+1
            while z < len(password):
                c = caracteres_especiales.find(password[z])
                if c != -1:
                    solutions = solutions + 1
                    z = len(password)
                z = z+1
            while w<len(password):
                d = digitos.find(password[w])
                if d != -1:
                    solutions = solutions + 1
                    w = len(password)
                w = w+1
        elif len(password) > 16 or len(password) < 8:
            return False
        
        if solutions >= 3:
            usuario.password = password
            return True
        else:
            return False
    def login(self,password):
        if self.password == password:
            return True
        else:
            return False
usuario=Usuario("pablo","phschwarzenberg@uc.cl")