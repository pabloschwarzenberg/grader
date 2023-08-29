# Crear un objeto FechaHora
fecha_hora = FechaHora()

# Establecer la fecha
fecha_hora.fijarFecha('08/06/2023')

# Establecer la hora
fecha_hora.fijarHora('12:30:45')

# Mostrar la fecha y hora actual
print(fecha_hora)  # Salida: 2023/06/08 12:30:45

# Cambiar el día a 10
fecha_hora.cambiar('dd=10')

# Cambiar la hora a 15
fecha_hora.cambiar('hh=15')

# Mostrar la fecha y hora actual después de los cambios
print(fecha_hora)  # Salida: 2023/06/10 15:30:45
