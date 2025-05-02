# Nella lista concatenata aggiungo elementi in testa


class ListNode:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None     # come Nil e Null

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class List2Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Singly linked list for duplicates
class Linked2List:
    def __init__(self):
        self.head = None

    def add(self, key):
        new_node = List2Node(key)
        new_node.next = self.head
        self.head = new_node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = ListNode(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

# Cerchiamo  elementi e stampiamo la lista
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def print_l(self):
        current = self.head
        previous = None
        while current != None:
            print('..' , current.get_data())
            current = current.get_next()       

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())