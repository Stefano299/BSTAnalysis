from abr import *
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from time import perf_counter
from utils import *
import gc
import copy


def measure_time_insert(nodes, tree):
  gc.collect()
  gc.disable()
  start = perf_counter()
  for node in nodes:
    tree.insert(node)
  end = perf_counter()
  gc.enable()
  return end - start
  

def test_insert3(start_n, end_n, step, max_n):
  sizes = np.arange(start_n, end_n, step)
  times_flag = []
  times_list = []
  times_standard = []
  for n in sizes:
    nodes1 = generate_random_nodes(n, max_n)
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deepcopy(nodes1)
    
    flag_time = measure_time_insert(nodes1, FlagABR())
    list_time = measure_time_insert(nodes2, ListABR())
    standard_time = measure_time_insert(nodes3, StandardABR())
    
    times_flag.append(flag_time)
    times_list.append(list_time)
    times_standard.append(standard_time)
    print(f"n={n}, FlagABR: {flag_time:.4f}s, ListABR: {list_time:.4f}s, StandardABR: {standard_time:.4f}s")

  create_and_show_plt(
    sizes,
    times_flag,
    "Numero di inserimenti",
    "Tempo di inserimento (s)",
    "Confronto tempo di inserimento: FlagABR vs ListABR vs StandardABR",
    label1="FlagABR",
    yArr2=times_list,
    label2="ListABR",
    yArr3=times_standard,
    label3="StandardABR"
  )
  
def test_insert2(start_n, end_n, step, max_n):
  sizes = np.arange(start_n, end_n, step)
  times_flag = []
  times_list = []
  for n in sizes:
    nodes1 = generate_random_nodes(n, max_n)
    nodes2 = copy.deepcopy(nodes1)

    
    flag_time = measure_time_insert(nodes1, FlagABR())
    list_time = measure_time_insert(nodes2, ListABR())
    
    times_flag.append(flag_time)
    times_list.append(list_time)
    print(f"n={n} FlagABR: {flag_time:.4f}s, ListABR: {list_time:.4f}s")

  create_and_show_plt(
    sizes,
    times_flag,
    "Numero di inserimenti",
    "Tempo di inserimento (s)",
    "Confronto tempo di inserimento: FlagABR vs ListABR",
    label1="FlagABR",
    yArr2=times_list,
    label2="ListABR"
  )
#test_insert3(10, 1000, 50, 5)
#test_insert3(10, 5000, 100, 20)
test_insert2(10, 15000, 400, 20)
#test_insert2(10, 1000, 25, 20)