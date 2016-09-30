class Ruta:
	def __init__(self, kilometros_ok, kilometros_mal, desde, hasta):
		self.kilometros_ok = kilometros_ok
		self.kilometros_mal = kilometros_mal
		self.desde = desde
		self.hasta = hasta

	def obtener_total_kilometros(self):
		return self.kilometros_ok + self.kilometros_mal

class Vehiculo:
	carga_maxima = -1
	viajes = []

	def __init__(self, combustible):
		self.combustible = combustible

	def calcular_tiempo_viaje(self, ruta, carga):
		return -1	

	def calcular_consumo_combustible(self, ruta, carga):
		return -1

	def puede_hacer_viaje(self, viaje):
		if self.calcular_tiempo_viaje(viaje.ruta, viaje.carga) <= viaje.tiempo:
			if self.calcular_consumo_combustible(viaje.ruta, viaje.carga) <= self.carga_maxima:
				return True
		return False

	def asignar_viaje(self, viaje):
		self.viajes.append(viaje)  

	def calcular_consumo_total_viajes_asignados(self):
		consumo_total = 0
		for viaje in self.viajes:
			consumo_total +=  self.calcular_consumo_combustible(viaje.ruta, viaje.carga)
		return consumo_total

class Camioneta(Vehiculo):
	carga_maxima = 1200
	
	def calcular_tiempo_viaje(self, ruta, carga):
		return ruta.kilometros_ok * 120.00 + ruta.kilometros_mal * 100.00

	def calcular_consumo_combustible(self, ruta, carga):
		combustible_por_km = 0.1	
		return combustible_por_km
	
class Combi(Vehiculo):
	carga_maxima = 2500

	def calcular_tiempo_viaje(self, ruta, carga):
		if self.carga <= 1800:
			return ruta.obtener_total_kilometros() / 100.00
		else:
			return ruta.obtener_total_kilometros() / 90.00

	def calcular_consumo_combustible(self, ruta, carga):
		if carga <= 1500:	
			return ruta.obtener_total_kilometros() * 0.15
		else:
			return ruta.obtener_total_kilometros() * 0.20

class Camioncito(Vehiculo):
	carga_maxima = 6000

	def calcular_tiempo_viaje(self, ruta, carga):
		tiempo_viaje = 0.25

		tiempo_viaje += ruta.kilometros_ok / 100.00
		if carga <= 3000:
			tiempo_viaje += ruta.kilometros_mal / 75.00
		elif carga <= 5000:
			tiempo_viaje += ruta.kilometros_mal / 70.00
		else:
			tiempo_viaje += ruta.kilometros_mal / 60.00

		return tiempo_viaje

	def calcular_consumo_combustible(self, ruta, carga):
		return ruta.kilometros_ok * (carga/1500.00)
			+ 1.5 * ruta.kilometros_mal * (carga/1500.00)

class Camionazos(Vehiculo):
	cerga_maxima = 20000

	def calcular_tiempo_viaje(self, ruta, carga):
		tiempo_viaje = 1.00
		tiempo_viaje += (ruta.kilometros_ok / 90.00)
		tiempo_viaje += (ruta.kilometros_mal / 70.00)
		if carga > 1000:
 			tiempo_viaje *= 1.30
		return tiempo_viaje

	def calcular_consumo_combustible(self, ruta, carga):
		return ruta.obtener_total_kilometros() * (carga/1000.00 + 0.3)

class Viaje:
	def __init__(self, carga, tiempo, ruta):
		self.carga = carga
		self.tiempo = tiempo
		self.ruta = ruta


class Flota:
	vehiculos = []
	def __init__(self, vehiculos):
		self.vehiculos += vehiculos

	def obtener_vehiculos_capaces(self, viaje):
		vehiculos_capaces = []
		for vehiculo in self.vehiculos:
			if vehiculo.puede_hacer_viaje(viaje):
				vehiculos_capaces.append(vehiculo)
		return vehiculos_capaces






		
