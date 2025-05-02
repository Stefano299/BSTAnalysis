import copy
import numpy as np
from abr import *
from utils import *


def test_height(start_n, end_n, step, max_n):
  sizes = np.arange(start_n, end_n, step)
  heights_std = []
  heights_flag = []
  heights_list = []
  for n in sizes:
    # generate nodes and extract keys
    nodes1 = generate_random_nodes(n, max_n)
    nodes2 = copy.deepcopy(nodes1)
    nodes3 = copy.deepcopy(nodes1)
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
    height_std = std_tree.get_height()
    height_flag = flag_tree.get_height()
    height_list = list_tree.get_height()
    heights_std.append(height_std)
    heights_flag.append(height_flag)
    heights_list.append(height_list)
    print(f"n={n}, StandardABR height: {height_std:.6f}s, FlagABR height: {height_flag:.6f}s, ListABR height: {height_list:.6f}s")
  # plot results
  create_and_show_plt(
    sizes,
    heights_std,
    "Dimensione albero",
    "Tempo di ricerca (s)",
    "Confronto tempo di ricerca: StandardABR vs FlagABR vs ListABR",
    label1="StandardABR",
    yArr2=heights_flag,
    label2="FlagABR",
    yArr3=heights_list,
    label3="ListABR"
  )
  
test_height(10, 4000, 40, 40)