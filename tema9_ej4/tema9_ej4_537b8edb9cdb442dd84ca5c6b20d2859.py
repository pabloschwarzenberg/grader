class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        signos="!@#$%&/()=?¿¡'_-><,.:{}][*+"
        nm=0
        ns=0
        for i in range(0,len(mayusculas)):
            f=password.count(mayusculas[i])
            nm=nm+f

        for j in range(0,len(signos)):
            g=password.count(signos[j])
            ns=ns+g

        nt=ns+nm
                      
        if len(password)<8 or len(password)>16:
            return False
        if nt==0:
            return False
        if nt>0 and len(password)<16 and len(password)>8:
            self.password=password
            return True
        

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False