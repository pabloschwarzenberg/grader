class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        n=self.num*other.num
        d=self.den*other.den
        r=Fraccion(n,m)
        return r


    def __add__(self,otro):
        n1=self.num
        n2=otro.num
        d1=self.den
        d2=otro.den
        if d1==d2:
            df=d1
            nf=n1+n2
            ff=Fraccion(nf,df)
            return ff
        else:
            n11=self.num*otro.den
            n22=otro.num*self.den
            dff=self.den*otro.den
            nff=n11+n22
            rr=Fraccion(nff,dff)
            return rr
    def __div__(self,other):
        n=self.num*other.den
        d=self.den*other.num
        r=Fraccion(n,m)
        return r
        
            
            

    def a_numero(self):
        return self.num/self.den


   