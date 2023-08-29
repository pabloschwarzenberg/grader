def mcd(m,n):
    while m%n != 0:
        mViejo = m
        nViejo = n

        m = nViejo
        n = mViejo%nViejo
    return n

class Fraccion:
     def __init__(self,arriba,abajo):
         self.num = arriba
         self.den = abajo

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otraFraccion):
         nuevoNum = self.num*otraFraccion.den + \
                      self.den*otraFraccion.num
         nuevoDen = self.den * otraFraccion.den
         comun = mcd(nuevoNum,nuevoDen)
         return Fraccion(nuevoNum//comun,nuevoDen//comun)

     def __eq__(self, otro):
         primerNum = self.num * otro.den
         segundoNum = otro.num * self.den

         return primerNum == segundoNum

x = Fraccion(1,2)
y = Fraccion(2,3)
print(x+y)
print(x == y)