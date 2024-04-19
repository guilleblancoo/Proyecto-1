# Inicialización de variables globales
galones_regular = 40.0
galones_super = 40.0
galones_diesel = 40.0
trabajadores_diurnos = 1
trabajadores_vespertinos = 1
trabajadores_nocturnos = 1

# Costos de almacenamiento
costo_almacenamiento_regular = 7.00
costo_almacenamiento_super = 8.00
costo_almacenamiento_diesel = 6.00

# Precio gasolina
precio_regular = 29.00
precio_super = 30.00
precio_diesel = 26.50

# Salario por turnos
salario_diurno = 14.00
salario_vespertino = 14.50
salario_nocturno = 15.50

# Ingresos
ingresos_totales = 0

def inventario():
    global galones_regular, galones_super, galones_diesel
    print("---------------------------")
    print("Inventario actual:")
    print("Gasolina regular: ", galones_regular ,"galones")
    print("Gasolina súper: ", galones_super ,"galones")
    print("Diésel: ", galones_diesel ,"galones")
    agregar = input("¿Desea agregar combustible? (s/n): ")
    if agregar.lower() == "s":
        regular = int(input("Ingrese la cantidad de gasolina regular a agregar (en galones): "))
        super_ = int(input("Ingrese la cantidad de gasolina súper a agregar (en galones): "))
        diesel = int(input("Ingrese la cantidad de diésel a agregar (en galones): "))
        print("---------------------------")
        
        # Validación para gasolina regular
        if regular + galones_regular <= 80:
            galones_regular += regular
            print("Se agregaron ", regular ,"galones de gasolina regular.")
        else:
            print("La cantidad de gasolina regular a agregar supera la capacidad máxima del depósito.")
        
        # Validación para gasolina súper
        if super_ + galones_super <= 80:
            galones_super += super_
            print("Se agregaron ", super_ ,"galones de gasolina súper.")
        else:
            print("La cantidad de gasolina súper a agregar supera la capacidad máxima del depósito.")
        
        # Validación diésel
        if diesel + galones_diesel <= 80:
            galones_diesel += diesel
            print("Se agregaron ", diesel ,"galones de diésel.")
        else:
            print("La cantidad de diésel a agregar supera la capacidad máxima del depósito.")

def venta():
    global galones_regular, galones_super, galones_diesel, ingresos_totales
    print("---------------------------")
    print("Inventario actual:")
    print("Gasolina regular: ", galones_regular ,"galones Q", galones_regular*precio_regular)
    print("Gasolina súper: ",galones_super ,"galones Q", galones_super*precio_super)
    print("Diésel: ", galones_diesel ,"galones Q", galones_diesel*precio_diesel)
    combustible = input("Seleccione el tipo de combustible (1)regular, (2)súper o (3)diesel: ").lower()
    if combustible not in ["1", "2", "3"]:
        print("Tipo de combustible inválido.")
        return

    if combustible == "1":
        galones = galones_regular
        precio_combustible = precio_regular
    elif combustible == "2":
        galones = galones_super
        precio_combustible = precio_super
    elif combustible == "3":
        galones = galones_diesel
        precio_combustible = precio_diesel

    if galones <= 5:
        print("---------------------------")
        print("El depósito de combustible está agotado. No se puede realizar la venta.")
        print("---------------------------")
        return

    venta_por = input("¿Desea vender por galón o por quetzales? (1)galón o (2)quetzales: ").lower()
    if venta_por not in ["1", "2"]:
        print("---------------------------")
        print("Opción inválida.")
        print("---------------------------")
        return

    if venta_por == "1":
        galones_vender = float(input("Ingrese la cantidad de galones a vender: "))
        if galones_vender > galones:
            print("---------------------------")
            print("No hay suficiente combustible en inventario para realizar la venta.")
            print("---------------------------")
            return

        nombre = input("Nombre completo: ")
        nit = input("NIT: ")
        numero_bomba = int(input("Número de bomba (entre 1 y 4): "))
        print("---------------------------")
        print("Detalles de compra")
        print("---------------------------")
        print("Nombre: ", nombre)
        print("NIT: ", nit)
        print("Número de bomba: ", numero_bomba)
        print("Total: Q", galones_vender * 29)
        print("---------------------------")
    else:
        quetzales = float(input("Ingrese la cantidad de quetzales a vender: "))
        galones_vender = quetzales / precio_combustible
        if galones_vender > galones:
            print("---------------------------")
            print("No hay suficiente combustible en inventario para realizar la venta.")
            print("---------------------------")
            return

        nombre = input("Nombre completo: ")
        nit = input("NIT: ")
        numero_bomba = int(input("Número de bomba (entre 1 y 4): "))
        print("---------------------------")
        print("Detalles de compra")
        print("---------------------------")
        print("Nombre: ",nombre)
        print("NIT: ",nit)
        print("Número de bomba: ", numero_bomba)
        print("Total: Q", galones_vender*precio_combustible)
        print("---------------------------")

    realizar_compra = input("¿Desea proceder con la compra de combustible? (s/n): ").lower()
    if realizar_compra == "s":       
        if combustible == "1":
            galones_regular -= galones_vender
            ingresos_totales += galones_vender * precio_combustible
        elif combustible == "2":
            galones_super -= galones_vender
            ingresos_totales += galones_vender * precio_combustible
        elif combustible == "3":
            galones_diesel -= galones_vender
            ingresos_totales += galones_vender * precio_combustible

        print("---------------------------")
        print("Compra exitosa.")
        print("---------------------------")
    else:
        print("Compra de combustible cancelada.")

def turnos():
    global trabajadores_diurnos, trabajadores_vespertinos, trabajadores_nocturnos
    print("---------------------------")
    print("Trabajadores diurnos: ",trabajadores_diurnos)
    print("Trabajadores vespertinos: ", trabajadores_vespertinos)
    print("Trabajadores nocturnos: ", trabajadores_nocturnos)
    print("---------------------------")

    jornada = input("Seleccione la jornada diurna, vespertina o nocturna: ").lower()
    if jornada == "diurna":
        trabajadores = trabajadores_diurnos
    elif jornada == "vespertina":
        trabajadores = trabajadores_vespertinos
    elif jornada == "nocturna":
        trabajadores = trabajadores_nocturnos

    accion = input("¿Desea añadir o retirar trabajadores? (1)añadir o (2)retirar: ").lower()
    if accion == "1":
        cantidad = int(input("Ingrese la cantidad de trabajadores a añadir: "))
        
        print(cantidad ,"trabajador(es) añadido(s) a la jornada" ,jornada)
        if jornada == "diurna":
            trabajadores_diurnos += cantidad
        elif jornada == "vespertina":
            trabajadores_vespertinos += cantidad
        elif jornada == "nocturna":
            trabajadores_nocturnos += cantidad
    elif accion == "2":
        cantidad = int(input("Ingrese la cantidad de trabajadores a retirar: "))
        if cantidad > trabajadores:
            print("No hay suficientes trabajadores en esta jornada.")
            return

        print(cantidad ,"trabajador(es) retirado(s) de la jornada ", jornada)
        if jornada == "diurna":
            trabajadores_diurnos -= cantidad
        elif jornada == "vespertina":
            trabajadores_vespertinos -= cantidad
        elif jornada == "nocturna":
            trabajadores_nocturnos -= cantidad

def reportes():
    global galones_regular, galones_super, galones_diesel
    costo_almacenamiento_regular = 7 * galones_regular
    costo_almacenamiento_super = 8 * galones_super
    costo_almacenamiento_diesel = 6 * galones_diesel
    costo_materia_prima = costo_almacenamiento_regular + costo_almacenamiento_super + costo_almacenamiento_diesel
    salario_diurno = 14 * trabajadores_diurnos
    salario_vespertino = 14.5 * trabajadores_vespertinos
    salario_nocturno = 15.5 * trabajadores_nocturnos
    salario_mano_obra = salario_diurno + salario_vespertino + salario_nocturno
    costos_fijos = 10
    utilidad_bruta = ingresos_totales - costo_materia_prima - salario_mano_obra - costos_fijos
    print("---------------------------")
    print("Reporte de rentabilidad:")
    print("---------------------------")
    print("Ingresos totales: Q", ingresos_totales)
    print("---------------------------")
    print("Materia prima")
    print("---------------------------")
    print("Costo combustible Regular: Q", costo_almacenamiento_regular)
    print("Costo combustible Súper: Q", costo_almacenamiento_super)
    print("Costo Diesel: Q", costo_almacenamiento_diesel)
    print("Total: Q", costo_materia_prima)
    print("---------------------------")
    print("Mano de obra")
    print("---------------------------")
    print("Salario Jornada Diurna: Q", salario_diurno)
    print("Salario Jornada Vespertina: Q", salario_vespertino)
    print("Salario Jornada Nocturna: Q", salario_nocturno)
    print("Total: Q", salario_mano_obra)
    print("---------------------------")
    print("Costos Fijos: Q", costos_fijos)
    print("Utilidad Bruta: Q", utilidad_bruta)
    print("---------------------------")

def menu():
    while True:
        print("---------------------------")
        print("  GASOLINERAS JAGUAR")
        print("---------------------------")
        print("Menú:")
        print("1. Gestionar inventario")
        print("2. Venta de combustible")
        print("3. Gestión de turnos")
        print("4. Reporte de rentabilidad")
        print("5. Salir")
        print("---------------------------")
        
        opcion = input("Ingrese una opción (1-5): ")
        
        if opcion == "1":
            inventario()
        elif opcion == "2":
            venta()
        elif opcion == "3":
            turnos()
        elif opcion == "4":
            reportes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()