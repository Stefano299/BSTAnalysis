from utils import *

class NodesContainer:
  def __init__(self, n):   
    self.n = n
    self.nodes_lists = {}
    self.nodes_repetitions= {}
    self.percentages = None
    self.ranges = None
    
  def generate_nodes_lists(self, ranges):
    self.ranges = ranges
    for i in range(0, len(ranges)):
      nodes_list = generate_random_nodes(self.n, self.ranges[i])
      self.nodes_lists[ranges[i]] = nodes_list
      self.nodes_repetitions[ranges[i]] = compute_nodes_repetitions(nodes_list, self.ranges[i])
      
  def get_percentages(self):  #restituisce percentuale di nodi con chiavi uguali nelle varie liste dei nodi in nodes_lists
    self.percentages = [0] * len(self.ranges)
    for i in range(0, len(self.percentages)):
      repetitions = self.nodes_repetitions[self.ranges[i]]
      nonzero_elements = count_nonzero_elements(repetitions)
      self.percentages[i] = 100 - 100*(nonzero_elements/self.n)
    return self.percentages
  
  def get_inserted_keys(self, range):
    inserted_keys_full = {}
    for range in self.ranges:
      nodes_list = self.nodes_lists[range]
      inserted_keys = []
      for node in nodes_list:
        if node.key not in inserted_keys:
          inserted_keys.append(node.key)
      inserted_keys_full[range] = inserted_keys
    return inserted_keys_full[range]
  
  def get_nodes_list(self, range):
    return self.nodes_lists[range]
  
  def get_repetions(self, range):
    return self.nodes_repetitions[range]
  
  def get_ranges(self):
    return self.ranges
  
    
  


