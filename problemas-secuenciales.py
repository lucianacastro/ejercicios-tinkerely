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

#Punto 2.3.
def get_calificacion_final():
	nota_parcial_1 = float(raw_input("Ingresa la calificacion del primer parcial: "))
	nota_parcial_2 = float(raw_input("Ingresa la calificacion del segundo parcial: "))
	nota_parcial_3 = float(raw_input("Ingresa la calificacion del tercer parcial: "))
	examen_final = float(raw_input("Ingresa la calificacion del examen final: "))
	trabajo_final = float(raw_input("Ingresa la calificacion del trabajo final: "))
	promedio_parciales = (nota_parcial_1 + nota_parcial_2 + nota_parcial_3) / 3.0
	cincuenta_y_cinco =promedio_parciales * 0.55
	treinta = examen_final * 0.3
	quince = trabajo_final * 0.15
	nota_final = cincuenta_y_cinco + treinta + quince
	return "la nota final del alumno es: " + str(nota_final)

print get_calificacion_final()
