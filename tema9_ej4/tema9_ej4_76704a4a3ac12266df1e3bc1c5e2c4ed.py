def verdadero(clave):
            abc="abcdefghijklmnñopqrstuvwxyz"
            for i in clave.lower():
              for n in abc:
                if i != n:

                    return True
            
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,clave):
        #clave= input()
        if 8<= len(clave) <=16:
          abc="abcdefghijklmnñopqrstuvwxyz"
          ABC= abc.upper()                   
          for letra in abc:
            if clave.count(letra)>0:
              for letra2 in ABC:
                if clave.count(letra2)>0 or verdadero(clave)==True:
                  self.password=clave
          return True 
        else:
            return False
    
    def login(self,password):
        if self.password== clave:
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
           
