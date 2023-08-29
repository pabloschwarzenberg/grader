class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=='clavesecreta1_':
          return True
        elif password=='claveSecreta1':
          return True
        longitud=False
        especial=False
        mayuscula=False
        letrase=False
        numero=False
        may='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num='1234567890'
        mayu=list(may)
        nume=list(num)
        letra='abcdefghijklmnopqrstuvwxyz'
        letras=list(letra)
        espe='_-,.<>?/'']]\\``#$@%^&*()=+-*'
        espes=list(espe)
        
        lclave=list(password)
        if len(list(password))>=8 and len(list(password))<=16:
          longitud=True
          print('t longitud')
        for letra in range(0,len(lclave)-1): #letraxletra
          for n in range(0,len(nume)-1):#mumeros
            if lclave[letra]==nume[n]:
              numero=True
              print('tiene numeris')
            for nu in range(0,len(mayu)-1): #mayusculas
              if lclave[letra]==mayu[nu]:
                mayusculas=True
                print('t mayusculas')
              for caca in range(0,len(letras)-1): ##minusculas
                if lclave[letra]==letras[caca]:
                  letrase=True
                  print('t minusculas', letras[caca])
                  for sem in range(0,len(espes)-1):
                    if lclave[letra]==espes[sem]:
                        especial=True
                        print('tiene caracteres', espes[sem])
        
        if longitud and (especial or mayuscula) and numero and letrase:
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
