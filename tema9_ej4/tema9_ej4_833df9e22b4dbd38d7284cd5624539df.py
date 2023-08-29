class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.clave=""

    def cambiar_password(self,password):
        a=list(password)
        letras=[]
        numeros=[]
        caracter=[]
        for elemento in a:
            if elemento.isalpha():
                letras.append(elemento)
            elif elemento.isdigit():
                numeros.append(elemento)
            else:
                caracter.append(elemento)

        
    

        mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        existe=[]
        for elemento in letras:
            if elemento in mayusculas:
                existe.append(elemento)

        if len(a)>=8 and len(a)<=16:
            if len(letras)>0 and (len(existe)>0 or len(caracter)>0) and len(numeros)>0 :
                self.clave=password
                return(True)
            else:
                return(False)
        else:
            return(False)

    def login(self,password):
        if password==self.clave:
            return(True)
        else:
            return(False)

 