import sys

from dependencia_judicial import DependenciaJudicial

def cargar_dependencias(archivo):
    dependencias = []
    archivo = open(archivo, encoding='latin-1')
    for linea in archivo:
        atributos = linea.split(";")
        numero = atributos[0]
        if numero != "Número":
            fuero = atributos[1]
            nombre = atributos[2]
            tipo_de_ente = atributos[3]
            direccion = atributos[4]
            localidad = atributos[5]
            departamento_judicial = atributos[6]
            telefono = atributos[7]
            latitud = float(atributos[8].replace(',','.'))
            longitud = float(atributos[9].replace(',','.'))
            dependencia = DependenciaJudicial(linea)
            dependencias.append(dependencia)
    archivo.close()
    return dependencias

dependencias = cargar_dependencias(sys.argv[1])

latitud = sys.argv[2]
longitud = sys.argv[3]

distancias = dict()
min_distancia = []

for dependencia in dependencias:
    distancias[dependencia.distancia(latitud, longitud)] = dependencia
    min_distancia.append(dependencia.distancia(latitud,longitud))

min_distancia.sort()
print(distancias[min_distancia[0]])