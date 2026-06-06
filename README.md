# FPY1101 - Prueba Parcial 3: Sistema de Gestión Hospitalaria y de Biblioteca

Conjunto de ejercicios prácticos para la evaluación parcial 3 del curso FPY1101. Los programas implementan sistemas de validación de datos, bucles, manejo de excepciones y estructuras de control en Python.

---

## 📋 Contenido

- **Ejercicio 1**: Sistema de Registro y Clasificación de Médicos
- **Ejercicio 2**: Sistema de Gestión de Préstamo de Libros

---

## 🏥 Ejercicio 1: Registro de Médicos

### Descripción
Sistema que permite registrar médicos en un hospital y clasificarlos automáticamente según su experiencia laboral en dos categorías:
- **Médicos Residentes**: ≤ 5 años de experiencia
- **Médicos Especialistas**: > 5 años de experiencia

### Funcionalidades
✅ Solicitud validada de cantidad total de médicos  
✅ Validación de nombres (mínimo 6 caracteres, sin espacios)  
✅ Validación de años de experiencia (números positivos)  
✅ Clasificación automática por nivel de experiencia  
✅ Reporte final con totales de cada categoría  

### Requisitos
- Python 3.x
- Ninguna librería externa

### Cómo Usar
```bash
python ejercicio1.py
```

### Flujo del Programa
1. Ingresa la cantidad total de médicos a registrar
2. Para cada médico, ingresa:
   - Nombre (mínimo 6 caracteres, sin espacios)
   - Años de experiencia (número positivo)
3. El programa clasifica automáticamente y muestra el reporte final

### Ejemplo de Ejecución
```
____Registro de Medicos____

ingrese el numero de medicos: 3

ingrese el nombre del medico 1: (6 caracteres o mas no debe incluir espacios): JuanPerez
ingrese los años de experiencia del medico: 4

ingrese el nombre del medico 2: (6 caracteres o mas no debe incluir espacios): MariaLopez
ingrese los años de experiencia del medico: 8

ingrese el nombre del medico 3: (6 caracteres o mas no debe incluir espacios): CarlosSanchez
ingrese los años de experiencia del medico: 3

____Resultados____
El hospital cuenta con:
Medicos especialistas: 1
Medicos residentes: 2
```

### Validaciones Implementadas
| Validación | Criterio | Mensaje de Error |
|-----------|----------|------------------|
| Cantidad de médicos | Número no negativo | "registro de medicos no puede ser negativo" |
| Nombre del médico | ≥ 6 caracteres, sin espacios | "el nombre del medico debe tener 6 caracteres o mas" |
| Años de experiencia | Número positivo | "por favor, ingrese un numero mayor a 0" |
| Entrada numérica | Debe ser número entero | "por favor, ingrese un numero valido" |

---

## 📚 Ejercicio 2: Sistema de Gestión de Biblioteca

### Descripción
Sistema interactivo para gestionar el inventario de una biblioteca permitiendo realizar préstamos, devoluciones y consultar el historial de transacciones.

### Funcionalidades
✅ Consultar libros disponibles en el inventario  
✅ Realizar préstamos de libros (con validación de stock)  
✅ Devolver libros prestados (con control de capacidad máxima)  
✅ Ver historial total de préstamos realizados  
✅ Interfaz de menú interactivo  

### Requisitos
- Python 3.x
- Ninguna librería externa

### Cómo Usar
```bash
python ejercicio2.py
```

### Flujo del Programa
1. Se muestra un menú con 5 opciones
2. El usuario selecciona una opción (1-5)
3. Según la opción:
   - **Opción 1**: Muestra cantidad actual de libros disponibles
   - **Opción 2**: Realiza un préstamo (valida stock disponible)
   - **Opción 3**: Recibe una devolución (valida capacidad máxima)
   - **Opción 4**: Muestra total de libros prestados en toda la sesión
   - **Opción 5**: Termina el programa

### Ejemplo de Ejecución
```
===MENÚ PRINCIPAL===
1. Libros disponibles
2. Realizar préstamo
3. Devolver préstamo
4. Historial de préstamos
5. Salir
Seleccione una opción(1-5): 1

===LIBROS DISPONIBLES===
Libros disponibles: 120

===MENÚ PRINCIPAL===
1. Libros disponibles
2. Realizar préstamo
3. Devolver préstamo
4. Historial de préstamos
5. Salir
Seleccione una opción(1-5): 2

===REALIZAR PRÉSTAMO===
Ingrese el número de libros a prestar: 5
Préstamo realizado. Libros prestados: 5. Stock restante: 115.

===MENÚ PRINCIPAL===
...
Seleccione una opción(1-5): 5
Saliendo del programa. ¡Hasta luego!
```

### Validaciones Implementadas
| Validación | Criterio | Mensaje de Error |
|-----------|----------|------------------|
| Opción del menú | Número entre 1-5 | "Opción no válida. Por favor, seleccione una opción del 1 al 5." |
| Cantidad a prestar | ≥ 1 y ≤ stock disponible | "No hay suficientes libros disponibles para prestar" |
| Cantidad a devolver | ≥ 1 y no exceda capacidad máxima | "No se pueden devolver más libros de los que el sistema puede manejar" |
| Entrada numérica | Debe ser número entero | "Entrada no válida. Por favor, ingrese un número entero." |

### Configuración del Sistema
- **Capacidad máxima**: 120 libros
- **Stock inicial**: 120 libros
- **Contador de préstamos**: Acumula todos los libros prestados en la sesión

---

## 🔧 Características Técnicas Comunes

### Manejo de Excepciones
Ambos programas utilizan bloques `try-except` para:
- Capturar entradas no numéricas (`ValueError`)
- Mostrar mensajes de error claros al usuario
- Solicitar reintentos sin terminar el programa

### Validación de Datos
- Validación de tipos de datos (números enteros)
- Validación de rangos (números positivos)
- Validación de formato (longitud de strings, ausencia de espacios)

### Estructuras de Control
- **Bucles `while`**: Para reintentos y menús interactivos
- **Bucles `for`**: Para iteración sobre cantidades
- **Condicionales `if-elif-else`**: Para lógica de validación y decisiones

---

## 📝 Notas Importantes

- Los programas validan todas las entradas del usuario antes de procesarlas
- Ambos programas utilizan bucles infinitos controlados para permitir reintentos
- Los comentarios en el código explican cada sección del programa
- Los mensajes de error son específicos y guían al usuario

---

## 👨‍💻 Autor
Gabriel Pizarro - FPY1101-008v

---

## 📌 Requisitos del Curso
- ✅ Uso de bucles (while, for)
- ✅ Manejo de excepciones (try-except)
- ✅ Validación de entrada
- ✅ Condicionales
- ✅ Contadores y acumuladores
- ✅ Comentarios de código
