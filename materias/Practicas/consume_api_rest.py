import requests


class Empresa(object):
    def __init__(self, descripcion, idUsuario, nombreEmpresa, paginaWeb) -> None:
        self.descripcion = descripcion
        self.idUsuario = idUsuario
        self.nombreEmpresa = nombreEmpresa
        self.paginaWeb = paginaWeb
        pass

class Vacante(object):
    def __init__(self, area, descripcionPuesto, fechaPublicacion, nombreEmpresa, puesto, url) -> None:
        self.area = area
        self.descripcionPuesto = descripcionPuesto
        self.fechaPublicacion = fechaPublicacion
        self.nombreEmpresa = nombreEmpresa
        self.puesto = puesto
        self.url = url
        pass
    def __str__(self) -> str:
        return "Puesto {}, Área {} y Descripción {}".format(self.puesto, self.area, self.descripcionPuesto)

class Pais(object):
    def __init__(self, id, nombre) -> None:
        self.idPais = id
        self.nombre = nombre
        pass

class Usuario(object):
    def __init__(self, correo = None, idPais = 0, nombre = None, nombrePais = None) -> None:
        self.correo = correo
        self.idPais = idPais
        self.nombre = nombre
        self.nombrePais = nombrePais
        pass

    def __str__(self) -> str:
        return "Usuario: Correo={}, Identificador de país={}, Nombre={}".format(self.correo, self.idPais, self.nombre)

# Visualizar empleos dado el país.
def getListadoEmpresasPorPais(idPais: str):
    listadoEmpresas = list()
    response = requests.get(
        'http://verempleos.com:8088/empresa/empresa-pais/?IdPais=' + idPais)

    for empresa in response.json():
        listadoEmpresas.append(Empresa(empresa.get('descripcion'), empresa.get(
            'idUsuario'), empresa.get('nombreEmpresa'), empresa.get('paginaweb')))

    return listadoEmpresas

# Vacantes por país
def getVacantesPorPais(idPais: str):
    listadoVacantes = list()
    response = requests.get(
        'http://verempleos.com:8088/vacantes/porpais/?idPais=' + idPais)

    for vacante in response.json():
        listadoVacantes.append(Vacante(vacante.get('area'), vacante.get('descripcionPuesto'), vacante.get(
            'fechaPublicacion'), vacante.get('nombreEmpresa'), vacante.get('puesto'), vacante.get('url')))

    return listadoVacantes

def getVacantesDadoNombrePais(nombrePais: str):
    listado = getTodosPais()
    idPais = 0

    for pais in listado:
        if(pais.nombre == nombrePais):
            idPais = pais.idPais

    listadoVacantes = list()
    if idPais != 0:
        response = requests.get(
            'http://verempleos.com:8088/vacantes/porpais/?idPais=' + str(idPais))

        for vacante in response.json():
            listadoVacantes.append(Vacante(vacante.get('area'), vacante.get('descripcionPuesto'), vacante.get(
                'fechaPublicacion'), vacante.get('nombreEmpresa'), vacante.get('puesto'), vacante.get('url')))

    return listadoVacantes

# Visualizar todas las vacantes
def getTodasVacantes():
    listadoVacantes = list()
    response = requests.get(
        'http://verempleos.com:8088/vacantes')

    for vacante in response.json():
        listadoVacantes.append(Vacante(vacante.get('area'), vacante.get('descripcionPuesto'), vacante.get(
            'fechaPublicacion'), vacante.get('nombreEmpresa'), vacante.get('puesto'), vacante.get('url')))

    return listadoVacantes

# Todos los países
def getTodosPais():
    listadoPais = list()
    response = requests.get('http://verempleos.com:8088/pais')

    for vacante in response.json():
        listadoPais.append(Pais(vacante.get('id'), vacante.get('pais')))

    return listadoPais

def getTodosNombrePais():
    listadoPais = list()
    response = requests.get('http://verempleos.com:8088/pais')

    for vacante in response.json():
        listadoPais.append(vacante.get('pais'))

    return listadoPais


# Vacantes por empresa
def getVacantesPorEmpresa(idEmpresa: str):
    listadoVacantes = list()
    response = requests.get(
        'http://verempleos.com:8088/vacantes/porempresa/?idEmpresa=' + idEmpresa)

    for vacante in response.json():
        listadoVacantes.append(Vacante(vacante.get('area'), vacante.get('descripcionPuesto'), vacante.get(
            'fechaPublicacion'), vacante.get('nombreEmpresa'), vacante.get('puesto'), vacante.get('url')))

    return listadoVacantes

# Buscar usuario por correo electrónico
def getUsuario(correoElectronico: str):
    data = {'correo': correoElectronico}
    response = requests.post(
        'http://verempleos.com:8088/usuario/verificar/', json=data).json()
    
    return Usuario(correo=response.get('correo'), idPais=response.get('idPais'), nombre=response.get('nombre'))