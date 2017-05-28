#Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leer datos
mat = pd.read_csv("datos/student-mat.csv",sep=",")
por = pd.read_csv("datos/student-por.csv",sep=",")
datos = [mat,por]
datos = pd.concat(datos)

#Eliminamos los datos duplicados
datos=datos.drop_duplicates(["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])

graficas=["G1","G2","G3","Walc"] #nombres de los índices asociativos


plt.subplot(2, 2, 1)
plt.tight_layout()
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.hist((datos["G1"]*0.5),facecolor='g') # *0.5 porque las calis están sobre 20
plt.text(2, 100, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.title("Primer parcial")

plt.subplot(2, 2, 2)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G2"]*0.5)
plt.grid(True)
plt.title("Segundo parcial")

plt.subplot(2, 2, 3)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G3"]*0.5)
plt.grid(True)
plt.title("Tercer parcial")

plt.subplot(2, 2, 4)
plt.xlabel('Nivel de consumo')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["Walc"])
plt.grid(True)
plt.title("Consumo de alcohol (Fin de semana)")

plt.show()

