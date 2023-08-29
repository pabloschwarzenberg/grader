class Usuario:
    def _init_(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.letras=[ ]
        if 8<=len(password)<=16:
            for i in password:
                if i=="D" or i=="_":
                    self.letras.append(i)
            if len(self.letras)>=1:
                self.password=password
                return True
            else:
               return False
        else:
          return False

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False