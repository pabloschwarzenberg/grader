class Fraccion:
  def _truediv_(self,other):
    r=Fraccion(0,0)
    r.num=self.num/(1/other.den)
    r.den=self.den/(1/other.num)
    return r
    def _add_(self, other):
      m=Fraccion(0,0)
      m.num_(self.num*other.den)+(self.den*other.num)
      m.den=self.den*other.den
      return m 
    def _sub_(self,other):
      m=Fraccion(0,0)
      m.num=(self.num*other.den)-(self.den*other.num)
      m.den=self.den*other.den
      return m 
      if _name_ == "_main_":
        f=input("Ingresa la primera fraccion [a/b]: ")
        f=f.split("/")
        f1=Fraccion(int(f[0]),int(f[1]))
        f=input("Ingresa la segunda fraccion [c/d]: ")
        f=f.split("/")
        f2=Fraccion(int(f[0]),int(f[1]))
        print("La suma es ",f1+f2)
        print("La resta es ",f1-f2)
        print("La multiplicación es ",f1*f2)
        print("La división es ",f1/f2)