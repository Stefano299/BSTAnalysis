from abr import *
from time import perf_counter
from utils import *
import gc
import copy
from nodesContainer import *

def measure_time_insert(nodes, tree):
  gc.collect()
  gc.disable()
  start = perf_counter()
  for node in nodes:
    tree.insert(node)
  end = perf_counter()
  gc.enable()
  return end - start
  

def test_insert_sfl(nodes_container):
  ranges = nodes_container.get_ranges()
  times_standard = []
  times_flag = []
  times_list = []
  
  for rng in ranges:
    nodes1 = copy.deepcopy(nodes_container.get_nodes_list(rng))
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deepcopy(nodes1)

    flag_time = measure_time_insert(nodes1, FlagABR())
    list_time = measure_time_insert(nodes2, ListABR())
    standard_time = measure_time_insert(nodes3, StandardABR())

    times_flag.append(flag_time)
    times_list.append(list_time)
    times_standard.append(standard_time)

    print(f"range={rng}: FlagABR={flag_time:.6f}s,  ListABR={list_time:.6f}s,  StandardABR={standard_time:.6f}s")
    
  percentages = nodes_container.get_percentages()
  create_and_show_plt(
    percentages,
    times_flag,
    "Percentuale di chiavi ripetute",
    "Tempo di inserimento (s)",
    f"Confronto tempo di inserimento",
    label1="FlagABR",
    y_arr2=times_list,
    label2="ListABR",
    y_arr3=times_standard,
    label3="StandardABR"
  )


def test_insert_fl(nodes_container):
  ranges = nodes_container.get_ranges()
  times_flag = []
  times_list = []

  for rng in ranges:
    nodes1 = copy.deepcopy(nodes_container.get_nodes_list(rng))
    nodes2 = copy.deepcopy(nodes1)

    flag_time = measure_time_insert(nodes1, FlagABR())
    list_time = measure_time_insert(nodes2, ListABR())

    times_flag.append(flag_time)
    times_list.append(list_time)
    print(f"range={rng}: FlagABR={flag_time:.6f}s, ListABR={list_time:.6f}s")

  percentages = nodes_container.get_percentages()
  create_and_show_plt(
    percentages,
    times_flag,
    "Percentuale di chiavi ripetute",
    "Tempo di inserimento (s)",
    "Confronto tempo di inserimento",
    label1="FlagABR",
    y_arr2=times_list,
    label2="ListABR"
  )
  
