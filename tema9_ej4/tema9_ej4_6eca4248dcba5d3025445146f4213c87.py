class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if  8<=len(password)<=16:
            esta_el_numero=0
            #for i in password:
            numeros=["0","1","2","3","4","5","6","7","8","9"]
            for j in numeros:
                if j in password:
                    esta_el_numero=1
                #print("esta_el_numero:"+str(esta_el_numero))

            mayuscula=0
            for i in password:
                if (i == i.upper() and i.isalpha()) or (not i.isalnum()):
                    mayuscula=1
                #print("mayuscula:"+str(mayuscula))

         

            letra=0
            for h in password:
                if h.isalpha:
                    letra=1
                #print("letra:"+str(letra)) 


            if esta_el_numero==1 and mayuscula==1 and letra==1:
                return True


        return False


    def login(self,password):
        if password==self.password:
            return True
        
        return False 

usuario=Usuario("pablo","phschwarzenberg@uc.cl")
print(usuario.cambiar_password("clave"))
print(usuario.cambiar_password("clavesecreta1_"))
print(usuario.cambiar_password("clavesecreta"))
print(usuario.cambiar_password("clasesecreta1"))
print(usuario.cambiar_password("claveSecreta1"))
print(usuario.login("clavesecreta1_"))
print(usuario.login("claveSecreta1"))



