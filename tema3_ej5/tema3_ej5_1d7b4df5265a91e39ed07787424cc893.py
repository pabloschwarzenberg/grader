def __truediv__(self,other):
        r=Fraccion(0,0)
        r.num=self.num/(1/other.den)
        r.den=self.den/(1/other.num)
        return r
        
    def __add__(self,other):
        m=Fraccion(0,0)
        m.num=(self.num*other.den)+(self.den*other.num)
        m.den=self.den*other.den
        return m      

    def __sub__(self,other):
        m=Fraccion(0,0)
        m.num=(self.num*other.den)-(self.den*other.num)
        m.den=self.den*other.den
        return m
