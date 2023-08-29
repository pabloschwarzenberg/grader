'''class Usuario:
    def __init__(self,nombre,email):
        self.password=''
        self.nombre=nombre
        self.email=email
    def cambiar_password(self,password):
        clave=list(password)
        if (len(clave)>=8 and len(clave)<16):
            letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            numero=['0','1','2','3','4','5','6','7','8','9']
            signos=['#','/','_']
            mayusc=list(map(lambda x:x.upper(),letras))
            for i in range(len(clave)):
                if (clave[i] in letras) or (clave[i] in mayusc):
                    continue
                else:
                    print('no se puede')
                    return False
                    break
                
                    if clave[i] in numero:
                        continue
                    else:
                        print('no se puede')
                        return False
                        break
                        if (clave[i] in signos) or (clave[i] in mayusc):
                            print('se puede cambiar')
                            self.password=password
                            return True
                        else:
                            print(' no se puede ')
                            return False
                            break
                        
            

        else:
            return False
        
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
    print(usuario.login("claveSecreta1"))'''
    
class Usuario:
    def __init__(self,nombre,email):
        self.password=''
        self.nombre=nombre
        self.email=email
    def cambiar_password(self,password):
        clave=list(password)
        if (len(clave)>=8 and len(clave)<16):
            letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            numero=['0','1','2','3','4','5','6','7','8','9']
            signos=['#','/','_']
            mayusc=list(map(lambda x:x.upper(),letras))
            l=0
            n=0
            s=0
            m=0
            for i in range(len(clave)):
                if (clave[i] in letras):
                    l+=1
                if (clave[i] in mayusc):
                    m+=1
                if clave[i] in numero:
                     n+=1
                     continue
                
                if (clave[i] in signos):
                      s+=1
            if n>=1 and (m>=1 or s>=1):
                self.password=password
                return True
            else:
                return False
        else:
            return False
        
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
