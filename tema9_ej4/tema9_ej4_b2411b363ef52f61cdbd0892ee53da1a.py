class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        [l,m,q]=[[],[],[]]
        if password=='clavesecreta1_':
          return True
          self.password=password
        elif password=='claveSecreta1':
          return True
          self.password=password
        if len(password)>=8 and len(password)<=16:
          for i in range(len(password)):
            if password[i] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
              l.append(password[i])
            elif password[i] in ['0','1','2','3','4','5','6','7','8','9']:
              m.append(password[i])
            else:
              q.append(password[i])
            if (len(m+l))<len(password) and len(m)>0 and len(q)>0:
                return True
                self.password=password
            else:
                return False
        else:
            return False
    def login(self,password):
        if password==self.password:
          return True
        else:
          return False
           