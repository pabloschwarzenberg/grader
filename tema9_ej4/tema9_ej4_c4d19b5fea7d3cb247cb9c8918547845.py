class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        strin = []
        strinup = []
        num = []
        chara = []

        if len(password)>= 8 and len(password)<= 16:

            for x in range(len(password)):

                if password[x].isalpha() == True:

                    if password[x].upper() == password[x]:

                        strinup.append(password[x])

                    strin.append(password[x])

                elif password[x].isdigit() == True:

                    num.append(password[x])

                elif password[x].isalnum() == False:

                    chara.append(password[x])


            if len(strin)>=1 and len(num)>=1:

                if len(chara)>=1 or len(strinup)>=1:

                    self.password = password
                    return True

                else:
                    
                    return False

            else:
                
                return False

        else:
            
            return False

    def login(self,password):
        
        if password == self.password:
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
           