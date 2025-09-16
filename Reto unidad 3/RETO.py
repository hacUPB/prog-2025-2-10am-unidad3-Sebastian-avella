'''
|Variable        |Entrada/Salida   |Descripción|
|----------------|-----------------|-----------|
|Peso_vacio      |Entrada          |Peso vacio de la aeronave|
|Combustible     |Entrada          |Cantidad inicial de combustible (litros)|
|Altitud         |Entrada          | Altitud de vuelo (pies)|
|Peso_aeronave   |Entrada          |Peso de la aeronave (kg)|
|opcion Cadena   |Entrada          |Selección del menú (A, B, C, D)|
|velocidad       |Entrada          |Velocidad del avión (km/h)|
|ajuste          |Proceso          |Factor de corrección del consumo según velocidad|
|consumo_final   |Salida           |Consumo ajustado en litros/hora|
|consumo_ajustado|Salida           |Resultado final mostrado al usuario|
|Peso_comb       |Entrada          | Peso del combustible cargado en kilogramos|
|Peso_carga      |Entrada          |Peso de la carga transportada en kilogramos.|
|Peso_max        |Entrada          |Peso máximo permitido para el avión en kilogramos.|
|Paso            |Constante        |Incremento o decremento de peso en cada ajuste, medido en kilogramos.|
|Peso_total      |Proceso          |Resultado de la suma del peso vacío, combustible y carga.|
|alt_actual      |entrada          | Altitud inicial del avión en pies|
|alt_objetivo    |Constante        | Altitud deseada del avión (8000 pies).|
|alt_max         |Entrada          | Margen de tolerancia permitido para la altitud |
|comb_actual     |Entrada          |Cantidad inicial de combustible disponible en galones|
|comb_min        |Constante        | Nivel mínimo de combustible seguro, equivalente a 30 galones.|
|velocidad | Proceso |Velocidad del avión en km/h ajustada durante el vuelo.|
|movimiento |Proceso|Estado del avión en cada paso: subir, bajar, mantener estable, acelerar o desacelerar.|
|Control |Control| Contador de iteraciones de cada ciclo de ajuste|
|Max_iter |Constante| Límite máximo de iteraciones para evitar bucles infinitos.|
|Iteración | Salida| Número de pasos o ciclos realizados.|
|Salida |Salida| Resultado final mostrado al usuario (peso ajustado, altitud estabilizada o nivel de combustible y velocidad).|
''' 
#Pseudocodigo combustible
#Durante un vuelo, la velocidad del avión depende de la cantidad de combustible disponible.
#El sistema comienza con un nivel inicial de combustible (en galones) y una velocidad base de 500 km/h.
#Si el combustible actual es menor o igual a 30 galones (nivel mínimo seguro), el avión debe desacelerar para ahorrar energía y mostrar una alerta de bajo combustible.
#Si el combustible es mayor al mínimo, debe acelerar para mantener la potencia de vuelo.
#En cada iteración, se descuenta un consumo de combustible, y el proceso se repite hasta agotar el límite de control o que el combustible llegue a cero.
#El sistema imprime en cada paso la iteración, combustible restante, velocidad y acción tomada.

'''
Inicio
    Leer comb_actual            // Combustible inicial en galones
    comb_min = 30               // Combustible mínimo seguro en galones
    velocidad = 500             // Velocidad inicial en km/h
    accion = ""                 // Inicializa acción
    Control = 0                 // variable de control
    Max_iter = 20               // límite de iteraciones para detener el ciclo
 
    Mientras (Control < Max_iter) Y (comb_actual > 0) Hacer
        Si comb_actual <= comb_min Entonces
            accion = "Desacelerar - ALERTA: Bajo combustible"
            velocidad = velocidad - 50   // Reducir velocidad
        Sino
            accion = "Acelerar"
            velocidad = velocidad + 50   // Aumentar velocidad
        FinSi
 
        Control = Control + 1
        comb_actual = comb_actual - 5    // Consumo simulado de 5 galones por iteración
 
        Imprimir "Iteración: ", Control, 
                 " Combustible: ", comb_actual, " galones", 
                 " Velocidad: ", velocidad, " km/h", 
                 " Acción: ", accion
    FinMientras
 
    Imprimir "Ciclo finalizado después de ", Control, " iteraciones."
Fin
'''

#Pseudocodigo altitud
#Un avión debe estabilizarse cerca de una altitud de 8000 pies con un margen de error de ±200 pies.
#Si la altitud actual está por debajo del rango permitido, el avión debe subir en incrementos de 100 ft.
#Si está por encima, debe bajar en decrementos de 100 ft.
#Cuando se encuentre dentro del rango permitido, el avión debe mantener la altitud.
#El sistema debe mostrar en cada iteración la altitud actual, la acción realizada y la cantidad de iteraciones.

'''
Inicio
    Leer alt_actual         // Altitud inicial del avión (ft)
    alt_objetivo = 8000     // Altitud deseada (ft)
    Leer alt_max            // Margen permitido (ej: 200 ft)
    movimiento = ""         // Inicializa movimiento
    Control = 0             // Variable de control
    Max_iter = 200          // Límite de iteraciones
 
    Mientras (abs(alt_actual - alt_objetivo) > alt_max) Y (Control < Max_iter) Hacer
        Si alt_actual < (alt_objetivo - alt_max) Entonces
            movimiento = "Subir"
            alt_actual = alt_actual + 100
        Sino Si alt_actual > (alt_objetivo + alt_max) Entonces
            movimiento = "Bajar"
            alt_actual = alt_actual - 100
        FinSi
 
        Control = Control + 1
        Imprimir "Iteración: ", Control, 
                 " Altitud actual: ", alt_actual, " ft", 
                 " Movimiento: ", movimiento
    FinMientras
 
    movimiento = "Mantener estable"
    Imprimir "Altitud final cercana a ", alt_objetivo, " ft. Estado: ", movimiento
Fin
'''


#Pseudocodigo peso.
#Antes de despegar, una aerolínea debe asegurarse de que el peso total del avión no exceda el peso máximo autorizado.
#El sistema recibe como datos el peso vacío de la aeronave, el peso del combustible cargado y el peso de la carga.
#Con estos valores:
#Se calcula el peso total.
#Si no coincide con el peso máximo permitido, se realizan ajustes en incrementos de 1 kg hasta alcanzar el límite exacto.
#En cada ajuste se imprime el valor del peso y el número de iteración
'''
Inicio
    Leer Peso_vacio      // Peso vacío de la aeronave (kg)
    Leer Peso_comb       // Peso del combustible (kg)
    Leer Peso_carga      // Peso de la carga (kg)
    Leer Peso_max        // Peso máximo autorizado (kg)
 
    Paso = 1             // Cantidad de peso a ajustar en cada iteración (kg)
    Control = 0          // Variable de control
    Max_iter = 1000      // Límite de seguridad para detener el ciclo
 
    Peso_total = Peso_vacio + Peso_comb + Peso_carga
 
    Mientras (Peso_total ≠ Peso_max) Y (Control < Max_iter) Hacer
        Si Peso_total < Peso_max Entonces
            Peso_total = Peso_total + Paso
        Sino
            Peso_total = Peso_total - Paso
        FinSi
        Control = Control + 1
        Imprimir "Iteración: ", Control, " Peso total: ", Peso_total, " kg"
    FinMientras
 
    Imprimir "Peso total ajustado: ", Peso_total, " kg"
Fin
'''

# DECLARACION IA
# Para complementar y organizar mejor las ideas en la construcción de los pseudocódigos, utilizamos una herramienta de inteligencia artificial como apoyo. 
# Esta se usó únicamente como guía, pero la comprensión, adaptación y explicación  del trabajo son de nuestra autoría.

while True:
    Combustible = int(input ("Ingrese la cantidad del combustible"))
    Altitud = int(input ("Ingrese la altitud "))
    Peso_aeronave = int(input ("Ingrese el peso_aeronave"))
    print("=== MENÚ PRINCIPAL ===")
    print("A. Combustible\nB. Altitud\nC Peso_aeronave\nD Salir")
 
    opcion = input("Selecciona una opción")
    opcion = opcion.upper()
    match opcion:
        case "A":
            print("Combustible")
 
        case "B":
            print("Altitud")
 
        case "C":
            print("Peso_aeronave")
 
        case "D":
            print("Salir")
        case _:
            print("Opción inválida.")