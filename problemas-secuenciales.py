#Punto 2.1.
def get_interes():
	capital = float(raw_input("Ingrese el capital: "))
	tasa = 0.5
	interes = capital * tasa
	return interes

print get_interes()

#Punto 2.2
def get_comision():
	sueldo_basico = float(raw_input("Ingrese el sueldo basico: "))
	venta_1 = float(raw_input("Ingrese el monto de la primer venta: "))
	venta_2 = float(raw_input("Ingrese el monto de la segunda venta: "))
	venta_3 = float(raw_input("Ingrese el monto de la tercer venta: "))
	comision = (venta_1 + venta_2 + venta_3) * 0.1
	sueldo_total = sueldo_basico + comision
	print "comision: ", comision
	print "sueldo total: ", sueldo_total

get_comision()

