from coordenadas3D import *

def test_distancia_haversine(c1:Coordenadas3D, c2: Coordenadas3D)->None:
    res = distancia_haversine(c1,c2)
    print(f"La distancia haversine entre {c1} y {c2} es {res}")


if __name__=="__main__":
    sevilla = Coordenadas3D(37.3828300, -5.9731700,0)
    cadiz = Coordenadas3D(36.5008762, -6.2684345,0)
    test_distancia_haversine(sevilla, cadiz)

