class Usuario:
  def __init__(self,nombre,email):
    self.nombre=nombre
    self.email=email
    self.password=""
  def cambiar_password(self,password):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    numeros="0123456789"
    if 7<len(password)<17:
      ns=0
      ls=0
      distintos=0
      for a in password:
        if alfabeto.find(a)!=-1:
          ls+=1
        if numeros.find(a)!=-1:
          ns+=1
        distintos=len(password)-ls-ns
      if ls!=0 and ns!=0 and distintos!=0:
        self.password+=password
        return True
      else:
        return False
    else:
      return False
        
  def login(self,password):
    if password==self.password:
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
               