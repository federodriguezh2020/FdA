# TP1

# Alumnos: Julieta De Antonio, Maria Gomez Alzaga y Federico Rodriguez

# El numero primo que se encuentra el i posicion.
# Para saber si un numero es primo, debo ver la
# cantidad de divisores que tiene.
# Funciones auxiliares:
def numerosDivisores(n):
    i = 1
    divisores = []
    while (i <= n):
        if n % i == 0:
            divisores += [i]
        i= i + 1
    return divisores
    
numerosDivisores(10)

def divisores(n):
    i = 1
    divisores = []
    while (i <= n):
        if n % i == 0:
            divisores += [i]
        i= i + 1
    if divisores != 0:
        return divisores
    
divisores(7)

def divisoresPrimos(n):
    i = 2
    divisoresPrimos = []
    while i <= n:
        if esPrimo(i) == True and # tengo que hacer una funcion esDivisor(i) == True:
            divisoresPrimos += [i]
        i += 1
    return divisoresPrimos
       
divisoresPrimos(7)

# Funciones
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
        return True
    else:
        return False

esPrimo(15)

# Calculo auxiliar
def numerosPrimos(n):
    i = 2
    numerosPrimos = []
    while (i < n):
        if esPrimo(i) == True :
            numerosPrimos += [i]
        i= i + 1
    return numerosPrimos

numerosPrimos(13)

# Funciones
def iesimoPrimo(i):
    n = 1
    while len(numerosPrimos(n)) < i + 1:
        n += 1
    return numerosPrimos(n)[i - 1]    

iesimoPrimo(1200)

def cantidadPrimosMenoresOIguales(n):
    return len(numerosPrimos(n + 1))
        
cantidadPrimosMenoresOIguales(7)

def cantidadDivisoresPrimos(n):
    return len(divisoresPrimos(n))
 
cantidadDivisoresPrimos(6)

def sumaPrimerosPrimos(n): # REVISARRR
    i = 2
    suma = 0
    while i <= n:
        suma += iesimoPrimo(i)
        i =+ 1
    return suma

sumaPrimerosPrimos(5)
iesimoPrimo(5) 
    