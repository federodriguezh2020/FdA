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
            dependencia = DependenciaJudicial(numero, fuero, nombre, tipo_de_ente, direccion, localidad, departamento_judicial, telefono, latitud, longitud)
            dependencias.append(dependencia)
    archivo.close()
    return dependencias

dependencias = cargar_dependencias(sys.argv[1])

latitud = sys.argv[2]
longitud = sys.argv[3]

distancias = dict()

for dependencia in dependencias:
    distancias[dependencia.distancia(latitud, longitud)] = dependencia

for i in sorted(distancias.keys()) : 
    print(distancias[i], end ="\n")
    break
