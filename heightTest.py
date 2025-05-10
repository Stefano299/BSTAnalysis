import copy
from abr import *
from utils import *


def test_height(nodes_container):
  ranges = nodes_container.get_ranges()
  heights_std = []
  heights_flag = []
  heights_list = []
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

    height_std = std_tree.get_height()
    height_flag = flag_tree.get_height()
    height_list = list_tree.get_height()
    
    heights_std.append(height_std)
    heights_flag.append(height_flag)
    heights_list.append(height_list)
    print(f"range: {rng}, StandardABR height: {height_std}, FlagABR height: {height_flag}, ListABR height: {height_list}")

  percentages = nodes_container.get_percentages()
  create_and_show_plt(
    percentages,
    heights_std,
    "Percentuale di chiavi ripetute",
    "Altezza albero",
    "Confronto altezza",
    label1="StandardABR",
    y_arr2=heights_flag,
    label2="FlagABR",
    y_arr3=heights_list,
    label3="ListABR"
  )
  
