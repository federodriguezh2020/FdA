# TP1

# Alumnos: Julieta De Antonio, Maria Gomez Alzaga y Federico Rodriguez

import sys 

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

# Funciones auxiliares:
##
def numerosPrimos(n):
    i = 2
    numerosPrimos = []
    while (i < n):
        if esPrimo(i) == "sí" :
            numerosPrimos += [i]
        i += 1
    return numerosPrimos

##
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

##
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
def iesimoNumeroPrimo(i):
    n = 1
    while len(numerosPrimos(n)) < i + 1:
        n += 1
    return numerosPrimos(n)[i - 1] 

# Funciones:
# 2
def iesimoPrimo(i):
    n = 1
    while len(numerosPrimos(n)) < i + 1:
        n += 1
    return numerosPrimos(n)[i - 1]     

# 3
def cantidadPrimosMenoresOIguales(n):
    return len(numerosPrimos(n + 1))
        
# 4
def cantidadDivisoresPrimos(n):
    return len(divisoresPrimos(n))
 
# 5
def iesimoDivisorPrimo(n, i):
    if len(divisoresPrimos(n)) < i:
        return (str(n) + " no tiene " + str(i) + " divisores primos")
    else:
        return divisoresPrimos(n)[i - 1]
 
# 6
def sumaPrimerosPrimos(n):
    i = 1
    suma = 0
    while i <= n:
        suma += + iesimoNumeroPrimo(i)
        i += 1
    return suma

   
# Llamado a funciones        
funcion = sys.argv[1]
parametro1 = int(sys.argv[2])
if funcion == "esPrimo":
    print(esPrimo(parametro1)) 
elif funcion == "iesimoPrimo":
    print(iesimoPrimo(parametro1))
elif funcion == "cantidadPrimosMenoresOIguales":
    print(cantidadPrimosMenoresOIguales(parametro1))
elif funcion == "cantidadDivisoresPrimos":
    print(cantidadDivisoresPrimos(parametro1))
elif funcion == "sumaPrimerosPrimos":
    print(sumaPrimerosPrimos(parametro1))
elif funcion == "iesimoDivisorPrimo":
    parametro2 = int(sys.argv[3])
    print(iesimoDivisorPrimo(parametro1, parametro2))
