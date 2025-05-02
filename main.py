from abr import *
import random
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from time import perf_counter
from time import process_time
from utils import *
import math
import timeit
import gc


def measure_time_insert(nodes, tree):
  #gc.collect()
  #gc.disable()
  start = perf_counter()
  for node in nodes:
    tree.insert(node)
  end = perf_counter()
  #gc.enable()
  return end - start
  

  
def test_insert(start_n, end_n, step, max_n):
  sizes = np.arange(start_n, end_n, step)
  times_flag = []
  times_list = []
  for n in sizes:
    keys = generate_random_keys(n, max_n)
    
    flag_time = measure_time_insert(keys, FlagABR())
    list_time = measure_time_insert(keys, ListABR())
    
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
    y_arr2=times_list,
    label2="ListABR"
  )

def main():
  test_insert(10, 5000, 100, 5)
  
if __name__ == "__main__":
    main()

