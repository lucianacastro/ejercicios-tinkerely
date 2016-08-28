#Punto 1.1.
def ask_precio_neto():
	precio_neto = float(raw_input("Ingrese precio: "))
	return precio_neto

def get_precio_final(precio_neto):
	precio_final = precio_neto * 1.21
	return precio_final

print get_precio_final(ask_precio_neto())

#Punto1.2.
def ask_numeros():
	lista_numeros = []
	lista_numeros += [float(raw_input ("Ingrese el primer numero: "))]
	lista_numeros += [float(raw_input ("Ingrese el segundo numero: "))]
	lista_numeros += [float(raw_input ("Ingrese el tercer numero: "))]
	return lista_numeros

def get_promedio(lista_numeros):
	promedio = sum(lista_numeros) / len(lista_numeros)
	return promedio

print get_promedio(ask_numeros())

#Punto 1.3.
def get_numero_mayor():
	numero_uno = float(raw_input("Ingrese el primer numero: "))
	numero_dos = float(raw_input("Ingrese el segundo numero: "))
	if numero_uno > numero_dos:
		return numero_uno
	else:
		return numero_dos

print get_numero_mayor()

#Punto 1.4.
def say_numero_par_impar():
	numero = float(raw_input("Ingrese cualquier numero: "))
	if numero % 2 == 0:
		print "es par"
	else:
		print "es impar"
say_numero_par_impar()	

#Punto 1.5.
def get_num_negativo():
	numero = 0
 	while numero >= 0:
 		numero = float(raw_input("Ingrese cualquier numero: "))
get_num_negativo()


 


