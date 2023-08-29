class Vector:
    def init(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        v1 = self.x + self.y + self.z 

    def norma(v1):
        norma = v1**(1/2)
        return norma

    def  add(self,other):
        return(self.x + other.x, self.y + other.y, self.z + other.z)
class Fraccion:
    def init(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def mul(self,other):
        r=Fraccion(0,0)
        r.num=self.numother.num
        r.den=self.denother.den
        return r

    def repr(self):
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

    def add(self,otro):
      x=self.numotro.den
      c=self.denotro.num
      return Fraccion(x+c,self.denotro.den)

    def sub(self,otro):
      x=self.numotro.den
      c=self.denotro.num
      return Fraccion(x-c,self.denotro.den)

    def truediv(self, otro): 
      return Fraccion(self.numotro.den, self.denotro.num)

if name == "main":
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
    