import copy
import gc
from time import perf_counter 
from abr import *
from nodesContainer import *
from utils import *

def measure_time_search(key, tree):
  gc.collect()
  gc.disable()
  start = perf_counter()
  tree.search(tree.root, key)
  end = perf_counter()
  time = end - start
  gc.enable()
  return time
  
  
def test_search(nodes_container):
  ranges = nodes_container.get_ranges()
  times_standard = []
  times_flag = []
  times_list = []

  for rng in ranges:
    nodes1 = copy.deepcopy(nodes_container.get_nodes_list(rng))
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deepcopy(nodes1)

    std_tree = StandardABR()
    flag_tree = FlagABR()
    list_tree = ListABR()
    for node in nodes1:
      std_tree.insert(node)
    for node in nodes2:
      flag_tree.insert(node)
    for node in nodes3:
      list_tree.insert(node)

    # misura il tempo di ricerca per tutte le chiavi INSERITE
    inserted_keys = nodes_container.get_inserted_keys(rng)
    total_std = sum(measure_time_search(key, std_tree) for key in inserted_keys)
    total_flag = sum(measure_time_search(key, flag_tree) for key in inserted_keys)
    total_list = sum(measure_time_search(key, list_tree) for key in inserted_keys)

    times_standard.append(total_std)
    times_flag.append(total_flag)
    times_list.append(total_list)

    print(f"range={rng}: StandardABR search={total_std:.10f}s, FlagABR search={total_flag:.10f}s, ListABR search={total_list:.10f}s")

  percentages = nodes_container.get_percentages()
  create_and_show_plt(
    percentages,
    times_standard,
    "Percentuale di chiavi ripetute",
    "Tempo di ricerca (s)",
    "Confronto tempo di ricerca",
    label1="StandardABR",
    y_arr2=times_flag,
    label2="FlagABR",
    y_arr3=times_list,
    label3="ListABR"
  )
  
