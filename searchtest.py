import copy
import gc
from time import perf_counter  # added import for perf_counter
import numpy as np  # added numpy import
from abr import *
from utils import *

def measure_time_search(node, tree):
  gc.collect()
  gc.disable()
  start = perf_counter()
  result_list = tree.search(tree.root, node.key)
  result_list.search(node)
  end = perf_counter()
  time = end - start
  gc.enable()
  return time
  
def test_search(start_n, end_n, step, max_n):
  sizes = np.arange(start_n, end_n, step)
  times_standard = []
  times_flag = []
  times_list = []
  for n in sizes:
    # generate nodes and extract keys
    nodes1 = generate_random_nodes(n, max_n)
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deepcopy(nodes1)
    search_node = np.random.choice(nodes1)  
    # build trees
    std_tree = StandardABR()
    flag_tree = FlagABR()
    list_tree = ListABR()
    for node in nodes1:
      std_tree.insert(node)
    for node in nodes2:
      flag_tree.insert(node)
    for node in nodes3:
      list_tree.insert(node)
    # measure search
    t_std = measure_time_search(search_node, std_tree)
    t_flag = measure_time_search(search_node, flag_tree)
    t_list = measure_time_search(search_node, list_tree)
    times_standard.append(t_std)
    times_flag.append(t_flag)
    times_list.append(t_list)
    print(f"n={n}, StandardABR search: {t_std:.6f}s, FlagABR search: {t_flag:.6f}s, ListABR search: {t_list:.6f}s")
  # plot results
  create_and_show_plt(
    sizes,
    times_standard,
    "Dimensione albero",
    "Tempo di ricerca (s)",
    "Confronto tempo di ricerca: StandardABR vs FlagABR vs ListABR",
    label1="StandardABR",
    yArr2=times_flag,
    label2="FlagABR",
    yArr3=times_list,
    label3="ListABR"
  )
  
test_search(10, 4000, 50, 5)

  
"""
node1 = Node(4)
node2 = Node(5)
node3 = Node(5)
node4 = Node(5)

tree = ListABR()
tree.insert(node1)
tree.insert(node2)
tree.insert(node3)
tree.insert(node4)
results = LinkedList()
results = tree.search(tree.root, 5)
print(results.search(node2))
"""

