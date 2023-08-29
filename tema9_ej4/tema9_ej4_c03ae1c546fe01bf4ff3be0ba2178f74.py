class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      alfabeto="qwertyuiopasdfghjklñzxcvbnm"
      numeros="1234567890"
      otros="ABCDEFGHIJKLMNOPQRSTUVWXYZ_!#$%&/()=?¡"
      contadorl=0
      contadorn=0
      contadorc=0
      for caracter in password:
        for numero in numeros:
          if caracter == numero:
            contadorn+=1
            break
        for letra in alfabeto:
          if caracter == letra:
            contadorl+=1
            break
        for otro in otros:
          if caracter == otro:
            contadorc+=1
            break
      if 7<len(list(password))<17 and contadorl>0 and contadorn>0 and contadorc>0:
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
           