class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if  8 <= len(password) <= 16:
            for n in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]:
                if (n in password) == True:
                    for m in ["1","2","3","4","5","6","7","8","9"]:
                        if (m in password) == True:
                            if password.lower() != password:
                                self.password = password
                                return True


                            else:
                                for l in range(0,len(password)):
                                    if (password[l] in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]) == False:
                                        if (password[l] in ["1","2","3","4","5","6","7","8","9"]) == False:
                                            self.password = password
                                            return True

                                        else:
                                            continue

                                    else:
                                        continue
                                            
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
           