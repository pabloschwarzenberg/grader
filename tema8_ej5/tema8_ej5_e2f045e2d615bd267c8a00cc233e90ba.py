class FechaHora:
	
	def __init__(self):
		
		self.dia=0
		self.mes=0
		self.anio=0
		self.hora=0
		self.minuto=0
		self.segundo=0

	def __str__(self):
		
		fecha="{:02d}/{:02d}/{:02d}".format(self.anio, self.mes, self.dia)
		hora="{:02d}:{:02d}:{:02d}".format(self.hora, self.minuto, self.segundo)
		return fecha+" "+hora

	def fijarFecha(self, fecha):
		
		partes=fecha.split("-")
		self.dia=int(partes[0])
		self.mes=int(partes[1])
		self.anio=int(partes[2])

	def fijarHora(self, hora):
		
		partes=hora.split(":")
		self.hora=int(partes[0])
		self.minuto=int(partes[1])
		self.segundo=int(partes[2])

	def fijarFechaHora(self, fechahora):
		
		partes=fechahora.split(" ")
		self.fijarFecha(partes[0])
		self.fijarHora(partes[1])

	def cambiar(self, parte):
		
		partes=parte.split("=")
		tipo=partes[0].strip()
		valor=int(partes[1].strip())

		if tipo=="dd":
			
			if valor>=1 and valor<=31:
				
				self.dia=valor
				
			else:
				
				print("Dia invalido.")
				
		elif tipo=="mm":
			
			if valor>=1 and valor<=12:
				
				self.mes=valor
				
			else:
				
				print("Mes invalido.")
				
		elif tipo=="aaaa":
			
			self.anio=valor
			
		elif tipo=="HH":
			
			if valor>=0 and valor<=23:
				
				self.hora=valor
				
			else:
				
				print("Hora invalida.")
				
		elif tipo=="MM":
			
			if valor>=0 and valor<=59:
				
				self.minuto=valor
				
			else:
				
				print("Minuto invalido.")
				
		elif tipo=="SS":
			
			if valor>=0 and valor<=59:
				
				self.segundo=valor
				
			else:
				
				print("Segundo invalido.")
				
		else:
			
			print("Error")


if __name__=='__main__':
	
	fh=FechaHora()
	fh.fijarFechaHora("30-09-2015 17:45:00")
	print(fh)

	fh.cambiar("mm=10")
	print(fh)

	fh.fijarHora("18:00:00")
	fh.cambiar("aaaa=2016")
	print(fh)