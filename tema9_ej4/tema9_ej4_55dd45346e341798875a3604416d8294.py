class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if len(password) >= 8 and len(password) <= 16:
        for c in password:
          if c.isupper() or c.isalnum() == False:
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

           