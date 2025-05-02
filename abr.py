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
    def getHeightAux(self, x):
        if x == None:
            return -1
        return 1 + max(self.getHeightAux(x.left), self.getHeightAux(x.right))
   
    def getHeight(self):
        return self.getHeightAux(self.root)
    
    def addNodes(self, n, maxNum):
        for i in range(n):
            key = random.randint(1, maxNum)
            self.insert(Node(key))

class StandardABR(BaseABR):
    def search(self, x, k):
        results = LinkedList()
        stack = [x]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.key == k:
                results.add(node)
                stack.append(node.left)
                stack.append(node.right)
            elif k < node.key:
                stack.append(node.left)
            else:
                stack.append(node.right)
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

    def search(self, x, k):
        results = LinkedList()
        stack = [x]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.key == k:
                results.add(node)
                stack.append(node.left)
                stack.append(node.right)
            elif k < node.key:
                stack.append(node.left)
            else:
                stack.append(node.right)
        return results
    
class ListABR(BaseABR):
    def search(self, x, k):
        results = LinkedList()
        node = x
        while node is not None:
            if node.key == k:
                results = node.list
                results.add(node)
                return results
            elif k < node.key:
                node = node.left
            else:
                node = node.right
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
def calcHeghit():
  heights = []
  nums = np.arange(30)
  for i in range(30):
    tree = ABR2()
    addNodes(tree, 10000)
    heights.append(tree.getHeight(tree.root))
    
  plt.plot(nums, heights)
  plt.xlabel('Iteration')
  plt.ylabel('Height')
  plt.title('Height of ABR2 after 1000 insertions')
  plt.grid(True)
  plt.show()
  
def heightTime():
  sizes = [3000] * 50
  tempi3 = []
  heights = []
  for n in sizes:
      tree3 = ABR3()
      t = measureTime(addNodes, tree3, n)
      tempi3.append(t)
      heights.append(tree3.getHeight(tree3.root))
  
  plt.plot(tempi3, heights)
  plt.xlabel('Iteration')
  plt.ylabel('Height')
  plt.title('Height of ABR2 after 1000 insertions')
  plt.grid(True)
  plt.show()
def insertTest(startN, endN, step, dupRate):
  sizes = list(range(startN, endN, step))  # Esempio: da 10 a 100 con passo 10

  tempi1 = []
  for n in sizes:
    standardABR = StandardABR()
    maxN = computeMaxNum(n, dupRate)
    t = measureTime(standardABR.addNodes, n, maxN)
    tempi1.append(t)

  tempi2 = []
  for n in sizes:
    flagABR = FlagABR()
    maxN = computeMaxNum(n, dupRate)
    t = measureTime(flagABR.addNodes, n, maxN)
    tempi2.append(t)

  tempi3 = []
  for n in sizes:
    listABR = ListABR()
    maxN = computeMaxNum(n, dupRate)
    t = measureTime(listABR.addNodes, n, maxN)
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

  createAndShowPlt(
    sizes, tempi1, 'Size', 'Tempo di inserimento (s)', 
    'Tempo di inserimento in ABR1 vs ABR2 vs ABR3',
    label1='ABR1', yArr2=tempi2, label2='ABR2', yArr3=tempi3, label3='ABR3'
  )
  
"""