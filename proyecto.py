#Librerías
import pandas as pd
import numpy as np
from scipy import stats
from functools import reduce
import matplotlib.pyplot as plt

#Leer datos
datos = pd.read_csv("datos/estudiantes_merged.csv",sep=",")
muestra = pd.read_csv("datos/muestra.csv",sep=",")

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


######## HISTOGRAMAS CALIFICACIONES POBLACIÓN
p_calis = plt.figure(1)
plt.subplot(2, 2, 1)
# plt.tight_layout()
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.hist((datos["G1"]*0.5),bins=range(11)) # *0.5 porque las calis están sobre 20
#plt.text(2, 100, r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.title("Primer parcial")
#
plt.subplot(2, 2, 2)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G2"]*0.5,bins=range(11))
plt.grid(True)
plt.title("Segundo parcial")
#
plt.subplot(2, 2, 3)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(datos["G3"]*0.5,bins=range(11))
plt.grid(True)
plt.title("Tercer parcial")
#
plt.subplot(2, 2, 4)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
#plt.tight_layout()
plt.hist(((datos["G1"]*0.5)+(datos["G2"]*0.5)+(datos["G3"]*0.5))/3,facecolor='g',bins=range(11))
plt.grid(True)
plt.title("Calificación final")
#
print("Media: ",(reduce(lambda x,y: x+y,((datos["G1"]*0.5)+(datos["G2"]*0.5)+(datos["G3"]*0.5))/3))/len(datos))
p_calis.show()


######## HISTOGRAMAS CALIFICACIONES MUESTRA
m_calis = plt.figure(4)
plt.subplot(2, 2, 1)
plt.tight_layout()
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.hist((muestra["G1"]*0.5),bins=range(11)) # *0.5 porque las calis están sobre 20
#plt.text(2, 100, r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.title("Primer parcial M")
#
plt.subplot(2, 2, 2)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(muestra["G2"]*0.5,bins=range(11))
plt.grid(True)
plt.title("Segundo parcial M")
#
plt.subplot(2, 2, 3)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist(muestra["G3"]*0.5,bins=range(11))
plt.grid(True)
plt.title("Tercer parcial M")
#
plt.subplot(2, 2, 4)
plt.xlabel('Calificación')
plt.ylabel('# de alumnos')
plt.tight_layout()
res=plt.hist(((muestra["G1"]*0.5)+(muestra["G2"]*0.5)+(muestra["G3"]*0.5))/3,facecolor='g',bins=range(11))
plt.grid(True)
plt.title("Calificación final M")

#np.histogram()
#
print("Tabla de Calificación final (Muestra)")
print("Media: ",(reduce(lambda x,y: x+y,((muestra["G1"]*0.5)+(muestra["G2"]*0.5)+(muestra["G3"]*0.5))/3))/len(muestra))
x=0
suma=0
for i in res[0]:
	suma+=i
	print("["+str(res[1][x])+","+str(res[1][x+1])+"] | "+str(i)+" | "+str(suma)+" | "+str())
	x+=1
m_calis.show()


######## GRÁFICAS CONSUMO DE ALCOHOL POBLACIÓN
p_alcohol_calis = plt.figure(2)
plt.subplot(2, 1, 1)
plt.xlabel('Nivel de consumo')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist((datos['Walc']+datos['Dalc']),facecolor='pink',bins=range(11))
plt.grid(True)
plt.title("Consumo de alcohol (Población)")

plt.subplot(2, 1, 2)
plt.xlabel('Calificación')
plt.ylabel('Nivel de alcoholismo')
plt.scatter(((datos["G1"]*0.5)+(datos["G2"]*0.5)+(datos["G3"]*0.5))/3,(datos['Walc']+datos['Dalc']),facecolor='r')
#plt.scatter((datos["G1"]*0.5),(datos['Walc']+datos['Dalc']))
plt.title("Dispersión: Consumo de alcohol - Calificaciones")

p_alcohol_calis.show()


######## GRÁFICAS CONSUMO DE ALCOHOL MUESTRA
m_alcohol_calis = plt.figure(3)
plt.subplot(2, 1, 1)
plt.xlabel('Nivel de consumo')
plt.ylabel('# de alumnos')
plt.tight_layout()
plt.hist((muestra['Walc']+muestra['Dalc']),facecolor='pink',bins=range(11))
# plt.scatter((muestra['Walc']+muestra['Dalc']),facecolor='black')
plt.grid(True)
plt.title("Consumo de alcohol (Muestra)")

plt.subplot(2, 1, 2)
plt.xlabel('Calificación')
plt.ylabel('Nivel de alcoholismo')
plt.scatter(((muestra["G1"]*0.5)+(muestra["G2"]*0.5)+(muestra["G3"]*0.5))/3,(muestra['Walc']+muestra['Dalc']),facecolor='r')
#plt.scatter((datos["G1"]*0.5),(datos['Walc']+datos['Dalc']))
plt.title("Dispersión: Consumo de alcohol - Calificaciones")

m_alcohol_calis.show()

input()