# TP1

# Alumnos: Julieta De Antonio, Maria Gomez Alzaga y Federico Rodriguez

# El numero primo que se encuentra el i posicion.
# Para saber si un numero es primo, debo ver la
# cantidad de divisores que tiene.
import sys
n=int(sys.argv[1])
i= int(sys.argv[2])


#Funciones
#1 Determinar si un número esPrimo
#versión Juli
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
print(n, esPrimo(n), "es primo")

#versión Mery
#Función auxiliar:
def n_divisores(n):
    i=1
    ndiv=[]
    while i<=n:
        if n%i==0:
            ndiv.append(i)
        i+=1
    return len(ndiv)

#Función
def esPrimo2(n):
    if n_divisores(n) == 2:
        return "sí"
    else:
        return "no"
print(n, esPrimo2(n), "es primo")

#2 Indicado i, devuelvo el i-ésimo número primo

# Función auxiliar:
def numerosPrimos(n):
    i = 2
    numerosPrimos = []
    while (i < n):
        if esPrimo(i):
            numerosPrimos += [i]
        i= i + 1
    return numerosPrimos

#Función
def iesimoPrimo(i):
    n = 1
    while len(numerosPrimos(n)) < i + 1:
        n += 1
    return numerosPrimos(n)[i - 1]    

print(iesimoPrimo(i))

#3 Cantidad Primos Menores o Iguales a n

#Función
def cantidadPrimosMenoresOIguales(n):
    return len(numerosPrimos(n + 1))
        
print(cantidadPrimosMenoresOIguales(n))

#4 Cantidad de divisores primos

#Función auxiliar
def divisoresPrimos(n):
    i = 2
    divisoresPrimos = []
    while i <= n:
        if esPrimo(i):
            divisoresPrimos += [i]
        i += 1
    return divisoresPrimos

#Función
def cantidadDivisoresPrimos(n):
    return len(divisoresPrimos(n))
 
print(cantidadDivisoresPrimos(n))

#5 Dados i y n, devuelve el i-ésimo número primo de n

#6 Suma primeros n primos
def sumaPrimerosPrimos(n):
    i = 2
    suma = 0
    while i <= n:
        suma += iesimoPrimo(i)
        i =+ 1
    return suma

print(sumaPrimerosPrimos(n))


def numerosDivisores(n):
    i = 1
    divisores = []
    while (i <= n):
        if n % i == 0:
            divisores += [i]
        i= i + 1
    return divisores
    
def divisores(n):
    i = 1
    divisores = []
    while (i <= n):
        if n % i == 0:
            divisores += [i]
        i= i + 1
    if divisores != 0:
        return divisores
