class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        self.password=password
        lista1=['0','1','2','3','4','5','6','7','8','9']
        lista2=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
        lista3=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ñ','Z','X','C','V''B','N','M','º','ª',"|","!","@",'"','#','·','~','$','%','€','¬','&','/','(',')','=','?',"'",'¿','¡','^','[','`',']','+','*','{','´','¨','}','Ç','ç',',',';',':','.','_','-','<','>']
        lista4=[]
        if (16>=len(password)>=8):
            for elemento in lista1:
              for e in lista2:
               for i in lista3:
                 if elemento in list(password)and e in list(password) and i in list(password):
                    lista4.append('o')
                 else:
                     lista4.append('x')

                      
        else:
          lista4.append('x')

        if lista4.count('o')>=1:
            return True
        else:
            return False
      



    def login(self,password):
        if password!=self.password:
            return False
        else:
            return True

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    #print(usuario.login("clavesecreta1_"))
    #print(usuario.login("claveSecreta1"))
           