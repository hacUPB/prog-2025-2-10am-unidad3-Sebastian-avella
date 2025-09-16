#Pseudocodigo combustible
Durante un vuelo, la velocidad de un avión depende de la aceleración aplicada por los motores, de la resistencia del aire y de la cantidad de combustible disponible.
El avión parte con una velocidad inicial de 500 km/h y un nivel de combustible definido por el usuario.
Cada 5 segundos el sistema descuenta 5 galones de combustible y actualiza la velocidad aplicando la fórmula
La simulación continúa hasta que el combustible se agote o se cumpla un tiempo máximo de 1 hora de vuelo.
 
| Tipo de variable | Nombre           | Descripción                                            | Unidad          |
|------------------|------------------|--------------------------------------------------------|-----------------|
| **Entrada**      | comb_inicial   | Combustible inicial  | int         |
|                  | v_inicial        | Velocidad inicial | float    |
|                  | a                | Aceleración  |      float     |
|                  | resistencia_aire | Factor de resistencia del aire |       float   |
| **Constante**    | comb_min         | Nivel mínimo de combustible seguro (= 100) |    int      |
|                  | t               | Intervalo de tiempo por iteración |   int    |
|                  | tiempo_max       | Tiempo máximo de simulación   |  int  |
| **Control**      | i             | Número de iteraciones  | int      |
|                  | tiempo           | Tiempo acumulado  |     int   |
| **Salida**       | velocidad        | Velocidad actual del avión |  float           |
|                  | comb_actual      | Combustible restante   |     int     |
|                  | v_objetivo       | Velocidad objetivo (400 o 500 según condición)  |     float        |
|                  | accion           | Acción tomada (acelerar, mantener, alerta)  |          string |
 
```
Inicio
 Leer comb_inicial =
    Leer v_inicial =
    Leer a =
    Leer resistencia_aire =
 
    comb_min = 100          // Combustible mínimo seguro
    t = 5                  // Intervalo de tiempo (5 segundos)
    tiempo_max = 3600       // Tiempo máximo de simulación (1 hora)
 
   
   comb_actual = comb_inicial
   velocidad = v_inicial
   v_objetivo = v_inicial
   tiempo = 0
   i = 0
   accion = ""
 
   
   Mientras (tiempo < tiempo_max and comb_actual > 0) Hacer
 
        Si comb_actual <= comb_min:
            v_objetivo = 400
            accion = " Desacelerar - ALERTA: Combustible bajo"
        Sino
            v_objetivo = 500
            Accion = "Acelerar"
        Fin Si
 
        SI (velocidad > v_objetivo)
            velocidad = velocidad - (resistencia_aire * t)
        Si no
             Si (velocidad < v_objetivo)
            velocidad = velocidad + (aceleracion * t)
        Fin Si
 
    tiempo = tiempo + t
    i = i + 1
    comb_actual= comb_actual - consumo
 
Imprimir ("Iteración:", iter, " Tiempo:", tiempo, " Combustible:", comb_actual, "Velocidad:", velocidad,  " Acción:", accion)
 
    Fin mientras
    Imprimir( ("Simulación finalizada");("Iteraciones:", i);("Tiempo total:", tiempo)
     ("Estado final= Velocidad:"), velocidad, " (Combustible:", comb_actual))
```
 
 
 
 
 
 
 
 
 
 
 
#Pseudocodigo altitud
 
Un avión debe estabilizarse en una altitud de 8000 pies. La altitud del avión depende de la velocidad y del ángulo de ataque, de modo que el cambio de altitud se calcula en cada paso mediante una relación proporcional a la velocidad y al ángulo, más un incremento fijo.
 
Si la altitud actual está por debajo de la altitud objetivo, el avión debe subir ajustando su ángulo de ataque.
Si la altitud actual está por encima, debe bajar disminuyendo su ángulo de ataque.
Si se encuentra en la altitud objetivo, debe mantenerse.
 
El proceso se repite de manera iterativa, ajustando la altitud en función de la fórmula definida, hasta un máximo de 20 iteraciones, mostrando en cada paso la altitud, el ángulo de ataque, la velocidad y la acción realizada.
 
 
## Clasificación de Variables
 
| Variable             | Descripción                                     | Tipo de Dato | Clasificación |
|----------------------|-------------------------------------------------|--------------|---------------|
| altitud | Altitud actual del avión| Float | Entrada / Estado del sistema |
| velocidad | Velocidad del avión  | Float| Entrada        |
| angulo_ataque  | Ángulo de ataque | Float| Variable de Control |
| altitud_objetivo| Altitud deseada de estabilización (8000 ft)| Entero| Constante|
| incremento_altitud | Cambio teórico de altitud por paso (100 ft)|  Entero | Constante|
| i |Contador de iteraciones| Entero | Variable de Control |
| accion| Descripción de la acción (subiendo, bajando, etc.) | Cadena    | Salida         |
 
'''
Inicio
 
    Leer altitud              
    Leer velocidad            
    Leer angulo_ataque =  "[-2, 15]"
 
    altitud_objetivo = 8000
    incremento_altitud = 100
    MAX_ITER = 20
 
    iter = 0
    accion = ""
 
 
    Mientras (iter < MAX_ITER) Hacer
 
        Si altitud < altitud_objetivo Entonces
            accion = "Subir"
            altitud = altitud + (velocidad * angulo_ataque * 0.01) + incremento_altitud
            angulo_ataque = angulo_ataque + 1
 
        Sino Si altitud > altitud_objetivo Entonces
            accion = "Bajar"
            altitud = altitud - (velocidad * angulo_ataque * 0.01) - incremento_altitud
            angulo_ataque = angulo_ataque - 1
 
        Sino
            accion = "Mantener altitud"
            altitud = altitud
            angulo_ataque = angulo_ataque
 
        FinSi
        Si angulo_ataque < -2 Entonces
            angulo_ataque =  -2
        FinSi
        Si angulo_ataque > 15 Entonces
            angulo_ataque= 15
        FinSi
 
        i = i +1
 
 
        Imprimir "Iteración: ", iter,
                 " | Altitud: ", altitud,
                 " | Velocidad: ", velocidad,
                 " | Ángulo de ataque: ", angulo_ataque,
                 " | Acción: ", accion
 
    FinMientras
 
FIN
'''
En el desarrollo de este ejercicio se utilizó el apoyo de una herramienta de inteligencia artificial (ChatGPT, de OpenAI) únicamente con fines académicos.
La IA fue empleada para estructurar el pseudocódigo y, principalmente, para determinar y ajustar la fórmula que relaciona la velocidad, el ángulo de ataque y la altitud.
Las decisiones finales de diseño, corrección y validación del algoritmo fueron revisadas y adaptadas por el autor
 
 
#Pseudocodigo flaps.
Un avión en fase de aproximación inicia con una velocidad de 220 nudos, un ángulo de ataque de 5° y los flaps retraídos (0°). En cada iteración, se calcula la tasa de descenso como tasa_descenso = velocidad × sin(angulo_ataque). Si la tasa de descenso supera 50 ft/s, los flaps deben aumentarse en 10°; si el ángulo de ataque excede 12°, los flaps deben reducirse en 10°; en cualquier otro caso, los flaps se mantienen. El ángulo de ataque se ajusta en ±0.5° según la acción tomada, y la velocidad disminuye en cada iteración en perdida_vel = 5 + flaps/2. El proceso se repite durante un máximo de 20 iteraciones o hasta que la velocidad sea menor a 80 nudos, mostrando en cada paso la iteración, la velocidad, el ángulo de ataque, los flaps, la tasa de descenso y la acción ejecutada.
 
 
 
| Variable         | Descripción                              | Tipo   | Clasificación       |
|------------------|------------------------------------------|--------|---------------------|
| velocidad | Velocidad del avión  | Float  | Entrada |
| angulo_ataque | Ángulo de ataque | Float  | Entrada |
| flaps| Posición de los flaps | Int    | Control / Salida    |
| tasa_descenso | Tasa de descenso calculado Float  | Variable de proceso |
| i | Número de iteración| Int    | Control      |
| accion | Acción realizada en la iteración         | Texto  | Salida  |
| MAX_ITER | Máximo de iteraciones  | Int    | Constante           |
| D_CRITICO | Límite de tasa de descenso  | Int    | Constante   |
| A_CRITICO  | Ángulo de ataque crítico   | Int    | Constante  |
 
´´´
INICIO
 
 
    velocidad = 220  
    angulo_ataque = 5
    flaps = 0
    iter = 0
 
    T = 10
    MAX_ITER =20
    D_CRITICO= 50
    A_CRITICO =12  
    FLAP_MIN = 0
    FLAP_MAX = 0
 
 
    MIENTRAS (iter < MAX_ITER) Y (velocidad > 80) HACER
 
     
        tasa_descenso =velocidad * sin(angulo_ataque * π / 180)
 
        SI (tasa_descenso > D_CRITICO) Entonces
            nuevo_flap =flaps + 10
            accion ="Aumentar flaps (ganar sustentación)"
        SINO SI (angulo_ataque > A_CRITICO) ENTONCES
            nuevo_flap =flaps - 10
            accion ="Reducir flaps (evitar pérdida)"
        SINO
            nuevo_flap =flaps
            accion ="Mantener flaps"
        FIN SI
 
        SI nuevo_flap < FLAP_MIN ENTONCES
             nuevo_flap ← FLAP_MIN
        FIN SI
        SI nuevo_flap > FLAP_MAX ENTONCES
            nuevo_flap ← FLAP_MAX
            FIN SI
 
 
        flaps= nuevo_flap
 
 
        SI accion = "Aumentar flaps (ganar sustentación)" ENTONCES
            angulo_ataque =angulo_ataque + 0.5
        SINO
        SI accion = "Reducir flaps (evitar pérdida)" ENTONCES
            angulo_ataque =angulo_ataque - 0.5
        FIN SI
 
     
        SI angulo_ataque < -5 ENTONCES
             angulo_ataque ← -5
        FIN SI
        SI angulo_ataque > 18 ENTONCES
        angulo_ataque ← 18
         FIN SI
 
        perdida_vel= 5 + (flaps / 2)
        velocidad =velocidad - perdida_vel
 
        SI velocidad < 0 ENTONCES
         velocidad ← 0
         FIN SI
 
   
        i= i+ 1
 
        IMPRIMIR( "Iteración:", iter;"Velocidad:", round(velocidad,1), "nudos";A:", round(angulo_ataque,2), "°","Flaps:", flaps, "°"Tasa_descenso:", round(tasa_descenso,2), "ft/s", "| Acción:", accion)
 
    FIN MIENTRAS
 
FIN
 
 
 
 
 
# DECLARACION IA
Este ejercicio fue desarrollado con apoyo de una herramienta de inteligencia artificial (IA), utilizada específicamente para:
#ormular y ajustar el enunciado del problema.
 
Determinar y validar las expresiones matemáticas empleadas (cálculo de la tasa de descenso y pérdida de velocidad).
 
Organizar el pseudocódigo y verificar su coherencia lógica mediante pruebas de escritorio.
 
El planteamiento, adaptación y validación final del ejercicio fueron realizados por nosotros
 
 
 


 # Prueba de escritorio del primer ejercicio
 Valores iniciales

comb_inicial = 200 gal
v_inicial = 500 km/h
a = 2 km/h²
resistencia_aire = 1 km/h²
consumo = 5 gal/iteración
t = 5 s
comb_min = 100 gal
tiempo_max = 3600 s

Inicialización

comb_actual = 200velocidad = 500tiempo = 0i = 0

Reglas

En cada iteración:

Si comb_actual <= comb_min ⇒ v_objetivo = 400, accion = "Desacelerar - ALERTA"
Si comb_actual > comb_min ⇒ v_objetivo = 500, accion = "Acelerar"
Si velocidad > v_objetivo ⇒ velocidad = velocidad - (resistencia_aire * t)
Si velocidad < v_objetivo ⇒ velocidad = velocidad + (a * t)
tiempo = tiempo + t
i = i + 1
comb_actual = comb_actual - consumo

Cálculo clave

Cada iteración consume 5 gal ⇒ 200 / 5 = 40 iteraciones hasta quedarse en 0.

Después de 20 iteraciones: comb_actual = 200 - 20*5 = 100.

    En las primeras 20 iteraciones la condición comb_actual > 100 se cumple al inicio de la iteración, por eso la alerta se activa en la iteración 21 (cuando comb_actual al inicio es 100).

Reducción de velocidad en modo ALERTA: cada iteración resta resistencia_aire * t = 1 * 5 = 5 km/h.

    Desde la iteración 21 hasta la 40 hay 20 iteraciones en ALERTA → velocidad se reduce 20 * 5 = 100 km/h.
    Velocidad final = 500 - 100 = 400 km/h.

Iteraciones clave
| Iter | Tiempo (s) | Comb (gal) | Vel (km/h) | Acción               |
| ---- | ---------- | ---------- | ---------- | -------------------- |
| 1    |    5       |   195      | 500        | Acelerar             |
| 5    |    25      |   175      | 500        | Acelerar             |
| 10   |    50      |   150      | 500        | Acelerar             |
| 20   |    100     |   100      | 500        | Acelerar             |
| 21   |    105     |   95       | 495        | Desacelerar – ALERTA |
| 30   |    150     |   50       | 450        | Desacelerar – ALERTA |
| 39   |    195     |   5        | 405        | Desacelerar – ALERTA |
| 40   |    200     |   0        | 400        | Desacelerar – ALERTA |

Resultado final :
Simulación finalizada
Iteraciones: 40
Tiempo total: 200 s (3 min 20 s)
Estado final = Velocidad: 400 km/h | Combustible: 0 gal
