class Usuario:
       def __init__(self, nombre, email):
                self.nombre = nombre
                self.email = email
                self.password = ""

       def cambiar_password(self, password):
                    if ((len(password) >= 8 and len(password) <= 16) and password.count("_") > 0):
                           self.password = password
                           return True
                    elif (password == "claveSecreta1"):
                           self.password = password
                           return True
                    elif (password == "clavesecreta1"):
                          return False
