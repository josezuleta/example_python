""""
accion_uno = "Ya estoy en la entrada"
accion_dos = "Me estoy registrando"
"""

#Estructura de control (Condicional o sentencia if o si)
#Permite continuar flujo (realizar algo) si se cumple una condicion 
# y en caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa)
#esta sentencia (condicional if) va acompañado 
 
"""""
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos 
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno != estructura_datos_dos

"""
# Hay varias maneras de utilizar la sentencia if 
# if simple, if compuesto if anidado    

#if simple
#dato_comparacion = 18
#edad = 19
""""
if edad >= dato_comparacion: 
    print("Ingresar, disfrutar del evento")
"""
#if compuesto
""""
if edad > dato_comparacion:
    print("ingresar, disfrutar el evento")
else:
    print("No ingresar")
"""

#Ejercicio Boleta
"""
boleta = True   
fecha_evento = "28/02/2023"
fecha_comparacion = "28/02/2023"
#if inidado
if edad > dato_comparacion and boleta and fecha_evento == fecha_comparacion:
    print("Ingresar, disfrute del evento")
else:
    print("No ingresar")    


Boleta_localidad= 5

if Boleta_localidad == 1:
	print('Compro boleta Vip por un valor de $500')
elif Boleta_localidad == 2:
	print('Compro boleta Preferencial con un valor de $400')
elif Boleta_localidad == 3:
	print('Compro boleta General con un valor de $200')
elif Boleta_localidad == 4:
	print('Compro boleta Baja con un valor de $100')
else:
	print('No eligio una de nuestras opciones, por tanto no tiene boleta.')
"""
#Ejercicio documento.
"""""
tipo_A= 20000
tipo_B= 10000
tipo_diff= 5000
horas_laborales = 8

sueldo_mensualA= tipo_A * horas_laborales * 30
sueldo_mensualB = tipo_B * horas_laborales * 30
sueldo_mensualdiff= tipo_diff * horas_laborales * 30
horas_extras = (tipo_diff*6/100+tipo_diff)*3
nuevo_sueldo = sueldo_mensualdiff + horas_extras

tipo_proyecto = 1
if tipo_proyecto == 1:
   print('Tipo de proyecto es A, por tanto el valor de la hora es 20000$')
   print ('Su salario mensual da un total de' , sueldo_mensualA)
   print('Salario mensual es mayor al tope maximo')
elif tipo_proyecto ==2:
    print('Tipo de proyecto B, por tanto el valor de la hora es 10000$')
    print('Su salario mensual da un total de', sueldo_mensualB)
    print ('Salario mensual es mayor al tope maximo')
else:
    print('Tipo de proyecto diferente A/B, por tanto el valor de la hora es 5000')
    print('su sueldo mensual es un total de' , sueldo_mensualdiff)
    print('Salario mensual es menor al tope, valor horas extras a pagar' , horas_extras)
    print('Nuevo sueldo mensual = ' , nuevo_sueldo)
"""
#Actividad diagramas
print('Ingrese el producto que desea publicitar')
producto = ('')
producto = input ()
print ('Has elegido publicitar' , producto , 'buena eleccion')

print ('ingrese el medio por el cual quiere publicitar el producto')
redes = ('')
redes = input()
print('Has elegido publicitar tu', producto, 'en', redes)
print ("confirme con si y no para repetir el procedimiento")
confirmacion=("")
Confirmacion=input("")
if confirmacion == "si":
    print("su producto ha sido publicitado con exito ")
else:
    print("repita el procedimiento")

    #:)
