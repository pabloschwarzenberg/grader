class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.clave=""

    def cambiar_password(self,password):
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        simbolo="_!#$%&/@()=?¡¿°¨*+~}{[]^-"
        numeros="0123456789"
            
        a=0
        b=0
        c=0
        d=0
        e=0
        for i in password:
            
            if i in numeros:
                a=1
            
            if i in mayusculas:
                c=1
            if i in minusculas:
                d=1
            if i in simbolo:
                e=1
        if a==1 and d==1 and(c==1 or e==1) and len(password)>=8 and len(password)<=16:
            self.clave=password
            return True
        else:
           return False
            
        

    def login(self,password):
        if password==self.clave:
            return True
        else:
            return False

           