from route import *

def main():
    ronda=read_route("./data/ruta.csv")
    print("First point: ", ronda[0])
    print("Last point: ",ronda[-1])
    readers=read_route("./data/ruta.csv")
    get_sub_route(readers, time(18,30,24),time(19,30,24))
    get_distance(readers)
if __name__=="__main__":
    main()