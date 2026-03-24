import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# SQL
conexion = sqlite3.connect("datos_mision.db")
consulta = "SELECT * FROM tabla;"
df = pd.read_sql_query(consulta, conexion)
conexion.close()

# Mascara para gigantes gaseosos esponjosos
df["pl_dens"] = (df["pl_bmasse"] / (4/3 * np.pi)) / (df["pl_rade"] ** 3)
mascara_gigantes = (df["pl_bmasse"] > 95.34) & (df["pl_dens"] < 0.3)


# Curvas teóricas (Seager et al. 2007)
def curva_seager(M, m1, r1, k1=-0.20945, k2=0.0804, k3=0.394):

    Ms = M / m1

    return r1 * 10**(k1 + (1/3)*np.log10(Ms) - k2*(Ms**k3))


rango_masa = np.logspace(-1.2, 4, 3000)  # 0.062 a 10000 masas terrestres

R_cero = curva_seager(rango_masa, m1=1, r1=0.01) # curva cero
R_hierro = curva_seager(rango_masa, m1=4.34, r1=2.23)
R_tierra = curva_seager(rango_masa, m1=6.41, r1=2.84)
R_silicatos = curva_seager(rango_masa, m1=7.38, r1=3.58)
R_3capas = curva_seager(rango_masa, m1=6.41, r1=3.63)
R_agua = curva_seager(rango_masa, m1=8.16, r1=4.73)


# Función para colorear a los planetas según su posición relativa a las curvas teóricas
def mascara_curvas(R_curva_arriba, R_curva_abajo):
    interp_arriba = interp1d(np.log10(rango_masa), np.log10(R_curva_arriba), kind="linear", fill_value="extrapolate")

    interp_abajo = interp1d(np.log10(rango_masa), np.log10(R_curva_abajo), kind="linear", fill_value="extrapolate")

    M_planetas = df["pl_bmasse"].values

    R_arriba_planetas = 10**interp_arriba(np.log10(M_planetas))
    R_abajo_planetas = 10**interp_abajo(np.log10(M_planetas))

    R_obs = df["pl_rade"].values

    mascara = (R_obs <= R_arriba_planetas) & (R_obs >= R_abajo_planetas)

    return mascara

mascara_hierro = mascara_curvas(R_hierro, R_cero)
mascara_tierra = mascara_curvas(R_tierra, R_hierro)
mascara_silicatos = mascara_curvas(R_silicatos, R_tierra)
mascara_3capas = mascara_curvas(R_3capas, R_silicatos)
mascara_agua = mascara_curvas(R_agua, R_3capas)

mascara_otros = ~(mascara_curvas(R_agua, R_cero) | mascara_gigantes) # Mascara para planetas que no encajan en ninguna categoría

# Graficamos
plt.figure(figsize=(10, 7))

# Rocosos de hierro muy probables
plt.scatter(df.loc[mascara_hierro, "pl_bmasse"], df.loc[mascara_hierro,"pl_rade"], alpha=0.7, color="#592802", s=40, label="Rocosos densos")

# Rocosos similares a la Tierra probables
plt.scatter(df.loc[mascara_tierra, "pl_bmasse"], df.loc[mascara_tierra, "pl_rade"], alpha=0.7, color="#9A5006", s=40, label="Rocosos probables")

# Rocosos posibles de silicatos o de 3 capas
plt.scatter(df.loc[mascara_silicatos | mascara_3capas, "pl_bmasse"], df.loc[mascara_silicatos | mascara_3capas, "pl_rade"], alpha=0.7, color="#F28303", s=40, label="Rocosos poco probables")

# Rocosos posibles de agua
plt.scatter(df.loc[mascara_agua, "pl_bmasse"], df.loc[mascara_agua, "pl_rade"], alpha=0.7, color="#005EFF", s=40, label="Rocosos hipoteticos de hielo")

# Gigantes gaseosos
plt.scatter(df.loc[mascara_gigantes, "pl_bmasse"], df.loc[mascara_gigantes, "pl_rade"], alpha=0.7, color="green", s=40, label=r"Gigantes gaseosos esponjosos")


# Otros planetas
plt.scatter(df.loc[mascara_otros, "pl_bmasse"], df.loc[mascara_otros, "pl_rade"], alpha=0.7, color="#353E4A", s=40, label="Otros planetas")


plt.xscale("log")
plt.yscale("log")

plt.xlabel("Masa del planeta [$M_\\oplus$]")
plt.ylabel("Radio del planeta [$R_\\oplus$]")
plt.title("Diagrama masa-radio de exoplanetas")


#Curvas teóricas masa-radio
plt.plot(rango_masa, R_hierro, color="#592802", label="Planeta de 100% Fe", alpha=0.7)
plt.plot(rango_masa, R_tierra, color="#9A5006", label="Planeta de 67% MgSiO3 + 33% Fe", alpha=0.7)
plt.plot(rango_masa, R_silicatos, color="#F28303", label="Planeta de 100% MgSiO3", alpha=0.7)
plt.plot(rango_masa, R_3capas, color="#FFCF00", label="Planeta de Fe + MgSiO3 + H2O", alpha=0.7)
plt.plot(rango_masa, R_agua, color="#005EFF", label="Planeta de 100% H2O", alpha=0.7)

#Grafica de curva con densidad constante de 0.3 g/cm^3
R_constante = (rango_masa / (4/3 * np.pi * 0.3)) ** (1/3)
masa_minima = 95.34 # Masa mínima para gigantes
mascara_masa = rango_masa >= masa_minima # Solo graficar el rango de masa de gigantes
plt.plot(rango_masa[mascara_masa], R_constante[mascara_masa], color="red", linestyle="--", label=r"Densidad constante 0.3 $g/cm^3$")

#Grafica de recta vertical que va desde el punto con la masa minima y el radio minimo
radio_minimo = (masa_minima/(4/3 * np.pi * 0.3))**(1/3)
plt.plot([masa_minima, masa_minima], [radio_minimo, 100], color="purple", linestyle="--", label="Limite de masa para planetas gigantes")

plt.grid(True, which="both", linestyle=":", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig("resultado.png", dpi=300, bbox_inches="tight")
plt.show()
