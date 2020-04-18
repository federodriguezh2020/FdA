# TP1

import sys

nombre_comando = sys.argv[1]

# Alumnos: Julieta De Antonio, Maria Gomez Alzaga y Federico Rodriguez

# El numero primo que se encuentra el i posicion.
# Para saber si un numero es primo, debo ver la
# cantidad de divisores que tiene.
# Funciones auxiliares:

# Funciones:
#1
def esPrimo(n):
    i = 2 # Empezamos en dos porque todos los numeros se pueden dividir por 1.
    esPrimo = 0
    if n == 0 or n == 1:
        esPrimo = 1
    else:    
        while i < n:
            if n % i == 0:
                esPrimo = 1
            i = i + 1
    if esPrimo == 0:
        return "sí"
    else:
        return "no"
#2    
## Función auxiliar:
def numerosPrimos(n):
    i = 2
    numerosPrimos = []
    while (i < n):
        if esPrimo(i) == "sí" :
            numerosPrimos += [i]
        i += 1
    return numerosPrimos
##
def iesimoPrimo(i):
    n = 1
    while len(numerosPrimos(n)) < i + 1:
        n += 1
    return numerosPrimos(n)[i - 1]     

#3  
def cantidadPrimosMenoresOIguales(n):
    return len(numerosPrimos(n + 1))
        
#4
## Funciones auxiliares:    
def esDivisor(i, n):
    esDivisor = 0
    if i <= n:
        if i <= 0:
            esDivisor = 1
        else:    
            if n % i != 0:
                esDivisor = 1
        if esDivisor == 0:
            return True
        else:
            return False
        
def divisoresPrimos(n):
    i = 1
    divisoresPrimos = []
    while i <= n:
        if esPrimo(i) == "sí": 
            if esDivisor(i,n) == True:
                divisoresPrimos += [i]
        i += 1
    return divisoresPrimos
##
        
def cantidadDivisoresPrimos(n):
    return len(divisoresPrimos(n))
#5

def iesimoDivisorPrimo(n, i):
    if len(divisoresPrimos(n)) < i:
        return (str(n) + " no tiene " + str(i) + " divisores primos")
    else:
        return divisoresPrimos(n)[i - 1]
#6
def sumaPrimerosPrimos(n):
    i = 1
    suma = 0
    while i <= n:
        suma += + iesimoPrimo(i)
        i += 1
    return suma
  
# Llamado a funciones
if nombre_comando == "esPrimo":
    n = int(sys.argv[2])
    print(esPrimo(n))

if nombre_comando == "iesimoPrimo":
    i = int(sys.argv[2])
    print(iesimoPrimo(i))

if nombre_comando == "cantidadPrimosMenoresOIguales":
    n = int(sys.argv[2])
    print(cantidadPrimosMenoresOIguales(n))

if nombre_comando == "cantidadDivisoresPrimos":
    n = int(sys.argv[2])
    print(cantidadDivisoresPrimos(n))

if nombre_comando == "iesimoDivisorPrimo":
    n = int(sys.argv[2])
    i = int(sys.argv[3])
    print(iesimoDivisorPrimo(n, i))

if nombre_comando == "sumaPrimerosPrimos":
    n = int(sys.argv[2])
    print(sumaPrimerosPrimos(n))
