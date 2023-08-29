class Fraccion:
    def __init__(self, num, den):
        self.num=num
        self.den=den

    def __add__(self,f):
        if isinstance(f, Fraccion):
            n=(self.num*f.den+self.den*f.num)
            d=(self.den*f.den)
        elif isinstance(f, int)or isinstance(f, float):
            f=Fraccion(f,1)
            n=(self.num*f.den+self.den*f.num)
            d=(self.den*f.den)
        resultado=Fraccion(n,d)
        return(resultado)                    
    def __mul__(self,valor):
        if isinstance(valor,Fraccion):
          n=self.num*valor.num
          d=self.den*valor.den
        elif isinstance(valor,int) or isinstance(valor,float):
          n=self.num*valor
          d=self.den
        resultado=Fraccion(n,d)
        return resultado

    def __repr__(self):
        n=self.num//self.den
        if n>0:
          r=self.num%self.den
          if r!=0:
            return str(n)+" "+str(r)+"/"+str(self.den)
          else:
            return str(n)
        return str(self.num)+"/"+str(self.den)
        
        