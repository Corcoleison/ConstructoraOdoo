#!/usr/bin/python 
# coding: utf-8 
#
import xmlrpclib

# Datos de conexión (adaptar a cada caso)
#
server = "localhost"
port = 8069
dbname = "admin"
user_name = "admin"
user_passwd= "admin"

# Conectamos con el servicio 'common' de Odoo
conn = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'common'))
# Obtenemos identificador (uid) del usuario
uid = conn.authenticate(dbname, user_name, user_passwd, {})
# Conectamos con el servicio 'object' de Odoo
object = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/2/%s' % (server, port, 'object'))   


salir = False
opcion = 0
 
while not salir:
 
    print "1. Listar Albañiles"
    print "2. Listar Trabajos"
    print "3. Listar Materiales"
    print "4. Crear Albañil"
    print "5. Salir"
     
    print "Elige una opcion (Numero Entero)"
 
    opcion =raw_input()
 
    if opcion == "1":
        print "Listamos los albañiles en el sistema"
	# Buscamos los albañiles:
	customer_ids = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search', [[['albanil', '=' ,True]]])

	# Leemos sus nombres:
	customers = object.execute_kw(dbname, uid, user_passwd,'res.partner', 'read', [customer_ids], {'fields':['name']})

	# Y los mostramos:
	print "-- Albañiles --"
	for customer in customers:
    	 print customer['name']
	print " "

    elif opcion == "2":
        print "Listamos los trabajos en el sistema"
	# Buscamos los trabajos:
	trabajos_ids = object.execute_kw(dbname, uid, user_passwd, 'constructora.trabajo', 'search',[[['activo', '=' ,True]]])

	# Leemos los nombres y otros datos:
	trabajos = object.execute_kw(dbname, uid, user_passwd,'constructora.trabajo', 'read', [trabajos_ids], {'fields':['name', 'descripcion', 'fecha', 'lugar']})

	# Y los mostramos:
	print "-- Trabajos Activos --"
	for trabajo in trabajos:
		print trabajo['name'], trabajo['descripcion'], trabajo['fecha'], trabajo['lugar']
	print " "

    elif opcion == "3":
        print "Listamos los materiales en el sistema"
	# Buscamos los materiales:
	materiales_ids = object.execute_kw(dbname, uid, user_passwd, 'constructora.material', 'search',[[]])

	# Leemos los nombres y demas campos:
	materiales = object.execute_kw(dbname, uid, user_passwd,'constructora.material', 'read', [materiales_ids], {'fields':['name', 'cantidad', 'precio', 'preciomaterial']})

	# Y los mostramos:
	print "-- Materiales --"
	for material in materiales:
		print "\n"
		line_title = '{:>12}{:>15}{:>30}{:>20}'.format('Nombre', 'Cantidad', 'Precio por Unidad', 'Precio Total')
		print line_title
		#	print "Codigo \t Nombre \t Precio de Venta \t StockActual"
		line_new = '{:>12}{:>25}{:>20}{:>20}'.format(material['name'], material['cantidad'], material['precio'], material['preciomaterial'])
		print line_new
		print "\n"
		print " "

    elif opcion == "4":
	#print "Dame un nombre para el nuevo albañil"
	nombre = raw_input("Dame un nombre para el nuevo albañil: ")
	id_persona = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'create', [{
	'name': nombre,
	'albanil': True,
	}])
	
	print "Volvemos a listar los albañiles"
	# Buscamos los albañiles:
	customer_ids = object.execute_kw(dbname, uid, user_passwd, 'res.partner', 'search', [[['albanil', '=' ,True]]])

	# Leemos los nombres:
	customers = object.execute_kw(dbname, uid, user_passwd,'res.partner', 'read', [customer_ids], {'fields':['name']})

	# Y los mostramos:
	print "-- Albañiles --"
	for customer in customers:
    	 print customer['name']
	print " "


    elif opcion == "5":
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print "Fin"




