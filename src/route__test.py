from route import *

def main():
    ronda=read_route("./data/ruta.csv")
    print("First point: ", ronda[0])
    print("Last point: ",ronda[-1])
    readers=read_route("./data/ruta.csv")
    get_sub_route(readers, time(18,30,24),time(19,30,24))
    get_distance(readers)
    dist=distance(Coordenadas3D(36.74991256557405,-5.147951105609536,712.2000122070312), Coordenadas3D(36.742150420323014,-5.166372349485755,721.4000244140625))
    print(dist)
if __name__=="__main__":
    main()