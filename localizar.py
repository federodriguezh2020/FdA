import sys

from dependencia_judicial import DependenciaJudicial

def cargar_dependencias(archivo):
    dependencias = set()
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
            latitud = float(atributos[8])
            longitud = float(atributos[9])
            dependencia = DependenciaJudicial(numero, fuero, nombre, tipo_de_ente, direccion, localidad, departamento_judicial, telefono, latitud, longitud)
            dependencias.add(dependencia)
    archivo.close()
    return dependencias

dependencias = cargar_dependencias(sys.argv[1])

latitud = sys.argv[2]
longitud = sys.argv[3]

distancias = []

for dependencia in dependencias:
    if dependencia.latitud() != 0 and dependencia.longitud() !=0:
        distancias.append(dependencia.distancia(latitud, longitud))
        distancias.sort()

print(distancias[0])
