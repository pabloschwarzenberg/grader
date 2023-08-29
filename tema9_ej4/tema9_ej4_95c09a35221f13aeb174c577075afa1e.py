class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      clave=[]
      password= str(password)
      for letra in password:
        clave.append(letra)
      if 8<= len(clave) <= 16: 
        self.password = password
      else:
        False

    def login(self,password):
        pass
           