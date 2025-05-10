import sys
from heightTest import *
from insertTest import *
from searchTest import *

sys.setrecursionlimit(10000)  #Per evitare errore durante i search

nodes_container = NodesContainer(10000)  #Le liste dei nodi avranno 10.000 elementi
ranges  = [500, 400, 300, 250, 200, 180, 150, 130, 100, 80, 55, 50, 40, 35, 26, 20, 17, 15, 13, 9, 7, 6, 3]
nodes_container.generate_nodes_lists(ranges)  #Genera liste con 10.000 nodi e chiavi che vanno fino ai range che si trovano nella lista ranges

test_insert_fl(nodes_container)
#test_insert_sfl(nodes_container)
#test_height(nodes_container)
#test_search(nodes_container)



