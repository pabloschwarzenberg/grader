class Usuario:
  def __init__(self,nombre,email):
      self.nombre=nombre
      self.email=email
      self.password=""
  def cambiar_password(self,password):
      if 8<=len(password)<=16:
         a=0
      for i in password:
          if i.isupper()==True:
             a+=1
          if i.isalnum()==False and i.isalpha()==False and i.isspace()==False:
                a+=1
                if a!=0:
                    Usuario.password=password
                    return True
                else:
                    return False
  def login(self,password):
      if password==Usuario.password:
         return True
      else:
         return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           