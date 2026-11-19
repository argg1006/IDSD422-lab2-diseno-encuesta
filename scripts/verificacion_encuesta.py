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
