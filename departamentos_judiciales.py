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
escribir = open(sys.argv[2], "w", encoding="latin-1")

dependencias = sorted(dependencias)

departamentos = []

def my_function(x):
  return list(dict.fromkeys(x))

for departamento in dependencias:
    departamentos.append(str(departamento.departamento_judicial()))
departamentos = my_function(departamentos)

for departamento in departamentos:
    escribir.write(departamento + ": ")
    for dependencia in dependencias:
        if dependencia.departamento_judicial() == departamento:
            escribir.write(str(dependencia))
    escribir.write("\n")
    escribir.write("\n")
escribir.close()
