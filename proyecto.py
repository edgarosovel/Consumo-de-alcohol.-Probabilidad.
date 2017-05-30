#Librerías
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Leer datos
datos = pd.read_csv("datos/estudiantes_merged.csv",sep=",")

#por = pd.read_csv("datos/student-por.csv",sep=",")
#datos = [mat,por]
#datos = pd.concat(datos)
#Eliminamos los datos duplicados
#datos=datos.drop_duplicates(["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])

#Crear una muestra aleatoria de 30 alumnos
#muestra=datos.sample(30)
#muestra.to_csv("datos/muestra.csv")

# from sys import argv
# target = open('datos/muestra.csv', 'w')
# target.write(datos[0])
# for i in ran:
# 	writer.writerow(datos[i])
# target.close()



calis = plt.figure(1)
plt.subplot(2, 2, 1)
plt.tight_layout()
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.hist((datos["G1"]*0.5),facecolor='g') # *0.5 porque las calis están sobre 20
plt.text(2, 100, r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.title("Primer parcial")
#
plt.subplot(2, 2, 2)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G2"]*0.5)
plt.grid(True)
plt.title("Segundo parcial")
#
plt.subplot(2, 2, 3)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G3"]*0.5)
plt.grid(True)
plt.title("Tercer parcial")
#
plt.subplot(2, 2, 4)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(((datos["G1"]*0.5)+(datos["G2"]*0.5)+(datos["G3"]*0.5))/3)
plt.grid(True)
plt.title("Calificación final")
#
calis.show()

alcohol_calis = plt.figure(2)

plt.subplot(2, 1, 1)
plt.xlabel('Nivel de consumo')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["Walc"])
plt.grid(True)
plt.title("Consumo de alcohol (Fin de semana)")

plt.subplot(2, 1, 2)
plt.xlabel('Calificación')
plt.ylabel('Nivel de alcoholismo')
plt.scatter(((datos["G1"]*0.5)+(datos["G2"]*0.5)+(datos["G3"]*0.5))/3,(datos['Walc']+datos['Dalc']))
#plt.scatter((datos["G1"]*0.5),(datos['Walc']+datos['Dalc']))
plt.title("Relación: Consumo de alcohol - Calificaciones")

alcohol_calis.show()

input()