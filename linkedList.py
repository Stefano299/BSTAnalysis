class ListNode:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None     

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, node):
        temp = ListNode(node)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, node):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == node:
                found = True
            else:
                current = current.get_next()
        return found    

    def remove(self, node):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == node:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())