class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letras_minusculas=list("abcdefghijklmnñopqrstuvwxyz123456789")
        lista=list(password)
        simbolos=[]
        for i in lista:
          if i not in letras_minusculas:
            simbolos.append(i)
        if len(simbolos)>0:
          self.password=password
          return True
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
           