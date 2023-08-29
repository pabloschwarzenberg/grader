class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(str(password))>=8 and len(str(password))<=16:
            if ("1" in str(password) or "2" in str(password) or "3" in str(password) or "4" in str(password) or "5" in str(password) or "6" in str(password) or "7" in str(password) or "8" in str(password) or "9" in str(password) or "0" in str(password)):
                lista=list(str(password))
                lista_nueva=[]
                for i in lista:
                    if i == "!" or i=="@" or i=="#" or i=="$" or i=="%" or i== "^" or i=="&" or i=="*" or i=="(" or i==")" or i=="_" or i=="-" or i=="+" or i=="=" or i=="[" or i=="]" or i=="{" or i=="}" or i==":" or i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="Ñ" or i=="O" or i=="P" or i=="Q" or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="W" or i=="X" or i=="Y" or i=="Z" :
                        lista_nueva.append(i) 
                if len(lista_nueva)>=1:
                    self.password=password
                    return True
                else:
                    return False

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


           
