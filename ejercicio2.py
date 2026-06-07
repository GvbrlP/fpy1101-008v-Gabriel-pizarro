# Inicializar variables de control del inventario
maximo_libros = 120  # Capacidad máxima del inventario
stock_libros = 120   # Cantidad actual de libros disponibles
historial_prestamos = 0  # Contador total de libros prestados

# Bucle principal del programa
while True:
    # Mostrar menú de opciones al usuario
    print("\n____MENÚ PRINCIPAL____")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    try:
        # Solicitar al usuario que seleccione una opción del 1 al 5
        opcion = int(input("Seleccione una opción(1-5): "))
        # Validar que la opción esté dentro del rango permitido
        if opcion < 1 or opcion > 5:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        else:
            # OPCIÓN 1: Mostrar libros disponibles en el inventario
            if opcion == 1:
                print("\n____LIBROS DISPONIBLES____")
                print(f"Libros disponibles: {stock_libros}")
    
            # OPCIÓN 2: Realizar préstamo de libros
            elif opcion == 2:
                print("\n____REALIZAR PRÉSTAMO____")
                try:
                    # Solicitar cantidad de libros a prestar
                    libro_prestado = int(input("Ingrese el número de libros a prestar: "))
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número entero.")
                # Validar que la cantidad sea positiva
                if libro_prestado < 1:
                    print("Número de libros a prestar debe ser al menos 1.")
                # Validar que hay suficiente stock disponible
                elif libro_prestado > stock_libros:
                    print(f"No hay suficientes libros disponibles para prestar. Stock actual: {stock_libros}.")
                else:
                    # Actualizar el stock y el historial de préstamos
                    stock_libros -= libro_prestado
                    historial_prestamos += libro_prestado
                    print(f"Préstamo realizado. Libros prestados: {libro_prestado}. Stock restante: {stock_libros}.")
    
            # OPCIÓN 3: Devolver libros prestados
            elif opcion == 3:
                print("\n____DEVOLVER PRÉSTAMO____")
                try:
                    # Solicitar cantidad de libros a devolver
                    libro_devuelto = int(input("Ingrese el número de libros a devolver: "))
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número entero.")
                # Validar que la cantidad sea positiva
                if libro_devuelto < 1:
                    print("Número de libros a devolver debe ser al menos 1.")
                # Validar que no se exceda la capacidad máxima del inventario
                elif stock_libros + libro_devuelto > maximo_libros:
                    print(f"No se pueden devolver más libros de los que el sistema puede manejar. Stock actual: {stock_libros}. Máximo permitido: {maximo_libros}.")
                else:
                    # Actualizar el stock de libros
                    stock_libros += libro_devuelto
                    print(f"Devolución realizada. Libros devueltos: {libro_devuelto}. Stock actual: {stock_libros}.")
    
            # OPCIÓN 4: Mostrar historial total de préstamos
            elif opcion == 4:
                print("\n____HISTORIAL DE PRÉSTAMOS____")
                print(f"Total de préstamos realizados: {historial_prestamos}")
    
            # OPCIÓN 5: Salir del programa
            elif opcion == 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
    except ValueError:
        # Capturar error si el usuario no ingresa un número válido
        print("Entrada no válida. Por favor, ingrese un número entero para seleccionar una opción.")
