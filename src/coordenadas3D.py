from typing import NamedTuple
from math import sin, cos, asin, sqrt, radians

Coordenadas3D = NamedTuple ("Coordenadas3D",
                            [("latitud", float), ("longitud",float), ("altitud",float)])

def a_radianes(c:Coordenadas3D)->Coordenadas3D:
    '''Devuelve una nueva coordenada con la latitud y longitud de la coordenada
    dada como parámetro convertida en radianes. La altitud es la misma que
    la coordenada original

    :param c: Coordenada con la latitud y la longitud en grados
    :type c: Coordenadas3D
    :return: Una coordenada en la que la latitud y la longitud está en radianes
    :rtype: Coordenadas3D
    '''
    return Coordenadas3D(radians(c.latitud), radians(c.longitud), c.altitud)

def distancia_haversine(coordenadas1:Coordenadas3D, coordenadas2: Coordenadas3D)->float:
    '''Calcula la distancia haversine entre dos puntos (en km)

    :param coordenadas1: Coordenadas del primer punto
    :type coordenadas1: Coordenadas3D
    :param coordenadas2: Coordenadas del segundo punto
    :type coordenadas2: Coordenadas3D
    :return: Distancia haversine en km
    :rtype: float
    '''
    #1. Convertir las coordenadas a radianes
    c1 = a_radianes(coordenadas1)
    c2 = a_radianes (coordenadas2)

    #2. Diferencia de latitudes y longitudes
    dif_lat = c2.latitud - c1.latitud
    dif_lon = c2.longitud - c1.longitud

    #3. Calcular a 
    a = sin(dif_lat/2)**2 + \
        cos(c1.latitud) * cos(c2.latitud) * sin (dif_lon/2) **2

    #4. calcular la distancia
    r = 6371 # Radio de la tierra
    return 2 * r * asin (sqrt(a))                            


def distancia_haversine_3D(coordenada1:Coordenadas3D, coordenada2:Coordenadas3D)->float:
    '''Calcula la distancia haversine entre dos puntos, teniendo en cuenta la altitud
    mediante el teorema de pitágoras.

    :param coordenadas1: Coordenadas del primer punto
    :type coordenadas1: Coordenadas3D
    :param coordenadas2: Coordenadas del segundo punto
    :type coordenadas2: Coordenadas3D
    :return: Distancia haversine en km, teniendo en cuenta la altitud
    :rtype: float
    '''
    pass