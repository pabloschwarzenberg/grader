class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        simbolo = ["_","!","#","$","%"]
        tiene_simbolo = False
        tiene_numero = False
        tiene_mayuscula = False
        tiene_letras = False
        
        if len(password) >= 8 and len(password) <= 16:
            a = list(password)
            for letra in a:
                if letra in simbolo:
                    tiene_simbolo = True
                if letra.isdigit():
                    tiene_numero = True
                if letra.isalpha():
                    tiene_letras = True
                if letra.isupper():
                    tiene_mayuscula = True
            if tiene_numero and tiene_letras and(tiene_mayuscula or tiene_simbolo):
                self.password = password
                return True
        return False

       
    def login(self,password):
      if password == self.password:
        return True
      else:
        return False
