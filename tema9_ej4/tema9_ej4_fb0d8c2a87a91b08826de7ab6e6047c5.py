class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        g=0
        contadordecaracter=0
        contadordenumero=0
        largo=len(password)
        clave=password.lower()
        while g<largo:
            if password[g]=="#" or password[g]=="_" or password[g]==".":
                contadordecaracter +=1
                g +=1
            elif password[g]=="1" or password[g]=="2" or password[g]=="3" or password[g]=="4":
                contadordenumero +=1
                g +=1
            elif password[g]=="5" or password[g]=="6" or password[g]=="7" or password[g]=="8" or password[g]=="9":
                contadordenumero +=1
                g +=1
            else:
                g+=1
        if contadordecaracter!=0 and 8<=largo<=16 and contadordenumero!=0 and clave==password:
            return True
        elif 8<=largo<=16 and contadordenumero!=0 and contadordecaracter==0 and clave!=password:
            return True
        elif contadordecaracter!=0 and  8<=largo<=16 and contadordenumero!=0 and clave!=password:
            return True
        else:
            return False

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False


