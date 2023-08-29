class Usuario: 

    def __init__(self,nombre,email): 

        self.nombre=nombre 

        self.email=email 

        self.password="" 

 

    def cambiar_password(self,password): 

        #print(type(password)) 

        #print("cambiar_password") 

        #print("password: ",password) 

        numero_caracteres_especiales_o_mayuscula=0 

        numero_letras=0 

        numero_numeros=0 

        for i in str(password): 

            if i == i.upper(): 

                numero_caracteres_especiales_o_mayuscula+=1 

                #print("Mayuscula: ",i) 

            for m in """:'";[]-_=+~!@#$%^&*()<,>./?""".split(): 

                if i == m: 

                    numero_caracteres_especiales_o_mayuscula+=1 

                    #print("Caracter especial: ",m) 

        for j in password: 

            if type(j)== str: 

                numero_letras+=1 

        for h in password: 

            for k in "0123456789": 

                if h == k: 

                    numero_numeros+=1 

                    numero_caracteres_especiales_o_mayuscula-=1 

        #print("numero_caracteres_especiales_o_mayuscula: ",numero_caracteres_especiales_o_mayuscula) 

        #print("numero_letras: ",numero_letras) 

        #print("numero_numeros: ",numero_numeros) 

        if len(password) >= 8 and len(password) <=16: 

            if numero_letras >= 1 and numero_numeros >= 1 and numero_caracteres_especiales_o_mayuscula >=1 and numero_numeros>=1: 

                self.password=password 

                return True 

            else: 

                return False 

        else: 

            return False 

 

    def login(self,password): 

        #print("login") 

        #print("password: ",password) 

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
           