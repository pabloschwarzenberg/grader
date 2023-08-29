class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
       contador1=0
       contador2=0
       contador3=0
       if 8<=len(password)<=16:
           for letra in password:
               if letra.isalpha()==True:
                   contador1+=1
           for letra in password:
               if letra.isdigit()==True:
                   contador2+=1
           for letra in password:
               if letra.isupper()==True or (not letra.isdigit() and not letra.isalpha()):
                   contador3+=1
       if contador1>=1 and contador2>=1 and contador3>=1:
           self.password==password
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