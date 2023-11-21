import csv
from datetime import datetime
from datetime import time
from typing import NamedTuple, List
from coordenadas3D import Coordenadas3D
import math

Point=NamedTuple("Point", [("time", time), ("position", Coordenadas3D)])

#EX 1
def read_route(file:str)->List[Point]:
    with open(file) as f:
        lista_out=[]
        csv_reader=csv.reader(f)
        lista_out=[Point(datetime.strptime(d_time,"%H:%M:%S").time(),Coordenadas3D(float(d_latitude),float(),float(d_deep))) for d_time, d_latitude, d_longitud, d_deep in csv_reader]
        return lista_out
def get_sub_route(track:List[Point], iniT:time, finalT:time)->List[Point]:
    lista_final=[]
    for i in track:
         if i.time>iniT and i.time <finalT:
            print(i)
            lista_final.append(i)
    return lista_final

def get_distance(track: List[Point])->float:
    #implement harvesine_distanc
    lista_2=[i.position.latitude for i in track]
    lista_3=lista_2[1:]

def distance(coordinada1, coordinada2):
    alt_dif=(coordinada1.altitude-coordinada2.altitude)/100

    return math.squart(distancia2d**2)