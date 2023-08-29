class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:
          numeros = ["0","1","2","3","4","5","6","7","8","9"]
          letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          caracteres_especiales = ["#","-","_","%"]
          cantidad_numeros=0
          cantidad_letras=0
          cantidad_caracteres_o_mayus=0
          for elemento in password:
            if elemento in numeros:
              cantidad_numeros +=1
            elif elemento in letras.lower():
              cantidad_letras +=1
            elif elemento in letras or elemento in caracteres_especiales:
              cantidad_caracteres_o_mayus += 1
              
          if cantidad_numeros >=1 and cantidad_letras >=1 and cantidad_caracteres_o_mayus >= 1:
            return True
          else:
            return False
        else:
           return False

    def login(self,password):
        if password == self.password:
          return True
        else:
          return False


           