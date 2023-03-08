#EJERCICIO 1 

#MONEDAS 
monedas = ('EURO' 'DOLAR' 'CHILENO' 'ESTERLINA' 'SOL')

#VALORES
Euro_valor= 5000
dolar_valor= 4700
chileno_valor= 4600
esterlina_Valor= 5700
sol_valor= 1200

#VARIABLES
moneda_cambio = ("COP")
nombre = ("")
nombre = input("Ingrese su nombre completo: ")
documento = ("")
documento = input("Ingrese su número de documento de identidad: ")
moneda_origen = ("")
moneda_origen = input("Ingrese la moneda origen (EURO, DOLAR, CHILENO, ESTERLINA o SOL): ")
moneda_destino = ("")
moneda_destino = input("Ingrese la moneda destino (COP)" ":")
cantidad =("")
cantidad = float (input("Ingrese la cantidad de dinero a cambiar: "))

#PROCESO
if moneda_origen not in monedas: 
    print ("Lo siento, la moneda origen", moneda_origen , "no esta disponible")
elif moneda_destino not in moneda_cambio :
    print ("Lo siento, la moneda destino", moneda_destino, "no esta disponible")
elif moneda_origen == "EURO" :
    intermediacion = Euro_valor *0.1* cantidad
    conversion = Euro_valor *cantidad
    print(nombre,"con documento de identidad", documento, "con moneda de origen", moneda_origen,"a moneda destino" , moneda_destino,"con la cantidad en euros de :", cantidad,)
    print ("La conversion a pesos COP es :")
    print(conversion)
    print("El valor intermediacion es :")
    print(intermediacion)
    print(f"Atención: el porcentaje de intermediación al cambiar a '{moneda_destino}' es del {intermediacion}%, lo cual supera el límite del 10%.")
    respuesta = input("¿Desea continuar con la operación? (si/no): ")
    if respuesta == "no":
            print("Operación cancelada.")
            quit()
    if respuesta == "si" :
         print ("Ha confirmado, cambio de moneda finalizado")
elif moneda_origen == "DOLAR" :
    intermediacion = dolar_valor *0.06 * cantidad
    conversion = dolar_valor *cantidad
    print(nombre,"con documento de identidad", documento, "con moneda de origen", moneda_origen,"a moneda destino" , moneda_destino,"con la cantidad en dolares de :", cantidad,)
    print ("La conversion a pesos COP es :")
    print(conversion)
    print("El valor intermediacion es :")
    print(intermediacion)

elif moneda_origen == "CHILENO" :
    intermediacion = chileno_valor *0.5 * cantidad
    conversion = chileno_valor *cantidad
    print(nombre,"con documento de identidad", documento, "con moneda de origen", moneda_origen,"a moneda destino" , moneda_destino,"con la cantidad en pesos chilenos de :", cantidad,)
    print ("La conversion a pesos COP es :")
    print(conversion)
    print("El valor intermediacion es :")
    print(intermediacion) 

elif moneda_origen == "ESTERLINA" :
    intermediacion = esterlina_Valor *0.1 * cantidad
    conversion = esterlina_Valor *cantidad
    print(nombre,"con documento de identidad", documento, "con moneda de origen", moneda_origen,"a moneda destino" , moneda_destino,"con la cantidad en libras esterlinas de :", cantidad,)
    print ("La conversion a pesos COP es :")
    print(conversion)
    print("El valor intermediacion es :")
    print(intermediacion) 
    print(f"Atención: el porcentaje de intermediación al cambiar a '{moneda_destino}' es del {intermediacion}, lo cual supera el límite del 10%.")
    respuesta = input("¿Desea continuar con la operación? (si/no): ")
    if respuesta == "no":
            print("Operación cancelada.")
            quit()
    if respuesta == "si" :
         print ("Ha confirmado, cambio de moneda finalizado")
                 
elif moneda_origen == "SOL" :
    intermediacion = sol_valor *0.02 * cantidad
    conversion = sol_valor *cantidad
    print(nombre,"con documento de identidad", documento, "con moneda de origen", moneda_origen,"a moneda destino" , moneda_destino,"con la cantidad en sol de :", cantidad,)
    print ("La conversion a pesos COP es :")
    print(conversion)
    print("El valor intermediacion es :")
    print(intermediacion)



#EJERCICIO 2

#TARIFAS
tarifas = ("Individual" "Doble" "Familiar")

#PRECIOS
precio_individual = 2500
precio_doble = 4600
precio_familiar = 5200

#VARIABLES
nombre_huesped = input ("Ingrese por favor su nombre completo : ")
documento = ("")
documento = input ("ingrese su numero de documento : ")
total_dias = int (input ("Ingrese la cantidad de dias que se va quedar : "))
print(nombre_huesped , "TENGA presente la cantidad de personas que se van a hospedar, +3 personas tarifa ¡FAMILIAR! POR FAVOR.")
tipo_habitacion = input ("Ingrese por favor que tipo de tarifa desea comprar : (INDIVIDUAL : 2500$) (DOBLE : 4600$) (FAMILIAR : 5200$) : ")

#PROCESO

if tipo_habitacion == "INDIVIDUAL" :
   precio_total = precio_individual * total_dias
   iva = precio_total * 0.16
   precio_iva = precio_total + iva
   descuento = iva * 0.5
   total_descuento = precio_iva - descuento
   print ("El huesped", nombre_huesped, "con numero de documento", documento, "desea alquilar la habitacion INDIVIDUAL por", total_dias , "dias")
   print ("Con un precio sin IVA segun los dias de :",precio_total)
   print ("Con un precio con IVA del :",precio_iva)
   print ("Y un precio total con descuento :",total_descuento )
   respuesta = input("¿Desea confirmar la compra? : Si/No : ")
   if respuesta == "Si" :
      print (nombre_huesped , "La compra fue realizada correctamente")
   if respuesta == "No" :
      print (nombre_huesped,"La compra fue cancelada verifique y realice de nuevo el procedimiento")

elif tipo_habitacion == "DOBLE":
   precio_total = precio_doble * total_dias
   iva = precio_total * 0.16
   precio_iva = precio_total + iva
   descuento = iva * 0.9
   total_descuento = precio_iva - descuento
   print ("El huesped", nombre_huesped, "con numero de documento", documento, "desea alquilar la habitacion DOBLE por", total_dias , "dias")
   print ("Con un precio sin IVA segun los dias de :",precio_total)
   print ("Con un precio con IVA del :",precio_iva)
   print ("Y un precio total con descuento :",total_descuento )
   respuesta = input("¿Desea confirmar la compra? : Si/No : ")
   if respuesta == "Si" :
      print (nombre_huesped , "La compra fue realizada correctamente")
   if respuesta == "No" :
      print (nombre_huesped,"La compra fue cancelada verifique y realice de nuevo el procedimiento")

elif tipo_habitacion == "FAMILIAR":
   precio_total = precio_familiar * total_dias
   iva = precio_total * 0.16
   precio_iva = precio_total + iva
   descuento = iva * 0.15
   total_descuento = precio_iva - descuento
   print ("El huesped", nombre_huesped, "con numero de documento", documento, "desea alquilar la habitacion FAMILIAR por", total_dias , "dias")
   print ("Con un precio sin IVA segun los dias de :",precio_total)
   print ("Con un precio con IVA del :",precio_iva)
   print ("Y un precio total con descuento :",total_descuento )
   respuesta = input("¿Desea confirmar la compra? : Si/No : ")
   if respuesta == "Si" :
      print (nombre_huesped , "La compra fue realizada correctamente")
   if respuesta == "No" :
      print (nombre_huesped,"La compra fue cancelada verifique y realice de nuevo el procedimiento")
      
elif tipo_habitacion not in tarifas :
   print ('Tipo de habitacion no reconocida , realizar nuevamente el proceso :(')
