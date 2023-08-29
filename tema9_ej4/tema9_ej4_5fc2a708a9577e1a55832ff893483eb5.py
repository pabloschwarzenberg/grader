def Numero(n):
    if n in "0123456789":
        return True
    else:
        return False
def letra_minuscula(n):
        if n in "abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            return False
def letra_mayuscula(n):
    if n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False
def Caracter(n):
    if n in "123456789":
        return False
    if n in "abcdefghijklmnopqrstuvwxyz":
        return False
    if n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    else:
        return True
    
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password = str(password)
        numero = 0
        letra = 0
        LETRA = 0
        caracter = 0
        if len(password)<8 or len(password)>16:
            return False
        else:
            for i in password:
                if Numero(i):
                    numero +=1
                if letra_minuscula(i):
                    letra +=1
                if letra_mayuscula(i):
                    LETRA +=1
                if Caracter(i):
                    caracter +=1
            if numero > 0 and letra > 0 and LETRA > 0:
                self.password = password
                return True
            if numero > 0 and letra > 0 and caracter > 0:
                self.password = password
                return True
            if numero > 0 and LETRA > 0:
                self.password = password
                return True
            else:
              return False
    def login(self,password):
        if password == self.password:
            return True
        else:
            return False