# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Integrantes:** Villacís Vega Alejandro Xavier, Guido Fidel Quilumba Diaz, Jhon Jairo Tiupul Irua, Aitana Raquel Gomez Guaman · **Fecha:** 18/11/2026
**Repositorio (fork):** https://github.com/argg1006/IDSD422-lab2-diseno-encuesta
**Enfoque del equipo (aprobado en clase):** Compra en línea / app: experiencia.

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivo de la encuesta

Estimar el porcentaje de satisfacción con la compra en la app de RetailAndina mediante una encuesta aplicada en noviembre de 2026 a los clientes residentes en Quito que compraron en línea entre agosto y octubre de 2026, para decidir si el programa de fidelización se lanza en la aplicación.

**Definiciones operativas:**

- **Satisfecho:** responde 4 (Satisfecho) o 5 (Muy satisfecho) en la pregunta 6.
- **Probablemente usaría el programa:** responde 4 (Probable) o 5 (Muy probable) en la pregunta 8.

Los porcentajes se calculan sobre las respuestas válidas de origen real; las simuladas solo se usan para practicar los análisis.

**Regla de decisión:** si al menos el 70 % de los encuestados está satisfecho (4 o 5 en P6) y al menos el 60 % probablemente usaría el programa (4 o 5 en P8), se recomienda lanzarlo primero en la aplicación. Como la muestra es por conveniencia, el resultado se presenta como evidencia preliminar para la gerencia y no como una estimación de toda la población.

## 2. Población objetivo

- **Población:** personas de 18 años o más, residentes en la ciudad de Quito, que realizaron al menos una compra en línea (app o página web) en RetailAndina entre agosto y octubre de 2026.
- **Límites y justificación:**
  - Se fija el límite en 18 años o más porque a esa edad las personas pueden dar su consentimiento informado y deciden sus compras por cuenta propia.
  - Se consideran solo residentes de Quito porque la decisión se toma para esta ciudad: en otras ciudades las entregas, la cobertura y el stock pueden ser distintos. Además, facilita la recolección.
  - Se consideran las personas que compraron en línea entre agosto y octubre de 2026 porque pueden evaluar una experiencia de compra reciente y real. Esto también permite llegar a ellas mediante los contactos del equipo.
  - Quedan excluidos los menores de 18 años, las personas que viven fuera de Quito, quienes solo compran en la tienda física o no compraron en línea en ese periodo, y los integrantes del equipo, para evitar conflictos de interés.

**Preguntas filtro** (al inicio del formulario; las respuestas que no cumplen se descartan al procesar los datos con `scripts/muestreo.py`):

1. Edad (Menor a 18 años / Entre 18 y 35 años / Entre 36 y 50 años / Mayor a 50 años): se descarta a quien marca «Menor a 18 años».
2. ¿Actualmente reside en la ciudad de Quito? (Si / No): se descarta a quien responde No.
3. Pregunta 1 del cuestionario: su opción mínima es «1 compra», así que solo pueden contestarla quienes compraron en línea entre agosto y octubre de 2026.

**Nota:** el formulario también pregunta el género (Femenino / Masculino). No se usa como filtro y esa columna se elimina antes de compartir los datos (ver sección 6).

## 3. Método de muestreo

- **Método:** muestreo por conveniencia más referidos. Después se comparan, de forma descriptiva, los clientes ocasionales y frecuentes según la pregunta 1.
- **Justificación:** RetailAndina es ficticia y no tenemos acceso a un marco de clientes, así que no es posible un muestreo aleatorio simple ni estratificado: no hay una lista desde la cual sortear. La vía práctica es enviar el formulario a familiares, amigos y compañeros que cumplan los filtros y pedirles que lo reenvíen a otras personas que también califiquen. Por ser una muestra por conveniencia no se calcula margen de error ni se afirma que la muestra represente a todos los clientes; los resultados se leen como evidencia preliminar.
- **Tamaño y justificación:**
  - Meta de respuestas reales: entre 15 y 30 por equipo, es decir, de 3 a 6 por integrante (4 integrantes).
  - Para tener datos suficientes para los análisis del capítulo 4 y del laboratorio 7, el archivo se completa hasta 100 filas con valores simulados generados con código, marcados con `origen = simulada`. Simular no es inventar: se declara en el informe y la interpretación de sesgos se hace solo con las filas reales.
  - **Resultado de la aplicación (8 de noviembre de 2026):** el enlace se envió a aproximadamente 45 personas y se recibieron 30 respuestas, así que unas 15 no respondieron (tasa de respuesta aproximada: 66,7 %). De las 30 respuestas, 5 no cumplen la población (4 menores de 18 años y 1 persona que no reside en Quito), así que quedan 25 respuestas reales válidas, dentro de la meta de 15 a 30. El archivo se completó con 75 filas simuladas hasta llegar a 100. El número de invitados es aproximado, porque algunos contactos reenviaron el enlace.
- **Cómo se seleccionaron los participantes:**
  - Cada integrante envía el enlace del formulario por WhatsApp o correo a sus contactos que cumplen los filtros, repartiendo las invitaciones entre personas de distintas edades.
  - Las respuestas que no cumplen las preguntas filtro se descartan al procesar los datos con `scripts/muestreo.py`.
  - Se anota el total aproximado de personas a las que se envió el enlace (unas 45), sin nombres. Con ese número y las respuestas recibidas, `scripts/muestreo.py` calcula la tasa de respuesta y la no respuesta.
- **Equivalente en código (Python):** `scripts/muestreo.py`

```python
import pandas as pd

# Muestreo por conveniencia + referidos
# No hay marco de clientes (RetailAndina es ficticia), no se sortea a nadie.
# El archivo crudo de Google Forms queda en datos_crudos/ y NO se sube al repo

INVITADOS = 45  # aprox. personas a las que se les envio el enlace (sin nombres)

crudo = pd.read_csv("datos_crudos/formulario_respuestas.csv", dtype=str)
crudo.columns = ["marca_temporal", "edad_filtro", "genero", "reside_quito",
                 "frecuencia_compra", "rango_edad", "facilidad_busqueda",
                 "rapidez_pago", "tiempo_entrega", "satisfaccion_general",
                 "recomendaria", "prob_uso_programa", "beneficio_preferido"]

# preguntas filtro: 18+ y vive en Quito
menores = crudo["edad_filtro"] == "Menor a 18 años"
fuera_quito = crudo["reside_quito"] != "Si"
validas = crudo[~menores & ~fuera_quito].copy()

resp = len(crudo)
print("Respondieron:", resp)
print("No cumplen la poblacion:", (menores | fuera_quito).sum(),
      "(menores de 18:", menores.sum(), "| fuera de Quito:", fuera_quito.sum(), ")")
print("Cumplen la poblacion:", len(validas))
print("Invitados (aprox.):", INVITADOS, "| No respondieron:", INVITADOS - resp)
print("Tasa de respuesta (%):", round(resp / INVITADOS * 100, 1))
print("Meta 15-30 reales:", 15 <= len(validas) <= 30)

# anonimizacion: codigo R001..., solo la fecha, sin genero ni filtros
validas["fecha"] = validas["marca_temporal"].str[:10].str.replace("/", "-")
validas = validas.drop(columns=["marca_temporal", "edad_filtro", "genero", "reside_quito"])
validas.insert(0, "respuesta_id", [f"R{i:03d}" for i in range(1, len(validas) + 1)])
validas["origen"] = "real"
cols = ["respuesta_id", "fecha", "frecuencia_compra", "rango_edad", "facilidad_busqueda",
        "rapidez_pago", "tiempo_entrega", "satisfaccion_general", "recomendaria",
        "prob_uso_programa", "beneficio_preferido", "origen"]
reales = validas[cols]

# relleno simulado hasta 100 filas: cada columna se sortea de las respuestas reales
n_sim = 100 - len(reales)
sim = pd.DataFrame()
for i, col in enumerate(cols[2:-1]):
    sim[col] = reales[col].sample(n=n_sim, replace=True, random_state=42 + i).values
sim.insert(0, "respuesta_id", [f"S{i:03d}" for i in range(1, n_sim + 1)])
sim.insert(1, "fecha", "2026-11-18")
sim["origen"] = "simulada"

final = pd.concat([reales, sim], ignore_index=True)
final.to_csv("plantillas/encuesta_respuestas.csv", index=False)
print("Tamaño del archivo:", len(final), "(reales:", len(reales), "| simuladas:", n_sim, ")")
print(final[["respuesta_id", "fecha", "rango_edad", "frecuencia_compra", "origen"]].iloc[[0, 1, 2, 25, 26, 27]])
```

**Salida de la implementación:**

```
$ python scripts/muestreo.py
Respondieron: 30
No cumplen la poblacion: 5 (menores de 18: 4 | fuera de Quito: 1 )
Cumplen la poblacion: 25
Invitados (aprox.): 45 | No respondieron: 15
Tasa de respuesta (%): 66.7
Meta 15-30 reales: True
Tamaño del archivo: 100 (reales: 25 | simuladas: 75 )
   respuesta_id       fecha rango_edad frecuencia_compra    origen
0          R001  2026-11-08      18-29     4 - 6 compras      real
1          R002  2026-11-08      18-29          1 compra      real
2          R003  2026-11-08      18-29     2 - 3 compras      real
25         S001  2026-11-18      18-29     2 - 3 compras  simulada
26         S002  2026-11-18      18-29   7 o más compras  simulada
27         S003  2026-11-18      18-29          1 compra  simulada
```

Se usa muestreo por conveniencia más referidos porque RetailAndina es ficticia y no hay una base de clientes desde la cual sortear. El código aplica las preguntas filtro a las respuestas del formulario, calcula la no respuesta a partir del número aproximado de invitados, anonimiza los datos (código R001…, solo la fecha y sin género), completa el archivo con filas simuladas marcadas con `origen = simulada` (semilla `random_state=42 + i`). Como la muestra no es representativa, no se calcula margen de error y los resultados se presentan como evidencia preliminar.

## 4. Cuestionario (5–10 preguntas)

El formulario empieza con las preguntas filtro y con esta indicación: *En esta encuesta, RetailAndina es la página web donde más compras por internet.*

| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|
| 1 | Entre agosto y octubre de 2026, ¿cuántas compras hiciste en la app o en la página web de RetailAndina? | Categórica ordinal | `str` | 1 compra, 2 - 3 compras, 4 - 6 compras, 7 o más compras |
| 2 | ¿En qué rango de edad te encuentras? | Categórica ordinal | `str` | 18-29, 30-44, 45-59, 50 o más |
| 3 | ¿Qué tan fácil o difícil te resultó encontrar los productos que buscabas en línea? | Categórica ordinal | `int64` | 1 = Muy difícil, 2 = Difícil, 3 = Ni fácil ni difícil, 4 = Fácil, 5 = Muy fácil |
| 4 | En tu última compra en línea, ¿qué tan rápido o lento fue el proceso de pago? | Categórica ordinal | `int64` | 1 = Muy lento, 2 = Lento, 3 = Normal, 4 = Rápido, 5 = Muy rápido |
| 5 | ¿Cuánto tardó en llegar tu último pedido en línea, desde que lo pagaste? | Categórica ordinal | `str` | Mismo día, 1 a 2 días, 3 a 5 días, Más de 5 días, No aplica, retiré en tienda |
| 6 | En general, ¿qué tan satisfecho o insatisfecho estás con tu experiencia de compra en línea? | Categórica ordinal | `int64` | 1 = Muy insatisfecho, 2 = Insatisfecho, 3 = Neutral, 4 = Satisfecho, 5 = Muy satisfecho |
| 7 | ¿Recomendarías comprar en RetailAndina en línea a un familiar o amigo? | Categórica binaria | `str` | Si, No |
| 8 | Si RetailAndina incluyera un programa de fidelización en su aplicación, ¿qué tan probable es que lo uses? | Categórica ordinal | `int64` | 1 = Nada probable, 2 = Poco probable, 3 = Ni probable ni improbable, 4 = Probable, 5 = Muy probable |
| 9 | ¿Cuál de estos beneficios te motivaría más a usar un programa de fidelización? | Categórica nominal | `str` | Envíos gratis / Descuentos exclusivos / Puntos acumulables / Entregas más rápidas / Otro |

**Columnas del CSV:** `respuesta_id` (R001… reales, S001… simuladas), `fecha` (AAAA-MM-DD), `frecuencia_compra`, `rango_edad`, `facilidad_busqueda`, `rapidez_pago`, `tiempo_entrega`, `satisfaccion_general`, `recomendaria`, `prob_uso_programa`, `beneficio_preferido` y `origen`.

**Nota:** aunque las preguntas 3, 4, 6 y 8 lleguen como `int64`, se clasifican como ordinales: el dtype es solo una pista, no la clasificación. Si alguna quedara vacía, la columna pasaría a `float64`, por eso son obligatorias. El texto llega como `str` en pandas 3 (`object` en pandas 2), y el Si/No de la pregunta 7 también llega como texto, porque pandas solo convierte a `bool` los valores True/False. Las escalas tienen cinco puntos con ambos polos y un punto neutro, y nombran los dos extremos («fácil o difícil») para no inducir la respuesta; la pregunta 5 incluye «No aplica, retiré en tienda» para que las opciones sean exhaustivas.

**Nota sobre la pregunta 2:** las opciones «45-59» y «50 o más» se solapan, porque una persona de 52 años podría marcar cualquiera de las dos. Se mantienen tal como se aplicaron en el formulario y en el análisis se agrupan como «45 o más». En una nueva aplicación, la última opción debe ser «60 o más».

## 5. Análisis de sesgos

| Sesgo potencial | Mitigación |
|---|---|
| 1. **Sesgo de selección:** la muestra real sale de los contactos del equipo, así que tiende a tener muchos jóvenes de 18 a 29 años, estudiantes y personas cómodas con la tecnología, que probablemente encuentran la app más fácil que un cliente de 50 años. En los datos reales se confirma: 18 de las 25 respuestas válidas (72 %) son de personas de 18 a 29 años. | Declarar el método como conveniencia más referidos; repartir las invitaciones entre familiares de distintas edades; pedir referidos fuera del círculo cercano; revisar en la sección 7 la distribución de `rango_edad` y `frecuencia_compra`; presentar los resultados por grupo y como evidencia preliminar, sin margen de error. |
| 2. **Sesgo de respuesta:** al ser conocidos del equipo, los encuestados pueden dar calificaciones altas para ayudar o para no quedar mal. Además, como RetailAndina es ficticia, alguien podría responder pensando en una tienda distinta en cada pregunta. En los datos reales hay una señal: el 92 % (23 de 25) recomendaría comprar en línea, pero solo el 44 % calificó la búsqueda de productos como fácil o muy fácil. | Formulario anónimo (sin correo ni nombre); el encuestador no está presente al responder; preguntas neutras con punto medio; aviso de que no hay respuestas correctas y de que las críticas son igual de útiles; indicación al inicio y nombre de RetailAndina en las preguntas para que piensen siempre en el mismo supermercado. |

## 6. Confidencialidad (RA3)

- **Datos personales que se piden y por qué:** el rango de edad, el género y si la persona reside en Quito. La edad y la residencia sirven como filtro para comprobar que la persona pertenece a la población, y el rango de edad permite conocer la participación de los distintos grupos. El género se preguntó en el formulario, pero no es necesario para el objetivo, así que esa columna se elimina antes de compartir los datos. No se solicitan nombres, cédula, correo electrónico, teléfono ni dirección, porque no son necesarios y podrían permitir identificar a los participantes.
- **Plan de anonimización (qué se quita o codifica antes de compartir):** el formulario de Google se configura para no recopilar correos electrónicos. Al exportar las respuestas se elimina la marca temporal y se conserva solo la fecha (AAAA-MM-DD). Se eliminan por completo las respuestas de menores de 18 años y de personas que no residen en Quito, y se quitan las columnas de género y de las preguntas filtro. Cada fila recibe un código (R001…), sin nombres ni datos que identifiquen directamente a la persona. Las listas de contactos invitados quedan con cada integrante y no se suben al repositorio; solo se guarda el total aproximado de personas invitadas.
- El archivo CSV crudo con las respuestas no se sube al repositorio: queda en `datos_crudos/`, que el `.gitignore` excluye. Solo se publica `plantillas/encuesta_respuestas.csv` con los datos anonimizados y la columna `origen`. En el informe no se presentan cruces con menos de tres personas, para reducir el riesgo de identificar a alguien.

## 7. Verificación con herramientas (Python/R)

El script `scripts/verificacion_encuesta.py` revisa los dtypes de cada columna, cuenta los datos faltantes, muestra la distribución de `satisfaccion_general`, `recomendaria` y `rango_edad`, y separa las filas reales de las simuladas con la columna `origen`, para que la interpretación de sesgos use solo las respuestas reales.

```python
import pandas as pd

df = pd.read_csv("plantillas/encuesta_respuestas.csv")
print(df["origen"].value_counts(), "\n")

# tipos y datos faltantes de cada columna
resumen = pd.DataFrame({"dtype": df.dtypes.astype(str), "faltantes": df.isna().sum()})
print(resumen, "\n")

# la interpretacion de sesgos se hace solo con las filas reales
reales = df[df["origen"] == "real"]
print("Filas reales:", len(reales), "\n")

print("Distribucion de satisfaccion_general (reales):")
print(reales["satisfaccion_general"].value_counts().sort_index(), "\n")
print("Distribucion de recomendaria (reales):")
print(reales["recomendaria"].value_counts(), "\n")
# 45-59 y 50 o mas se solapan, se agrupan como 45 o mas
edad = reales["rango_edad"].replace({"45-59": "45 o más", "50 o más": "45 o más"})
print("Distribucion de rango_edad (reales):")
print(edad.value_counts(), "\n")

# regla de decision: >= 70 % satisfechos y >= 60 % usaria el programa
satisf = (reales["satisfaccion_general"] >= 4).mean() * 100
usaria = (reales["prob_uso_programa"] >= 4).mean() * 100
print("Satisfechos (4-5 en P6) %:", round(satisf, 1))
print("Usaria el programa (4-5 en P8) %:", round(usaria, 1))
print("Se cumple la regla de decision:", satisf >= 70 and usaria >= 60)
```

**Salida:**

```
$ python scripts/verificacion_encuesta.py
origen
simulada    75
real        25
Name: count, dtype: int64 

                      dtype  faltantes
respuesta_id            str          0
fecha                   str          0
frecuencia_compra       str          0
rango_edad              str          0
facilidad_busqueda    int64          0
rapidez_pago          int64          0
tiempo_entrega          str          0
satisfaccion_general  int64          0
recomendaria            str          0
prob_uso_programa     int64          0
beneficio_preferido     str          0
origen                  str          0 

Filas reales: 25 

Distribucion de satisfaccion_general (reales):
satisfaccion_general
2     2
3     6
4    14
5     3
Name: count, dtype: int64 

Distribucion de recomendaria (reales):
recomendaria
Si    23
No     2
Name: count, dtype: int64 

Distribucion de rango_edad (reales):
rango_edad
18-29       18
30-44        4
45 o más     3
Name: count, dtype: int64 

Satisfechos (4-5 en P6) %: 68.0
Usaria el programa (4-5 en P8) %: 60.0
Se cumple la regla de decision: False
```

- **¿Coinciden los tipos con la predicción de la sección 4?** Sí. Las preguntas 3, 4, 6 y 8 llegan como `int64` y el resto como `str`, tal como se anotó en la tabla del cuestionario. Aunque lleguen como `int64`, siguen siendo variables ordinales.
- **¿Cuántos datos faltantes hay por columna?** Ninguno: todas las columnas tienen 0 faltantes. Las tres celdas vacías del formulario eran de personas que no cumplían la población y se descartaron con los filtros.
- **Resultado frente a la regla de decisión (solo las 25 respuestas reales):** el 68 % está satisfecho (4 o 5 en P6) y el 60 % probablemente usaría el programa (4 o 5 en P8). Se alcanza la meta de uso del programa, pero no la de satisfacción (70 %), así que, según la regla, todavía no se recomienda lanzar el programa primero en la aplicación: antes conviene mejorar la experiencia de compra en línea. La diferencia es de una sola persona (18 de 25 sería 72 %) y la muestra es por conveniencia, por lo que el resultado es evidencia preliminar.
- **Sesgo de no respuesta:** lo delataría una tasa de respuesta baja o que quienes contestan sean casi todos clientes contentos, con muy pocas calificaciones de 1 y 2. La tasa de respuesta fue de aproximadamente 66,7 % (30 de unas 45 personas invitadas), así que una de cada tres no contestó. Además, en los datos reales solo 2 de 25 personas calificaron la satisfacción con 2 y ninguna con 1, lo que es compatible con que los clientes insatisfechos hayan respondido menos.
- **Sesgo de respuesta:** lo delataría una distribución cargada hacia las respuestas positivas que no coincide con la evaluación de cada etapa. El 92 % (23 de 25) recomendaría comprar en línea, pero solo el 44 % calificó la búsqueda de productos como fácil o muy fácil y el 40 % calificó el pago como rápido o muy rápido. Esa diferencia sugiere que la pregunta de recomendación pudo contestarse por cortesía con el equipo.
- **Sesgo de selección:** la distribución de `rango_edad` muestra 18 de 25 personas (72 %) entre 18 y 29 años y solo 3 de 45 años o más, lo que confirma que la muestra viene sobre todo del círculo joven del equipo.
