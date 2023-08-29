class Fraccion:
    def _init_(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def _mul_(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def _repr_(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)

    def a_numero(self):
        return self.num/self.den

    def _add_(self,otro):
      x=self.num*otro.den
      c=self.den*otro.num
      return Fraccion(x+c,self.den*otro.den)

    def _sub_(self,otro):
      x=self.num*otro.den
      c=self.den*otro.num
      return Fraccion(x-c,self.den*otro.den)

    def _truediv_(self, otro): 
      return Fraccion(self.num*otro.den, self.den*otro.num)