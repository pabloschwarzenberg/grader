class Vector:    
    def truediv(self,other):
        r=Fraccion(0,0)
        r.num=self.num/(1/other.den)
        r.den=self.den/(1/other.num)
        return r

    def add(self,other):
        m=Fraccion(0,0)
        m.num=(self.numother.den)+(self.denother.num)
        m.den=self.denother.den
        return m

    def sub(self,other):
        m=Fraccion(0,0)
        m.num=(self.numother.den)-(self.denother.num)
        m.den=self.denother.den
        return m