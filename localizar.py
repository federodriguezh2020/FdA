import sys

from dependencia_judicial import DependenciaJudicial

nombre_archivo = sys.argv[1]

def cargar_dependencias(archivo):
    dependencias = []
    archivo = open(archivo)
    for linea in archivo:
        atributos = linea.split(",")
        fuero = atributos[1]
        nombre = atributos[2]
        tipo_de_ente = atributos[3]
        direccion = atributos[4]
        localidad = atributos[5]
        departamento_judicial = atributos[6]
        telefono = atributos[7]
        latitud = atributos[8]
        longitud = atributos[9]
        dependencia = DependenciaJudicial(fuero, nombre, tipo_de_ente, direccion, localidad, departamento_judicial, telefono, latitud, longitud)
        dependencias.append(dependencia)
    archivo.close()
    return dependencias

dependencias = cargar_dependencias(nombre_archivo)


latitud = sys.argv[2]
longitud = sys.argv[3]

distancias = []

for dependencia in dependencias:
    if dependencia.latitud() != 0 and dependencia.longitud() !=0 :
        distancias.add[dependencia.distancias(latitud, longitud)]

distancias.sort()
print(distancias[0])
