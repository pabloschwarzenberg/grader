# USUARIO DE TWITTER
def esint(txt):
    try:
        int(txt)
        return True
    except ValueError:
        return False

class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:
            letrasmi = [] # Letras minusculas
            letrasma = [] # Letras mayusculas
            signos = []
            for i in password:
                if not(esint(i)): # tiene al menos una letra o signo
                    if 65 <= ord(i) <= 90 :
                        letrasma.append(i)
                    if 97 <= ord(i) <= 122:
                        letrasmi.append(i)
                    else:
                        signos.append(i)
            numeros = []
            for e in password:
                if esint(e): # tiene al menos un numero
                    numeros.append(e)
            if numeros != [] and letrasmi != [] and (letrasma != [] or signos != []):
                self.password = password
                return True
            else:
                return False
        else:
            return False

    def login(self,password):
        if password == self.password:
            return True
        elif password != self.password:
            return False

    def __repr__(self):
        s = " Usuario: {0} \n Email: {1}".format(self.nombre,self.email)
        return s