#Punto 2.1.
def get_interes():
	capital = float(raw_input("Ingrese el capital: "))
	tasa = 0.05
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

#Punto 2.4.
def get_porcentaje_hombres_mujeres():
	total_mujeres = float(raw_input("Ingresa el total de alumnas mujeres: "))
	total_hombres = float(raw_input("Ingresa el total de alumnos hombres: "))
	total_alumnos = total_mujeres + total_hombres
	porcentaje_mujeres = total_mujeres / total_alumnos * 100
	porcentaje_hombres = total_hombres / total_alumnos * 100
	print "En el curso hay un %f por ciento de mujeres" %(porcentaje_mujeres), 
	print "y un %f por ciento de hombres" %(porcentaje_hombres)
get_porcentaje_hombres_mujeres()

#Punto 2.5.
def get_pulsaciones():
	edad = float(raw_input("Ingresa su edad: "))
	pulsaciones = (220 - edad)/10
	print "usted deberia tener %f pulsaciones por cada diez segundos" %pulsaciones 
get_pulsaciones()

#Punto 2.6.
def get_participacion_societaria():
	inversion_socio_1 = float(raw_input("Ingresa la participacion del socio 1: "))
	inversion_socio_2 = float(raw_input("Ingresa la participacion del socio 1: "))
	inversion_total = inversion_socio_1 + inversion_socio_2
	participacion_socio_1 = inversion_socio_1 / inversion_total * 100
	participacion_socio_2 = inversion_socio_2 / inversion_total * 100
	print "El socio uno tiene una participacion del %f por ciento" %(participacion_socio_1) 
	print "y el socio 2 el %f por ciento" %(participacion_socio_2)
get_participacion_societaria()




