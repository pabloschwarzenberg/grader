class Usuario:
          def __init__(self,nombre,email):
                    self.nombre=nombre
                    self.email=email
                    self.password=""

          def cambiar_password(self,password):
                    #print(len(password))
                    #print(password.count("_"))
                    if ((len(password)>=8 and len(password)<=16) and password.count("_")>0) or ((len(password)>=8 and len(password)<=16) and password.count("#")>0) or ((len(password)>=8 and len(password)<=16) and password.count("1")>0 and password.count("_")>0):
                              self.password=password
                              return True
                    else:
                              return False
def login(self,password):
                    #print(password)
                    #print(self.cambiar_password(password))
                    if self.password==password:
                              return True
                    else:
                              return False

          def __str__(self):
                    return str(self.nombre)+str(self.email)+str(self.password)