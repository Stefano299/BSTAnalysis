import random
from linkedlist import *

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.direction = -1
        self.list = LinkedList()

class BaseABR:
    def __init__(self):
        self.root = None
          
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x
      
    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x
      
    def inorder_walk(self, x):
        if x != None:
            self.inorder_walk(x.left)
            print(x.key)
            self.inorder_walk(x.right)
    def get_height_aux(self, x):
        if x == None:
            return -1
        return 1 + max(self.get_height_aux(x.left), self.get_height_aux(x.right))
   
    def get_height(self):
        return self.get_height_aux(self.root)
    
    def add_nodes(self, n, max_num):
        for i in range(n):
            key = random.randint(1, max_num)
            self.insert(Node(key))

class StandardABR(BaseABR):
    def search(self, x, k, results = None):
        if results is None:
            results = LinkedList()
        if x is None:
            return 
        if x.key == k:
            results.add(x)
            self.search(x.right, k, results)
        elif k < x.key:
            self.search(x.left, k, results)
        else:
            self.search(x.right, k, results)
        return results

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

class FlagABR(BaseABR):    
    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key == x.key:
                x.direction *= -1
                if x.direction == -1:
                    x = x.left
                else:
                    x = x.right
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        elif z.key > y.key:
            y.right = z
        else:
            y.direction *= -1
            if y.direction == 1:
                y.left = z
            else:
                y.right = z

    def search(self, x, k, results = None):
        if results is None:
            results = LinkedList()
        if x is None:
            return 
        if x.key == k:
            results.add(x)
            self.search(x.left, k, results)
            self.search(x.right, k, results)
        elif k < x.key:
            self.search(x.left, k, results)
        else:
            self.search(x.right, k, results)
        return results
    
class ListABR(BaseABR):
    def search(self, x, k):
        results = None
        if x is None:
            return LinkedList()  #ritorna una LinkedList vuota se non trova nulla
        if x.key == k:
            results = x.list
            results.add(x)
        elif k < x.key:
            results = self.search(x.left, k)
        else:
            results = self.search(x.right, k)
        return results
    
    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key == x.key:
              x.list.add(z)
              return
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

"""
def calc_heghit():
  heights = []
  nums = np.arange(30)
  for i in range(30):
    tree = ABR2()
    add_nodes(tree, 10000)
    heights.append(tree.get_height(tree.root))
    
  plt.plot(nums, heights)
  plt.xlabel('Iteration')
  plt.ylabel('Height')
  plt.title('Height of ABR2 after 1000 insertions')
  plt.grid(True)
  plt.show()
  
def height_time():
  sizes = [3000] * 50
  tempi3 = []
  heights = []
  for n in sizes:
      tree3 = ABR3()
      t = measure_time(add_nodes, tree3, n)
      tempi3.append(t)
      heights.append(tree3.get_height(tree3.root))
  
  plt.plot(tempi3, heights)
  plt.xlabel('Iteration')
  plt.ylabel('Height')
  plt.title('Height of ABR2 after 1000 insertions')
  plt.grid(True)
  plt.show()
def insert_test(start_n, end_n, step, dup_rate):
  sizes = list(range(start_n, end_n, step))  # Esempio: da 10 a 100 con passo 10

  tempi1 = []
  for n in sizes:
    standard_abr = StandardABR()
    max_n = compute_max_num(n, dup_rate)
    t = measure_time(standard_abr.add_nodes, n, max_n)
    tempi1.append(t)

  tempi2 = []
  for n in sizes:
    flag_abr = FlagABR()
    max_n = compute_max_num(n, dup_rate)
    t = measure_time(flag_abr.add_nodes, n, max_n)
    tempi2.append(t)

  tempi3 = []
  for n in sizes:
    list_abr = ListABR()
    max_n = compute_max_num(n, dup_rate)
    t = measure_time(list_abr.add_nodes, n, max_n)
    tempi3.append(t)

  # aggiunta smoothing con media mobile
  def moving_average(data, window=5):
      half = window // 2
      smoothed = []
      for i in range(len(data)):
          start = max(0, i - half)
          end = min(len(data), i + half + 1)
          smoothed.append(sum(data[start:end]) / (end - start))
      return smoothed

  tempi1 = moving_average(tempi1)
  tempi2 = moving_average(tempi2)
  tempi3 = moving_average(tempi3)

  create_and_show_plt(
    sizes, tempi1, 'Size', 'Tempo di inserimento (s)', 
    'Tempo di inserimento in ABR1 vs ABR2 vs ABR3',
    label1='ABR1', y_arr2=tempi2, label2='ABR2', y_arr3=tempi3, label3='ABR3'
  )
  
"""