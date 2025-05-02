from abr import *
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from time import perf_counter
from utils import *
import gc
import copy


def measureTimeInsert(nodes, tree):
  gc.collect()
  gc.disable()
  start = perf_counter()
  for node in nodes:
    tree.insert(node)
  end = perf_counter()
  gc.enable()
  return end - start
  

def testInsert3(startN, endN, step, maxN):
  sizes = np.arange(startN, endN, step)
  times_flag = []
  times_list = []
  times_standard = []
  for n in sizes:
    nodes1 = generateRandomNodes(n, maxN)
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deppcopy(nodes1)
    
    flagTime = measureTimeInsert(nodes1, FlagABR())
    listTime = measureTimeInsert(nodes2, ListABR())
    standardTime = measureTimeInsert(nodes3, StandardABR())
    
    times_flag.append(flagTime)
    times_list.append(listTime)
    times_standard.append(standardTime)
    print(f"n={n}, FlagABR: {flagTime:.4f}s, ListABR: {listTime:.4f}s, StandardABR: {standardTime:.4f}s")

  createAndShowPlt(
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
  
def testInsert2(startN, endN, step, maxN):
  sizes = np.arange(startN, endN, step)
  times_flag = []
  times_list = []
  for n in sizes:
    nodes1 = generateRandomNodes(n, maxN)
    nodes2 = copy.deepcopy(nodes1)

    
    flagTime = measureTimeInsert(nodes1, FlagABR())
    listTime = measureTimeInsert(nodes2, ListABR())
    
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
#testInsert3(10, 1000, 50, 5)
#testInsert3(10, 5000, 100, 20)
testInsert2(10, 15000, 400, 20)
#testInsert2(10, 1000, 25, 20)