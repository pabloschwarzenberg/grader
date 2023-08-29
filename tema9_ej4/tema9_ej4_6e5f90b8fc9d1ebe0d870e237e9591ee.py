class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=password
        if len(a)>7 and len(a)<17:
            if a.isdigit()==True or a.isalpha()==True:
                return False
            if a.isalnum()== True:
               M=0
               C=0
               N=0
               while C!= len(a):
                   if a[C].isalpha()==True:
                                    if a[C].upper()==a[C]:
                                        M+=1
                                        C+=1
                                    else:
                                        C+=1
                   if a[C].isdigit()==True:
                       N+=1
                       C+=1
               if N!=0 and M!=0:
                   return True
                   self.password=password 
               else:
                   return False
            if a.isalnum() == False:
                L=0
                n=0
                c=0
                
                while c != len(a):
                    if a[c].isalpha() == True:
                            L += 1
                            c+= 1
                        
                         
                    if a[c].isdigit() == True:
                        n += 1
                        c += 1
                    else:
                        c+=1 
               
               
                if n!= 0 and L!= 0:
                    return True
                    self.password = password
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
           