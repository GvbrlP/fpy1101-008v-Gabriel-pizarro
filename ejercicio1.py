# Inicializar contadores para clasificar médicos por experiencia
medicos_residentes = 0  # Contador de médicos con 5 años o menos de experiencia
medicos_especialistas = 0  # Contador de médicos con más de 5 años de experiencia

# Mostrar encabezado del programa
print("\n____Registro de Medicos____")

# Bucle para solicitar la cantidad total de médicos a registrar
while True:
    try:
        # Solicitar al usuario el número total de médicos a ingresar
        medicos_total = int(input("\ningrese el numero de medicos: "))
        # Validar que la cantidad no sea negativa
        if medicos_total < 0:
            print("registro de medicos no puede ser negativo.")   
        else:
            # Salir del bucle si la entrada es válida
            break
    except ValueError:
        # Capturar error si el usuario no ingresa un número entero
        print("por favor, ingrese un numero valido.")

# Ciclo para registrar cada médico
for i in range(medicos_total):
    # VALIDACIÓN 1: Solicitar y validar el nombre del médico
    while True:
        # Pedir nombre del médico (con número de orden)
        medico_nombre = input(f"\ningrese el nombre del medico {i+1}: (6 caracteres o mas no debe incluir espacios): ")
        # Validar que el nombre tenga al menos 6 caracteres y no contenga espacios
        if (len(medico_nombre) < 6 ) or (" " in medico_nombre):
            print("el nombre del medico debe tener 6 caracteres o mas.")
        else:
            # Nombre válido, pasar a siguiente validación
            break
    
    # VALIDACIÓN 2: Solicitar y validar los años de experiencia
    while True:
        try:
            # Solicitar los años de experiencia del médico
            medico_experiencia = int(input("\ningrese los años de experiencia del medico: "))
            # Validar que la experiencia sea un número positivo
            if medico_experiencia < 0:
                print("por favor, ingrese un numero valido.")
            else:
                # Clasificar al médico según su experiencia
                if medico_experiencia <= 5:
                    # Si tiene 5 años o menos, es residente
                    medicos_residentes += 1
                else:
                    # Si tiene más de 5 años, es especialista
                    medicos_especialistas += 1
                # Salir del bucle después de registrar correctamente
                break
        except ValueError:
            # Capturar error si el usuario no ingresa un número entero
            print("por favor, ingrese un numero mayor a 0.")

# Mostrar encabezado de resultados
print("\n____Resultados____")
print("El hospital cuenta con:")
# Mostrar totales clasificados
print(f"Medicos especialistas: {medicos_especialistas}")
print(f"Medicos residentes: {medicos_residentes}")
