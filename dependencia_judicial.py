class DependenciaJudicial:
    
    def __init__(self, linea):
        v = linea.split(";")
        self._numero = v[0]
        self._fuero = v[1]
        self._nombre = v[2]
        self._tipo_de_ente = v[3]
        self._direccion = v[4]
        self._localidad = v[5]
        self._departamento_judicial = v[6]
        self._telefono = v[7]
        self._latitud = float(v[8].replace(',','.'))
        self._longitud = float(v[9].replace(',','.'))
    
    def fuero(self):
        return self._fuero
    
    def nombre(self):
        return self._nombre
    
    def tipo_de_ente(self):
        return self._tipo_de_ente
    
    def direccion(self):
        return self._direccion
    
    def localidad(self):
        return self._localidad
    
    def departamento_judicial(self):
        return self._departamento_judicial
    
    def telefono(self):
        return self._telefono
    
    def latitud(self):
        return self._latitud
    
    def longitud(self):
        return self._longitud
    
    def distancia(self, lat, lng):
        distancia = (((float(self._latitud) - float(lat))**2) + ((float(self._longitud) - float(lng))**2))**0.5
        return float(distancia)
    
    def __hash__(self):
        return hash((self._fuero, self._nombre, self._tipo_de_ente, self._direccion, self._localidad, self._departamento_judicial, self._latitud, self._longitud))
    
    def __eq__ (self, other):
        return self._fuero == other._fuero and self._nombre == other._nombre and self._departamento_judicial == other._departamento_judicial
    
    def __lt__(self, other):
        return self._departamento_judicial < other._departamento_judicial or \
               self._departamento_judicial == other._departamento_judicial and self._fuero < other._fuero or \
               self._departamento_judicial == other._departamento_judicial and self._fuero == other._fuero and self._nombre < other._nombre    
    
    def __repr__(self):
        return "{" + self._fuero + ";" + self._nombre + ";" + self._direccion + ";" + self._localidad + "}"