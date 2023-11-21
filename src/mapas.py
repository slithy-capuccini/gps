# -*- coding: utf-8 -*-

import folium
from coordenadas3D import *
import webbrowser
import os
from typing import List

def crea_mapa(centro:Coordenadas3D, zoom:int=9)->folium.Map:
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    :param coordenadas: latitud y longitud del centro del mapa en pantalla
    :type coordenadas: Coordenadas (float, float)
    :param zoom: nivel del zoom con el que se muestra el mapa 
    :type zoom:int
    :return: objeto mapa creado
    :rtype: folium.Map
    '''
    mapa = folium.Map(location=(centro.latitud, centro.longitud), 
                      zoom_start=zoom)
    return mapa

def agrega_polilinea(mapa:folium.Map, puntos:List[Coordenadas3D], color:str)->folium.PolyLine:
    '''Añade una polilínea a un mapa
    :param mapa: Objeto con el mapa donde se va a dibujar la polilínea
    :type mapa: folium.Map
    :param puntos: Lista de puntos que serán los vértices de la polilínea
    :type puntos: List[Coordenadas3D]
    :param color: Color de la polilínea
    :type color: str
    :return: El objeto polilínea creado
    :rtype: folium.PolyLine
    '''
    coordenadas = [(p.coordenadas.latitud, p.coordenadas.longitud) \
                     for p in puntos]
    polilinea= folium.PolyLine(locations=coordenadas, color=color)
    polilinea.add_to(mapa)
    return polilinea

def agrega_marcador (mapa:folium.Map, coordenadas:Coordenadas3D, etiqueta:str, color:str):
    '''
    Función que agrega un marcador del color dado como parámetro con un icono de tipo señal de información 
    al mapa dado como parámetro. El marcador se mostrará en el punto del mapa dado por la latitud y longitud de las coordenadas dadas
    como parámetro y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    :param mapa: objeto mapa al que se le van a agregar el marcador
    :type: folium.Map
    :param coordenadas: coordenadas del punto en el que se dibujará el marcador
    :type coordenadas: Coordenadas3D
    :param etiqueta: texto de la etiqueta que se asociará al marcador 
    :type etiqueta: str
    :param color: color del marcador
    :type color: str
    :return: objeto marcador creado 
    :rtype: folium.Marker
    '''
    marcador = folium.Marker((coordenadas.latitud,coordenadas.longitud), 
                   popup=etiqueta, 
                   icon=folium.Icon(color=color, icon='info-sign')) 
    marcador.add_to(mapa)
    return marcador

def guarda_mapa(mapa, ruta_fichero):
    '''Guarda un mapa como archivo html

    :param mapa: Mapa a guardar
    :type mapa: folium.Map
    :param ruta_fichero: Nombre y ruta del fichero
    :type ruta_fichero: str
    '''
    mapa.save(ruta_fichero)
    # Abre el fichero creado en un navegador web
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))
