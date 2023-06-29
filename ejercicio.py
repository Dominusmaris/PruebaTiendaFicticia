import datetime

# Lista de vehículos
lista_vehiculos = [
    "Toyota;GT86;2016;RDU243;Rojo",
    "Toyota;4Runner;1990;VQR314;Rojo",
    "Toyota;4Runner;2011;ASC378;Azul",
    "Toyota;Yaris;2014;UHN783;Verde",
    "Toyota;GT86;2013;PXR919;Burdeo",
    "Toyota;4Runner;1984;RSB197;Verde",
    "Toyota;Corolla;2018;NQE146;Morado",
    "Toyota;Yaris;2020;ZAV269;Burdeo",
    "Toyota;Supra;2021;UCE557;Verde",
    "Toyota;4Runner;2017;CIF927;Blanco",
    "Toyota;Supra;2023;DVT712;Amarillo",
    "Honda;Quint;1985;HMH396;Blanco",
    "Honda;Fit;2020;JAE691;Amarillo",
    "Honda;Logo;1998;CSX826;Morado",
    "Honda;Quint;1985;HMH396;Blanco",
    "Honda;Accord;1988;EHP775;Burdeo",
    "Honda;Civic Type-R;2005;QNE248;Rojo",
    "Mitsubishi;Lancer;1996;RNA741;Rojo",
    "Ferrari;California;2014;FWM618;Rojo",
    "Ferrari;575M Maranello;2004;HIR719;Azul",
    "Ferrari;F430;2006;TTH289;Rojo"
]

# Función para imprimir la lista de vehículos
def mostrar_lista(lista_vehiculos):
    print("\n----- LISTA DE VEHÍCULOS -----")
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        marca = datos[0]
        modelo = datos[1]
        año = datos[2]
        patente = datos[3]
        color = datos[4]
        print(f"Marca: {marca}")
        print(f"Modelo: {modelo}")
        print(f"Año: {año}")
        print(f"Patente: {patente}")
        print(f"Color: {color}")
        print("-------------------------------")

# Función para buscar un auto por modelo o marca
def buscar_auto(lista_vehiculos):
    modelo = input("Ingrese el modelo o marca del auto a buscar: ")
    encontrados = []
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        if modelo.lower() in datos[1].lower() or modelo.lower() in datos[0].lower():
            encontrados.append(vehiculo)
    
    if encontrados:
        print("Se encontraron los siguientes autos:")
        for auto in encontrados:
            print(auto)
    else:
        print("No se encontraron autos con el modelo o marca especificados.")

# Función para imprimir un certificado de un automóvil
def imprimir_certificado(lista_vehiculos, nombre_usuario, fecha_actual):
    patente = input("Ingrese la patente del automóvil: ")
    encontrado = False
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        if patente.lower() == datos[3].lower():
            encontrado = True
            marca = datos[0]
            modelo = datos[1]
            color = datos[4]
            print(f"{nombre_usuario} emite certificado que:")
            print(f"El vehículo {marca} {modelo} con patente {patente}")
            print(f"De color {color}")
            print(f"Queda registrado oficialmente a la fecha de {fecha_actual}")
            break
    
    if not encontrado:
        print("No se encontró un automóvil con la patente especificada.")

# Función para buscar automóviles por patente
def buscar_por_patente(lista_vehiculos):
    patente = input("Ingrese la patente a buscar: ")
    encontrados = []
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        if patente.lower() == datos[3].lower():
            encontrados.append(vehiculo)
    
    if encontrados:
        print("Se encontraron los siguientes autos:")
        for auto in encontrados:
            print(auto)
    else:
        print("No se encontraron autos con la patente especificada.")

# Función para buscar automóviles por rango de año
def buscar_por_rango_de_año(lista_vehiculos):
    min_año = int(input("Ingrese el año mínimo del rango: "))
    max_año = int(input("Ingrese el año máximo del rango: "))
    encontrados = []
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        año = int(datos[2])
        if min_año <= año <= max_año:
            encontrados.append(vehiculo)
    
    if encontrados:
        print("Se encontraron los siguientes autos:")
        for auto in encontrados:
            print(auto)
    else:
        print("No se encontraron autos dentro del rango de años especificado.")

# Función para agregar información del dueño a un automóvil
def agregar_info_dueño(lista_vehiculos):
    patente = input("Ingrese la patente del automóvil: ")
    encontrado = False
    for i in range(len(lista_vehiculos)):
        vehiculo = lista_vehiculos[i]
        datos = vehiculo.split(";")
        if patente.lower() == datos[3].lower():
            encontrado = True
            nombre_propietario = input("Ingrese el nombre del propietario: ")
            datos.append(nombre_propietario)
            lista_vehiculos[i] = ";".join(datos)
            print("Información del dueño agregada correctamente.")
            break
    
    if not encontrado:
        print("No se encontró un automóvil con la patente especificada.")

# Función para mostrar todos los automóviles del color favorito del usuario
def mostrar_por_color_favorito(lista_vehiculos, color_favorito):
    encontrados = []
    for vehiculo in lista_vehiculos:
        datos = vehiculo.split(";")
        if color_favorito.lower() == datos[4].lower():
            encontrados.append(vehiculo)
    
    if encontrados:
        print("Se encontraron los siguientes autos:")
        print("+------------------------------------------------------------------------+")
        print("| {:^15} | {:^15} | {:^15} | {:^15} |".format("Marca", "Modelo", "Año", "Patente"))
        print("+------------------------------------------------------------------------+")
        for auto in encontrados:
            datos = auto.split(";")
            marca = datos[0]
            modelo = datos[1]
            año = datos[2]
            patente = datos[3]
            print("| {:^15} | {:^15} | {:^15} | {:^15} |".format(marca, modelo, año, patente))
        print("+------------------------------------------------------------------------+")
    else:
        print("No se encontraron autos del color favorito especificado.")

# Función principal del programa
def main(lista_vehiculos):
    nombre_usuario = input("Ingrese su nombre: ")
    fecha_actual = datetime.datetime.now()
    color_favorito = input("Ingrese su color favorito: ")

    print("\nFecha actual:", fecha_actual.strftime("%d/%m/%Y"))

    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1 - Buscar 1 auto por Modelo / Marca")
        print("2 - Imprimir la lista")
        print("3 - Imprimir Certificado")
        print("4 - Buscar por patente")
        print("5 - Buscar por rango de año")
        print("6 - Agregar información de Dueño al automóvil")
        print("7 - Mostrar todos los automóviles del color favorito")
        print("8 - Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            buscar_auto(lista_vehiculos)
        elif opcion == "2":
            mostrar_lista(lista_vehiculos)
        elif opcion == "3":
            imprimir_certificado(lista_vehiculos, nombre_usuario, fecha_actual)
        elif opcion == "4":
            buscar_por_patente(lista_vehiculos)
        elif opcion == "5":
            buscar_por_rango_de_año(lista_vehiculos)
        elif opcion == "6":
            agregar_info_dueño(lista_vehiculos)
        elif opcion == "7":
            mostrar_por_color_favorito(lista_vehiculos, color_favorito)
        elif opcion == "8" or opcion == "":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar función principal
main(lista_vehiculos)
