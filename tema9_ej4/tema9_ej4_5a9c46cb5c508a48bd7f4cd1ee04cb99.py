class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password = str(password)
        largoPass = len(password)
        listaPass = list(password)
        lower = []
        num = []
        upperSpec = []
        for i in password:
          if i.islower() == True:
            lower.append(i)
          elif i.isdigit() == True:
            num.append(i)
          elif i == '_' or i == '-' or i.isupper() == True or i.isalnum == False and i.isspace == False:
            upperSpec.append(i)
        if len(lower) > 0 and len(num) > 0 and len(upperSpec) > 0 and 8 <= len(password) <= 16:
          self.password = password
          cambio = True
        else:
          cambio = False
        return cambio

    def login(self,password):
        if password == self.password:
          login = True
        else:
          login = False
        return login

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           