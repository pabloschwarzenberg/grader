class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letras = list("abcdefghijklmnopqrstuvwxyz")
        letras_mayusc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        numeros = list("1234567890")
        if len(password) >= 8  and len(password) <= 16: 
          contador_num = 0
          contador_letras = 0
          contador_M = 0
          for i in password :
            if i in numeros :
              contador_num += 1
            elif i in letras :
              contador_letras += 1
            elif i in letras_mayusc :
              contador_M += 1
            else :
              contador_M += 1
          if contador_num >= 1 and contador_letras >= 1 and contador_M >= 1 :
            self.password = password
            return True
          else :
            return False
        else :
          return False

    def login(self,password):
      if self.password == password :
        return True
      else :
        return False
    


           