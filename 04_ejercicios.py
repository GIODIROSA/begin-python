# 1. Cálculo del área de un rectángulo solicitando los datos al usuario.

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area= base * altura
print("El área del rectangulo es ", area)

# 2. Conversor de monedas (Dólar a CLP) solicitando el valor actual del dólar y la cantidad de dolares al usuario.

cantidad_dolares = float(input("Ingrese la cantidad de dolares: "))
valor_actual_dolar = float(input("Ingrese el valor actual del dolar: "))
cantidad_pesos_clp= round(cantidad_dolares * valor_actual_dolar)
# print("Su cambio de dolar a pesos CLP es: $", cantidad_pesos_clp, "CLP")

resultado_casa_cambio= """
El cambio obtenido por los valores ingresados en dolares y el valor del dolar actual es: $
"""
print(resultado_casa_cambio, cantidad_pesos_clp, "CLP")

# 3. Generador de correo electrónico con formato nombre.apellido@correo.cl, solicitando los datos al usuario.

nombre_usuario= input("Ingrese el nombre: ")
apellido_usuario= input("Ingrese el apellido: ")
formato_nombre= nombre_usuario + "." + apellido_usuario
# print("=>", formato_nombre)
generador_correo= formato_nombre + "@inacap.cl"
print("Su nuevo correo es: ", generador_correo)

# 4. Conversor de longitud (Pies a Metros) solicitando los datos al usuario.

cantidad_pies= float(input("Ingrese la cantidad de longitud en pies: "))
conversor_a_metros= round(cantidad_pies // 3,281)
print("La longitud en metros son: ", conversor_a_metros)

# 5. Solicitar al usuario un número y un porcentaje, para mostrar por pantalla el número correspondiente al porcentaje del número ingresado.

valor_numero = float(input("Ingrese el valor: "))
valor_porcentaje = int(input("Ingrese el porcentaje aplicar: "))
reset_porcentaje = valor_porcentaje / 100
resultado_porcentaje = round(valor_numero * reset_porcentaje)
print("El", valor_porcentaje, "% de", valor_numero, "es ",  resultado_porcentaje)


# 6. Solicitar al usuario el precio de un producto y el porcentaje de descuento, para mostrar por pantalla el precio a pagar después de aplicar el descuento

precio_producto = float(input("Ingrese el precio del producto: "))
valor_descuento = float(input("Ingrese el descuento aplicar: "))
resultado_descuento_aplicado= round(precio_producto * (valor_descuento / 100))
resultado_final= precio_producto - resultado_descuento_aplicado
print("El valor del producto con porcentaje aplicado es: ", resultado_final)