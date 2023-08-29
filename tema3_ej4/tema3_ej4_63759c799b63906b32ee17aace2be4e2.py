class Fraccion:
    def __init__(self,numerador,denominador):
        self.n = numerador
        self.d=denominador
    def __add__(self, other):
        r = Fraccion(0,0)
        r.d=self.d*other.d
        r.n=self.d*other.n+self.n*other.d
        return r
    def __sub__(self, other):
        r = Fraccion(0,0)
        r.d = self.d*other.d
        r.n=self.n*other.d-self.d*other.n
        return r
    def __mul__(self, other):
        r = Fraccion(0,0)
        r.n = self.n*other.n
        r.d = self.d*other.d
        return r
    def __truediv__(self, other):
        r = Fraccion(0,8)
        r.n = self.n * other.d
        r.d = self.d * other.n
        return r
    def __repr__(self):
        entero = self.n // self.d
        if 0 < entero:
            resto = self.n%self.d
            return resto
        if 0 > entero:
            resto = self.d%self.n