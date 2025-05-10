from linkedList import *

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

class StandardABR(BaseABR):
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
            
    def search(self, x, k):
        if x is None:
            return 0
        if k < x.key:
            return self.search(x.left, k)
        elif k > x.key:
            return self.search(x.right, k)
        elif k == x.key:
            return 1 + self.search(x.right, k)


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
        if x is None:
            return 0
        if x.key == k:
            return 1 + self.search(x.left, k) + self.search(x.right, k)
        elif k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
    
class ListABR(BaseABR):
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
            
    def search(self, x, k):
        if x is None:
            return 0
        if k < x.key:
            return self.search(x.left, k)
        elif k > x.key:
            return self.search(x.right, k)
        elif k == x.key:
            return 1 + x.list.size()

