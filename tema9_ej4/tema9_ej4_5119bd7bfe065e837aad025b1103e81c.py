class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        cambiar=True
        contador_letras=0
        contador_numeros=0
        contador_simbolosmayuscula=0
        minusculas="abcdefghijklmnopqrstuvwxyz"
        if len(password)>=8 and len(password)<=16:
            i=0
            while i<len(password):
                if password[i].isalpha()==True:
                    if password[i] in minusculas:
                        contador_letras+=1
                    else:
                        contador_simbolosmayuscula+=1
                else:
                    if password[i]=="0" or password[i]=="1" or password[i]=="2" or password[i]=="3" or password[i]=="4" or password[i]=="5" or password[i]=="6" or password[i]=="7" or password[i]=="8" or password[i]=="9":
                        contador_numeros+=1
                    else:
                        contador_simbolosmayuscula+=1
                i+=1
        if contador_letras!=0 and contador_numeros!=0 and contador_simbolosmayuscula!=0:
            self.password=password
        else:
            cambiar=False
            
        return cambiar
            
 
    def login(self,password):
        if self.password==password:
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