class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password=list(password)
        simbolos=["!","#","$","%","/","&","(",")","=","´","*","~","@",'"',"_"]
        if 8<=len(password)<=16:
            contador_abecenum=0
            contador_abecemayusimb=0
            for i in password:
                if i.isalnum():
                    contador_abecenum+=1
                if i.isupper() or i in simbolos:
                    contador_abecemayusimb+=1
            if contador_abecenum>=1 and contador_abecemayusimb>=1:
                self.password=password
                return True
                
            else:
                return False

        else:
            return False

        pass
    
    def login(self,password):
        if password==self.password:
            return True
        else:
            return False
        pass
     