class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      lena=len(password)
      especiales=["_","#","$","%"]
      numeros=["1","2","3","4","5","6","7","8","9","0"]
      sumnum=0
      suma=0
      if 8<=lena<=16:
        b=password.islower()
        for i in password:
          if i in especiales:
            suma+=1
        for i in password:
          if i in numeros:
            sumnum+=1
        if suma!=0 and sumnum!=0:
          self.password=password
          return True
        elif sumnum!=0 and b==False:
          self.password=password
          return True
        elif sumnum!=0 and b==False and suma!=0:
          self.password=password
          return True
        else:
          return False
      else:
        return False
        

    def login(self,password):
      if self.password==password:
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
           