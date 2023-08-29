class Auto:
    def __init__(self,es,ren):
        self.kilometraje=0
        self.cuenta_k=0
        self.capa_est=es
        self.nivel_estanque=0
        self.ren=ren
    def reiniciar_cuentakilometros(self):
        self.cuenta_k=0
    def andar(self,v,t):
        reco=t*v
        self.cuenta_k+=reco
        self.kilometraje+=reco
        gas=reco/self.ren
        if gas>self.nivel_estanque:
            re=reco-(gas*self.ren)
            return re
        else:
            self.nivel_estanque-=gas
            return 0
    def autonomia(self):
        r=self.ren*self.nivel_estanque
        return r
    def llenar_estanque(self,l):
        if self.capa_est-self.nivel_estanque < l:
            a=self.capa_est-self.nivel_estanque
            return a,False
        else:
            self.nivel_estanque+=l
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12) 