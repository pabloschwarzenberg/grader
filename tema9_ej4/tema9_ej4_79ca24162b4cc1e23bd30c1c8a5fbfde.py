class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        self.password=password
        if 8<=len(self.password)<=16:
            palabra=self.password
            palabra2=palabra.lower()
            palabra3=[]
            for i in range(0,len(palabra)):    
                palabra3.append(palabra2[i])
            palabra3.sort()
            for i in range(0,len(palabra)):
                b1=palabra3[i]
                b2=palabra3[i+1]
                if b1 in ("1234567890"):
                    if palabra != palabra2 or (b2 not in ("abcdefghijklmnopqrstuvwxyz")):
                        return True
                        self.password=password
                    else:
                        return False
                else:
                    return False
                break
        else:
            return False
            self.password=None
            
    def login(self,password):
        if password==self.password:
            return True
        else:
            return False