class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      password=list(password)
      numeros=["0","1","2","3","4","5","6","7","8","9"]
      letras="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      letras1=letras.lower()
      letras=list(letras)
      letras1=list(letras1)
      caracteres=["!","#","$","%","&","/","(",")","=","-","_","+","*"]
      if 8<=len(password)<=16:
        for i in range(0,len(numeros)):
          if numeros[i] in password:
            for j in range(0,len(letras1)):
              if letras1[j] in password:
                for k in range(0,len(letras)):
                  if letras[k] in password:
                      password="".join(password)
                      self.password=password
                      return True
                for l in range(0,len(caracteres)):
                  if caracteres[l] in password:
                      password="".join(password)
                      self.password=password
                      return True
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
           