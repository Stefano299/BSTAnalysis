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




def measureTimeInsert(keys, tree):
  #gc.collect()
  #gc.disable()
  start = perf_counter()
  for key in keys:
    tree.insert(Node(key))
  end = perf_counter()
  #gc.enable()
  return end - start
  

  
def testInsert(startN, endN, step, maxN):
  sizes = np.arange(startN, endN, step)
  times_flag = []
  times_list = []
  for n in sizes:
    keys = generateRandomKeys(n, maxN)
    
    flagTime = measureTimeInsert(keys, FlagABR())
    listTime = measureTimeInsert(keys, ListABR())
    
    times_flag.append(flagTime)
    times_list.append(listTime)
    print(f"n={n} FlagABR: {flagTime:.4f}s, ListABR: {listTime:.4f}s")

  createAndShowPlt(
    sizes,
    times_flag,
    "Numero di inserimenti",
    "Tempo di inserimento (s)",
    "Confronto tempo di inserimento: FlagABR vs ListABR",
    label1="FlagABR",
    yArr2=times_list,
    label2="ListABR"
  )

def main():
  testInsert(10, 5000, 100, 5)
  
if __name__ == "__main__":
    main()

