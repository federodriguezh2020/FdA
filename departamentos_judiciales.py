import sys # Importamos la libreria.

# Importamos el tipo DependenciaJudicial. 
from dependencia_judicial import DependenciaJudicial

# Definimos una funcion que cargue las dependencias judiciales del archivo que se le pasa como argumento. 
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

# Cargo el archivo que le paso despues de python en la consola y lo guardo en dependencias:
dependencias = cargar_dependencias(sys.argv[1])

# Despues del archivo le voy a pasar otro arhicvo que sera el que utilice para escribir, lo guardo en escribir.
escribir = open(sys.argv[2], "w", encoding="latin-1")

# Ordeno las dependencias:
dependencias = sorted(dependencias)

# Creo una lista vacia.
departamentos = []

# Función para eliminar los duplicados.
def lista(x):
  return list(dict.fromkeys(x))

# Itero en las depencias y agrego a la lista cada departamento judicial.
for departamento in dependencias:
    departamentos.append(str(departamento.departamento_judicial()))
    
# Elimino los duplicados.
departamentos = lista(departamentos)

# Itero en los departmentos y escribo cada uno de ellos en el archivo que me dice el usuario, seguido de :.
# Luego itero en las dependencias y escribo cada una de las que estan asociadas a ese departamento.
for departamento in departamentos:
    escribir.write(departamento + ": ")
    for dependencia in dependencias:
        if dependencia.departamento_judicial() == departamento:
            escribir.write(str(dependencia))
    escribir.write("\n")
    
# Cierro el archivo.   
escribir.close()
